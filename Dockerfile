FROM docker.oa.com:8080/public/python:3.6
RUN pip install django
COPY gaiastack /gaiastack
WORKDIR /gaiastack
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
