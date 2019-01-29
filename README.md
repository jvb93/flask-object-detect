# Flask Object Detection MicroService

### What is it? 

This is a proof of concept application that uses computer vision to detect people in a photo. If a person is detected, a discord webhook is notified.

This flask-based microservice relies on [cvlib](https://www.cvlib.net/) to detect 80 different objects.

The current motiviation for this project is to detect humans in security camera frames and send notifications accordingly.

### Prerequisites
 - Docker
 - A discord webhook URL to post alerts to
 - Some jpg's

### How to run

#### Docker command
    docker run -d \
    -e WEBHOOK_URL= {Your discord webhook url} \
    -p 5000:5000 \
    jvb1993/flask-object-detect

### Using the service

Make an http post request to http://{thecontainer:port}/detect

Attach a photo as form data 

(wait a moment as computer vision is pretty slow right now, especially on larger files)

If a person is detected, your webhook URL will be called with the photo attached

#### Example cURL call

```
curl -X POST \
  http://localhost:5000/detect \
  -H 'cache-control: no-cache' \
  -H 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' \
  -F 'file=@{path to your jpg file}'
```
