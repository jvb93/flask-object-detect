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

#### Required Parameters
  - **WEBHOOK_URL**: A discord webhook url
  - **OD_THRESHOLD**: 0-1 value - percentage of certainty that an object is in the photo to trigger a notificaiton. For example: .45 would mean the OD must be at least 45% confident an object exists to send a notification
  - **OBJECTS**: comma-delimited list of objects to look for; eg: "horse,person,car" - valid objects are listed [here](https://raw.githubusercontent.com/arunponnusamy/object-detection-opencv/master/yolov3.txt)

#### Docker command
    docker run -d \
    -e WEBHOOK_URL= {Your discord webhook url} \
    -e OD_THRESHOLD= {object detection threshold} \
    -e OBJECTS= {comma-seperated list of objects of interest} \
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
