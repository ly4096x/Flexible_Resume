FROM ubuntu:20.04
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -q \
    && apt-get install --no-install-recommends -qy curl jq texlive-full python-pygments gnuplot software-properties-common make git python3.8 python3-jinja2 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /data
VOLUME ["/data"]