# Select the base image
FROM  python:3.10

# Set the working directory
WORKDIR /code

# Install ffmpeg
RUN apt-get update -y
RUN apt-get install ffmpeg libsm6 libxext6  -y 

# Install pyaudio
RUN apt-get install libasound-dev libportaudio2 libportaudiocpp0 portaudio19-dev -y
RUN pip install pyaudio

# Copy the requirements file
COPY ./requirements.txt /code/requirements.txt

# Install the dependencies
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the source code
COPY ./app /code/app

# Expose the port
EXPOSE 80

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]