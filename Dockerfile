# Set base image (host OS)
FROM python:3.10.6-slim-buster

# By default, listen on port 5000
EXPOSE 5000/tcp

# Copy the dependencies file to the working directory
COPY ./requirements.txt /app/requirements.txt

# Set the working directory in the container
WORKDIR /app

# Install any dependencies
RUN pip3 install -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY . /app

# Specify the command to run on container start
CMD [ "python3", "server.py" ]