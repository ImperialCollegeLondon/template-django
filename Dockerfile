FROM python:3-alpine

EXPOSE 8000

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=nobody . /usr/src/app
WORKDIR /usr/src/app
USER nobody
# RUN python manage.py collectstatic --no-input # STATIC_ROOT setting must be set
