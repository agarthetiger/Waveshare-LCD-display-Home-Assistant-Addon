ARG BUILD_FROM
FROM $BUILD_FROM

RUN apk add --no-cache \
  python3 \
  py3-pip \
  wget \
  unzip \
  swig3.0 \
  python-dev \
  python3-dev \
  python-setuptools \
  python3-setuptools
FROM python:3

# Install lgpio, details from https://github.com/joan2937/lg
RUN \
  wget https://github.com/joan2937/lg/archive/master.zip && \
  unzip master.zip && \
  cd lg-master && \
  make && \
  make install

COPY requirements.txt /bin/requirements.txt
RUN \
  pip install --upgrade pip && \
  pip3 install -r /bin/requirements.txt

ADD lib /bin/lib
ADD font /bin/font
COPY bin/main.py /bin/main.py

# RUN pip3 install /bin/lib/lgpio-0.2.2.0.tar.gz

CMD [ "python", "./bin/main.py" ]
