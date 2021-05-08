FROM python:3.8.5

ENV PATH="/scripts:${PATH}"


COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /saas
COPY ./saas /saas
WORKDIR /saas
COPY ./scripts /scripts

RUN chmod +x /scripts/entrypoint.sh

#might have to add these lines
RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

RUN useradd -ms /bin/bash user
RUN chown -R user:user /vol
RUN chmod -R 755 /vol/web

CMD ["entrypoint.sh"]