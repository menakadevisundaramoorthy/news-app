FROM python:3.6

ARG api_key
ENV NEWS_API_KEY $api_key

COPY . /app
WORKDIR /app
RUN pip install Django
RUN pip install requests
RUN pip install whitenoise
EXPOSE 8000
ENTRYPOINT ["python"]
CMD ["manage.py", "runserver", "0.0.0.0:8000"]
