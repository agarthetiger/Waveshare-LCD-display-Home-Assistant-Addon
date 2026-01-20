# import sys
import time
import logging
# import psutil
import shutil
import socket
#sys.path.append("..")
from lib import LCD_2inch
from PIL import Image,ImageDraw,ImageFont

version = "v0.0.20"
# Raspberry Pi (BCM/WiringPi) pin configuration:
RST = 27
DC = 25
BL = 18
bus = 0 
device = 0 

logging.basicConfig(
    datefmt="%Y-%m-%d %H:%M",
    format="{asctime} - {levelname} - {message}",
    level=logging.DEBUG,
    style="{",
)
logging.info(f"Starting Waveshare LCD display AddOn {version}")
Font02 = ImageFont.truetype("/bin/font/Font02.ttf",40)

def display_init():
    # display with hardware SPI:
    ''' Don't create multiple display objects. '''
    #disp = LCD_2inch.LCD_2inch(spi=SPI.SpiDev(bus, device),spi_freq=10000000,rst=RST,dc=DC,bl=BL)
    display = LCD_2inch.LCD_2inch()
    display.Init()
    display.clear()
    # Set the backlight brightness
    display.bl_DutyCycle(40)
    return display


def get_sys_info():
    # Returns a dict containing information about the currently running system
    sys_info = {}
    sys_info['hostname'] = socket.gethostname()
    sys_info['ip_addr'] = get_ip()
    sys_info['cpu_temp'] = get_cpu_temp()
    sys_info['fan_speed'] = "Unknown"

    total, used, free = shutil.disk_usage("/")
    sys_info['disk_total_gib'] = total // (2**30)
    sys_info['disk_used_gib'] = used // (2**30)
    sys_info['disk_free_gib'] = free // (2**30)

    return sys_info


# def get_cpu_temp():
#     temp = psutil.sensors_temperatures()['cpu_thermal'][0].current
#     return temp


def get_cpu_temp():
    with open('/sys/class/thermal/thermal_zone0/temp', 'rt') as f:
        temp = (int)(f.read() ) / 1000.0
    return temp


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        # doesn't even have to be reachable
        s.connect(('10.254.254.254', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


disp = display_init()
logging.info(f"Initialised Starting Waveshare LCD display AddOn {version}")

try:
    while True:
        # Create blank image for drawing. Display is portrait, height 320, width 240.
        # Draw display as though it's landscape and rotate before displaying. 
        image1 = Image.new("RGB", (disp.height, disp.width ), "WHITE")
        draw = ImageDraw.Draw(image1)

        sys_info = get_sys_info()

        #draw.rectangle([(0,65),(140,100)],fill = "WHITE")
        # (0,0) is the top left corner, (320,240) is the bottom right.
        draw.text((5, 5), f"Name: {sys_info['hostname'].upper()}", fill = "BLACK",font=Font02)

        draw.rectangle([(0,50),(320,95)],fill = "BLUE")
        draw.text((5, 50), f"IP: {sys_info['ip_addr']}", fill = "WHITE",font=Font02)
        draw.text((5, 95), f"CPU temp: {sys_info['cpu_temp']:2.1f}", fill = "GREEN",font=Font02)
        draw.text((5, 140), f"Disk: {sys_info['disk_total_gib']} GiB", fill = "GREEN",font=Font02)
        draw.text((5, 185), f"Free: {sys_info['disk_free_gib']} GiB", fill = "GREEN",font=Font02)

        image1=image1.rotate(180)
        disp.ShowImage(image1)
        time.sleep(1)

except IOError as e:
    logging.info(e)

except KeyboardInterrupt:
    disp.module_exit()
    logging.info("Keyboard Interrupt detected, quitting")
    exit()
