FROM python:3.6

# set a directory for the app
WORKDIR /app

# copy all the files to the container
COPY . .

# install dependencies
RUN pip install -U pip
RUN pip install -r requirements.txt

# tell the port number the container should expose
# docker run -p 80:80 --rm {IMAGE}
EXPOSE 80

# Set labels
LABEL author=samuraii

# run the command
CMD ["python", "app.py"]
