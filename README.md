# learn-docker
Learn docker - from basicsi


1. Build a docker image based on ubuntu machine and add a very simple helloworld sample app to it. Taka a look at `Dockerfile` for details
2. You can build the image by running `docker build -t sample-app:latest .` - this builds the app from instructions in dockerfile and tags it as sample-app
3. You can also run it by running `docker-compose up` - This uses the docker-compose.yaml file to spin up the whole application according to the config
