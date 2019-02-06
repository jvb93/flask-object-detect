from flask import Flask, request
import cvlib as cv
from cvlib.object_detection import draw_bbox
import sys
import cv2
import os
import json
from discord_webhook import DiscordWebhook, DiscordEmbed
app = Flask(__name__)

odThreshold = 0 
discord_webhook_url = ''
objectsOfInterest = [] 

@app.route('/')
def hello_world():
    return 'ok'

@app.route('/detect', methods = ['POST'])
def detect():
    app.logger.info('processing file')
    f = request.files['file']
    f.save(f.filename)
    app.logger.info(f)
    image = cv2.imread(f.filename)

    app.logger.info('detecting')
    # apply object detection
    bbox, label, conf = cv.detect_common_objects(image)
    zipped = zip(label, conf)

    detection = False
    detections = []
    toReturn = {}
    for label, conf in zipped:
        toReturn[label] = float(conf)
        if(label in objectsOfInterest and float(conf) >= odThreshold):
            detection = True
            detections.append((label, conf))
    if detection:       
        webhook = DiscordWebhook(url=discord_webhook_url, content="Object of Interest Detected!") 
        with open(f.filename, "rb") as fl:
            webhook.add_file(file=fl.read(), filename=f.filename)
        webhook.execute()
    
    return json.dumps(toReturn)


if __name__ == '__main__':
    discord_webhook_url = os.environ['WEBHOOK_URL']
    odThreshold = float(os.environ["OD_THRESHOLD"])
    objectsOfInterest = os.environ["OBJECTS"].lower().split(",")

    app.run(debug=True,host='0.0.0.0')
    