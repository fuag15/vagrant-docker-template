FROM ubuntu:14.04
WORKDIR /tmp

# install python 3.5.1
RUN apt-get update \
 && apt-get install --assume-yes wget libssl-dev openssl build-essential \
 && wget https://www.python.org/ftp/python/3.5.1/Python-3.5.1.tgz \
 && tar -xzf ./Python-3.5.1.tgz \
 && cd Python-3.5.1 \
 && ./configure \
 && make \
 && make install

# install python 3.5.1 virtualenv
RUN /usr/local/bin/pip3.5 install --upgrade pip \
 && /usr/local/bin/pip3.5 install virtualenv

# install npm for convienient testing
RUN apt-get install --assume-yes npm \
 && ln -s /usr/bin/nodejs /usr/bin/node \
 && npm install -g wscat

# install curl for convinient testing
RUN apt-get install --assume-yes curl

# install application files
COPY ["./", "/opt/tornadowebsocket"]

# move to the relevant dir
WORKDIR /opt/tornadowebsocket

# setup virtual env and install application
RUN make install

# expose our port
EXPOSE 80

# start the server
CMD ["/opt/virtualenvs/tornadowebsocket/bin/tornadowebsocket"]

