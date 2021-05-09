# pull official base image
FROM python:3.8.3

# set work directory
WORKDIR /usr/src/app

# install dependencies
RUN pip install --upgrade pip
COPY ./app/requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY ./app .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]