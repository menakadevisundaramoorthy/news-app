# Heart care
The Heart care news app is a web application built with Python Django, designed to provide users with the latest health news articles. Users can browse through various health topics, read articles, and stay informed about recent developments in the health sector.

## Technologies Used
**Python**: Backend logic and server-side scripting are implemented using Python programming language.

**Django**: Django framework is used for building the web application, handling routing, views, models, and templates.

**HTML/CSS/JavaScript**: Frontend user interface is developed using HTML, CSS, and JavaScript for enhanced interactivity.

**Docker**: The project includes Docker support for containerized deployment.

## Installation
To run the Heart care App using Docker, follow these steps:

**Clone the repository**

```
git clone https://github.com/menakadevisundaramoorthy/news-app
```

**Navigate to the project directory**

```
cd news-app
```

Generate an API key from the site newsapi.org.

**Build the Docker image with the API key as argument to the docker build**

```
docker build -t heart-care --build-arg NEWS_API_KEY="<NEWS_API_KEY>" .
```

**Run the Docker container**

```
docker run -d -p 8000:8000 heart-care
```
