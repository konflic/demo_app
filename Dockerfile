FROM python:3.6

# set a directory for the app
WORKDIR /app

# copy requirements
COPY requirements.txt .

# install dependencies
RUN pip install -U pip && pip install -r requirements.txt

# copy the rest of the app
COPY . .

# tell the port number the container should expose
# docker run -p 80:80 --rm {IMAGE}
EXPOSE 80

ENV PORT=5000

# Set labels
LABEL author=samuraii

# run the command
CMD ["python", "app.py"]
