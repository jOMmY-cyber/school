FROM python:3.8.9-slim
# ENV PYTHONUNBUFFERED=1
WORKDIR /myproject
RUN pip install Django==3.1.5
# RUN pip install psycopg2==2.8.6
RUN pip install djangorestframework==3.12.4
RUN pip install Pillow==8.1.0
RUN pip install django-cors-headers==3.7.0


# FROM imaginaz/vpms-env:v2 # fail due to arch arm

# RUN apt-get update \
#     && apt-get install -y --no-install-recommends \
#         postgresql-client \
#     && rm -rf /var/lib/apt/lists/*


COPY . /myproject/
RUN python manage.py makemigrations
RUN python manage.py migrate

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]