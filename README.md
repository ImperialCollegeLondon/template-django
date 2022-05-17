# template-django

This is a minimal template for a Django project using docker.

After downloading this repo and changing the top-level folder name, these are the steps to setup your django project:

 1. Create and activate a Virtual Environment inside this folder:

    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```

 1. Install requirements:

    ```bash
    python -m pip install -U pip
    python -m pip install -r requirements.in
    ```

 1. Create a `requirements.txt` to use the specific versions you just installed. This file is required for Docker image:

    ```bash
    python -m pip freeze > requirements.txt
    ```

 1. Install the git hooks (you may have to install the development requirements if they are not already installed globally with `pip install requirements-dev.txt`):

    ```
    pre-commit install
    ```

 1. Create Django project using [the `django-admin` tool](https://docs.djangoproject.com/en/4.0/ref/django-admin/#startproject):

    ```bash
    django-admin startproject <mysite> .
    ```

    Make sure you replace `<mysite>` with the name you want for your project. Then make sure you change the lines referencing `mysite` in `.dockerignore` and `.flake8` to your chosen project name.

    You should now have a directory structure that looks like this (note new file `manage.py` and new directory `mysite/`):

    ```
    .
    ├── .dockerignore
    ├── .flake8
    ├── .gitignore
    ├── .pre-commit-config.yaml
    ├── .python-version
    ├── .venv
    │   ├── ...
    ├── Dockerfile
    ├── README.md
    ├── docker-compose.yml
    ├── manage.py
    ├── mysite
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── pyproject.toml
    ├── requirements.in
    └── requirements.txt
    ```

 1. Create you main django app:

    ```bash
    python manage.py startapp main
    ```

    `main` is our recommended name for the app, but you can call it whatever you want. If you change the name, make sure you change the lines referencing `main/migrations` in `pyproject.toml` and `.flake8` to `<your-app-name>/migrations`.

    You should now have a new sub-directory called `main` with this structure:

    ```
    main
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── migrations
    │   └── __init__.py
    ├── models.py
    ├── tests.py
    └── views.py
    ```

 1. Ensure this repo is tracked by git with `git init` and to update this README to match your project.

If you want to specify a python version for your Docker container, change the first line of the Dockerfile to your preferred image.

The project is now ready to build and run in the docker container using `docker-compose build` and `docker-compose run -d`.
