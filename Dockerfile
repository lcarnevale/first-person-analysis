From ubuntu:latest
LABEL maintainer="Lorenzo Carnevale"
LABEL email="lorenzocarnevale@gmail.com"

COPY requirements.txt /opt/app/requirements.txt

# application folder
WORKDIR /opt/app

# update source
RUN apt update && \
		apt upgrade -y && \
    apt install -y python3 python3-pip && \
    pip3 install -r requirements.txt

COPY app /opt/app

RUN python3 -m nltk.downloader punkt
RUN python3 -m nltk.downloader averaged_perceptron_tagger

# copy config files
EXPOSE 5005

CMD ["python3", "app.py"]
