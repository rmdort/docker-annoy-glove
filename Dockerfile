FROM fnndsc/ubuntu-python3
RUN apt-get update -y
RUN apt-get install -y git
RUN pip install mprpc annoy numpy

COPY . /app
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8
WORKDIR /app
EXPOSE 9033
ENTRYPOINT ["sh", "entrypoint.sh"]
