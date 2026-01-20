ARG BUILD_FROM
FROM $BUILD_FROM

RUN apk add --no-cache python3 py3-pip
FROM python:3
COPY requirements.txt /bin/requirements.txt
RUN \
  pip install --upgrade pip && \
  pip3 install -r /bin/requirements.txt

ADD lib /bin/lib
ADD font /bin/font
COPY bin/main.py /bin/main.py

CMD [ "python", "./bin/main.py" ]
