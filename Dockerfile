FROM python:3.7-alpine3.8

RUN apk update && apk upgrade \
    && pip install pipenv

ENV PYTHONUNBUFFERED=1 \
    PYTHONIOENCODING=UTF-8

# Set the working directory to /opt/polestar
WORKDIR /opt/polestar/

# Copy the current directory contents into the container at /opt/polestar
ADD . /opt/polestar/

# Install any needed packages specified in requirements.txt


RUN pip install -r requirements.txt

WORKDIR /opt/polestar/polestarproject/

RUN python manage.py makemigrations

RUN python manage.py migrate

RUN python manage.py test

CMD ["python","manage.py" ,"runserver", "0.0.0.0:8000"]

EXPOSE 8000