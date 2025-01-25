FROM python:3.6

ARG api_key="test"
ENV NEWS_API_KEY=$api_key

COPY . /app
WORKDIR /app

RUN pip install --no-cache-dir Django requests whitenoise

EXPOSE 8000
ENTRYPOINT ["python"]
CMD ["manage.py", "runserver", "0.0.0.0:8000"]
