FROM python:3.8-slim

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

ENV STATIC_ROOT /data/static/
ENV MEDIA_ROOT /data/media/
ENV LOG_ROOT /data/log/

RUN apt-get update \
    && apt-get install -y --no-install-recommends python3-dev default-libmysqlclient-dev build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt \
    && rm -rf /tmp/requirements.txt

RUN mkdir -p STATIC_ROOT \
    && mkdir -p MEDIA_ROOT \
    && mkdir -p LOG_ROOT

WORKDIR /app
COPY ./scripts /scripts/
COPY ./app .

ENTRYPOINT ["/scripts/docker/wait_for_it.sh", "database:3306" , "-s", "--"]
CMD ["/scripts/docker/start.sh"]