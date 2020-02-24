FROM debian:stretch-slim
LABEL maintainer="CyberHead <info@cyberhead.uk>" \
    org.label-schema.name="CyberHead" \
    org.label-schema.url="http://www.cyberhead.uk/" \
    org.label-schema.version="1.0" 

ENV SERIES 5.0
ENV LANG C.UTF-8

RUN apt-get update
    && apt-get install python3 \
                       python3-pip


RUN git clone https://github.com/TheCyberHead/CyberHead
    && cd CyberHead
    && pip install -r requirements.txt


EXPOSE 80

ENTRYPOINT ["/home/CyberHead"]
