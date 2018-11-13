FROM python:3-alpine3.7 as base

RUN apk add --no-cache gcc musl-dev libffi-dev openldap-dev git

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3-alpine3.7

COPY --from=base /usr/local/lib/python3.7/site-packages /usr/local/lib/python3.7/site-packages

RUN apk add --no-cache xmlsec

EXPOSE 8000

WORKDIR /usr/src/app

COPY . .
