import logging
import smbus
import time

# I2C Addresses
ADDR_ARGONONEFAN=0x1a
ADDR_ARGONONEREG=ADDR_ARGONONEFAN

# ARGONONEREG Addresses
ADDR_ARGONONEREG_DUTYCYCLE=0x80
ADDR_ARGONONEREG_FW=0x81
ADDR_ARGONONEREG_CTRL=0x86

version = "v1.0.0"

logging.basicConfig(
    datefmt="%Y-%m-%d %H:%M",
    format="{asctime} - {levelname} - {message}",
    level=logging.DEBUG,
    style="{",
)

logging.info(f"Starting Argon Fan HAT control AddOn {version}")

def argon_initialize_bus_obj():
    try:
        return smbus.SMBus(1)
    except Exception:
        try:
            # Older version
            return smbus.SMBus(0)
        except Exception:
            print("Unable to detect i2c")
            return None

def argonregister_getbyte(busobj, address):
    if busobj is None:
        return 0
    return busobj.read_byte_data(ADDR_ARGONONEREG, address)

def argonregister_setbyte(busobj, address, bytevalue):
    if busobj is None:
        return
    busobj.write_byte_data(ADDR_ARGONONEREG, address, bytevalue)
    time.sleep(1)

def argonregister_setfanspeed(busobj, fanspeed):
    if busobj is None:
        return

    if fanspeed > 100:
        fanspeed = 100
    elif fanspeed < 0:
        fanspeed = 0

    busobj.write_byte(ADDR_ARGONONEFAN, fanspeed)
    time.sleep(1)


def get_cpu_temp():
    with open('/sys/class/thermal/thermal_zone0/temp', 'rt') as f:
        temp = (int)(f.read() ) / 1000.0
    return temp

def get_fan_speed_for_temp(temp):
    if(temp > 40): # Default is 40 (degrees C)
        speed = 20
    elif(temp > 45):
        speed = 40
    elif(temp > 50):
        speed = 50
    elif(temp > 55):
        speed = 75
    elif(temp > 60):
        speed = 90
    elif(temp > 65):
        speed = 100
    else:
        speed = 0
    return speed


# Initialize I2C Bus
bus = argon_initialize_bus_obj()

logging.info(f"Initialised Argon Fan HAT control AddOn {version}")

try:
    INITIALSPEEDVAL = 200   # ensures fan speed gets set during initialization (e.g. change settings)
    prev_speed=INITIALSPEEDVAL

    while True:
        cpu_temp = get_cpu_temp()
        new_speed = get_fan_speed_for_temp(temp=cpu_temp)

        if prev_speed == new_speed:
            time.sleep(30)
            continue
        elif new_speed < prev_speed and prev_speed != INITIALSPEEDVAL:
            # Pause 30s before speed reduction to prevent fluctuations
            time.sleep(30)

        try:
            argonregister_setfanspeed(bus, new_speed)
            prev_speed = new_speed
            time.sleep(30)
        except IOError:
            time.sleep(60)

# except IOError as e:
#     oled.Closebus()
#     print(e)

except KeyboardInterrupt:
    print("ctrl + c:")
    argonregister_setfanspeed(bus, 50)
