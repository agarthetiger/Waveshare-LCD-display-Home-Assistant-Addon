ARG BUILD_FROM
FROM $BUILD_FROM

RUN apk add --no-cache python3 py3-pip
FROM python:3
RUN \
  pip install --upgrade pip && \
  pip3 install --no-cache-dir gpiod && \
  pip3 install --no-cache-dir smbus

COPY bin/main.py /bin/main.py
COPY lib /lib
COPY font /font

CMD [ "python", "./bin/main.py" ]
