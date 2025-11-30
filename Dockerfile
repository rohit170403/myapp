FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    python3 python3-pip git zip unzip openjdk-8-jdk \
    autoconf libtool pkg-config zlib1g-dev libncurses5-dev \
    libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev

RUN pip3 install buildozer cython

WORKDIR /app
COPY . .

CMD ["buildozer", "android", "debug"]