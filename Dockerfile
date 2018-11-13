FROM python:3.7-alpine as base

RUN apk update && apk add gcc musl-dev openldap-dev

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.7-alpine

COPY --from=base /usr/local/lib/python3.7/site-packages /usr/local/lib/python3.7/site-packages

RUN apk add --no-cache libldap

EXPOSE 8000

WORKDIR /usr/src/app

COPY . .
