# flask-findip

## About

This service will push the calling services external IPv4 address to the localhost of this service. This allows the external IP address of the calling service to be published without using the services of a third party site like WhatsMyIP.com or alike.

## Details
Written in Python 3.8.1 and using Flask to contain the web app.

## Requirements
If running this locally the following requirements are assumed:

- Python 3.8.1
- Flask
- IPGetter2

## Running
Run the following command from the directory of the application

`python app.py`

## Dockerfile
now available ina self contained dockerfile through DockerHub using the following command:

```
docker run -dit -p 8080:8080 screamingjoypad/flask-ipfinder
```
