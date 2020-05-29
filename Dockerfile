FROM ubuntu:latest

WORKDIR /app
ADD ./cyberhead /app

RUN apt-get update
RUN apt-get install -y python3 python3-pip telnet curl nodejs
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN apt-get update
RUN apt-get install -y yarn