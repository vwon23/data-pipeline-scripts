# # Use Ubuntu 22.4
# FROM ubuntu:jammy

# # install python
# RUN apt-get update && apt-get install -y \
#     python3.9 \
#     python3-pip \
#     vim

# # install pip3 packages specified in requirements.txt file
# COPY requirements.txt .
# RUN pip3 install -r requirements.txt


# Use python slim
FROM python:3.9-slim

COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt


# Copy app_run code into image
WORKDIR /app
COPY ./app_run /app/app_run/

# # Set default commands
# CMD ["bash", "-c", "python3 app_run/scripts/sf_create_environ.py"]