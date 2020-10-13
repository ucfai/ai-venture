FROM python:3-slim

# copy program files
COPY . /app

# specify working directory
WORKDIR /app

# install requirements
RUN pip install -r requirements.txt

# open port
ENV PORT 8080


# run application
CMD ["python", "app.py"]

