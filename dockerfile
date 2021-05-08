FROM python:3.8

ENV PATH="/scripts:${PATH}"


COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /saas
COPY ./saas /saas
WORKDIR /saas
COPY ./scripts /scripts

#might have to add these lines
RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

CMD ["python manage.py collectstatic --noinput", "uwsgi --socket :8000 --master --enable-threads --module app.wsgi"]