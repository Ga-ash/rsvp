FROM ubuntu:22.04
ENV DEBIAN_FRONTEND noninteractive
ENV TZ Etc/UTC


RUN apt-get update -y && apt-get upgrade -y && apt-get install -y --no-install-recommends \
    python3-pip python3-pip-whl

ENV PYTHONDONTWRITEBYTECODE=1


# Set the working directory to /app
WORKDIR /app


# Copy the current directory contents into the container at /app
COPY . /app/

RUN ln -s /usr/bin/python3 /usr/bin/python && \
    pip install --no-cache-dir -r requirements.txt

# Install any needed packages specified in requirements.txt
EXPOSE 8000

# Run Django server by executing manage.py runserver
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
