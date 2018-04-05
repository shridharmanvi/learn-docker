# Base image
FROM ubuntu:latest

# Metadata
MAINTAINER Shridhar Manvi "shridharmanvi@gmail.com"

# Install python
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

# Copy content to current directory
COPY . /opt/myapp
WORKDIR /opt/myapp

RUN pip install -r requirements.txt

# ENTRYPOINT ["python"]
EXPOSE 5000

CMD ["python", "app.py"]
