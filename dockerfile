FROM python:3.8

ENV PATH="/scripts:${PATH}"


COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN adduser -D user
USER user
RUN mkdir /saas
COPY ./saas /saas
WORKDIR /saas
COPY ./scripts /scripts

#might have to add these lines
RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

RUN useradd -ms /bin/bash user
RUN chown user:user -R /vol
RUN chmod -R 755 /vol/web

CMD ["python manage.py collectstatic --noinput", "uwsgi --socket :8000 --master --enable-threads --module app.wsgi"]