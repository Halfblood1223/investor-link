# django-adebanjo

There are 4 processes in this app.

1st - Front End Django Code

2nd - Redis Server

3rd - Celery Processes

4th - Stripe Webhook

Commands for Startup
---------------------

1st (Starts redis-server) - redis-server

2nd (Starts celery beat) - celery -A vancouvar beat -l info

3rd (Starts celery worker) - celery -A vancouvar worker -l info -P solo

4th (Starts server) - python manage.py runserver

NOTES
-----

The stripe webhook receives requests at /plans/stripehook. Let me know where it is being hosted so I can register the webhook in Stripe and provide the endpoint secret.
The endpoint secret variable is used in the stripehook view which is in the plans app. I will provide you with an updated key to replace that one.
