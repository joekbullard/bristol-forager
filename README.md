# GeoDjango Docker Template
> A Docker Django project template built upon osgeo/gdal ubuntu image and using PostGIS extension for PostgreSQL to enable geospatial applications. It includes a generic user auth model with email login. To be used as the base for a development environment for geospatial django applications.

## Requirements
* Docker
* Docker-compose

## Usage
`docker-compose up -d --build`

This will build the ubuntu osgeo/gdal image using `app/Dockerfile.dev` and install relevant requriements.

Inspect the `.env.dev` and `.env.dev.db` files for relevant environmental variables for app and database.

The project is set up to automatically `makemigrations`, `migrate` and `runserver` on the default port of 8000.

## Todo
Currently uses psycopg2-binary, this is a development environment template only and not fit for production. When required, should instead be adjusted to use psycopg2, this will require adjusting the `Dockerfile.dev` to include psycopg2 prerequisites.

Implement django-rest-framework and django-rest-framework-gis

Consider swapping to alpine-small for production