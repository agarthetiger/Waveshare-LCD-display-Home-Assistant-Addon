ARG BUILD_FROM
FROM $BUILD_FROM

RUN apk add --no-cache python3 py3-pip
FROM python:3
COPY requirements.txt /bin/requirements.txt
RUN \
  pip install --upgrade pip && \
  pip3 install --no-cache-dir  && \
  pip3 install --no-cache-dir  && \
  pip3 install -r /bin/requirements.txt

COPY bin/main.py /bin/main.py
COPY lib/*.* /lib
COPY font/*.* /font

CMD [ "python", "./bin/main.py" ]
