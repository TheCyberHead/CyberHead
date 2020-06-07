FROM ubuntu:latest


ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /app
ADD ./cyberhead /app

RUN apt-get update
RUN apt-get install -y 	python3 \
			python3-pip \
			npm \
			telnet \
			curl \
			make \
			g++ \
			libssl-dev \
			git \
			vim

RUN npm install -g yarn

RUN yarn --cwd ./web install
RUN pip3 install -r ./requirements.txt

RUN ./init.sh
