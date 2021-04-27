FROM python:3.6.8-alpine3.9
ENV PYTHONUNBUFFERED=1 \
    GROUP_ID=1000 \
    USER_ID=1000

WORKDIR /var/www/
COPY requirements.txt /var/www/requirements.txt
RUN pip install -r requirements.txt
COPY . /var/www/

RUN addgroup -g $GROUP_ID www
RUN adduser -D -u $USER_ID -G www www -s /bin/sh

USER www

EXPOSE 8000

CMD ["gunicorn", "-w", "4", "--preload","--bind", "0.0.0.0:8000","wsgi"]
