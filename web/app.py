from flask import Flask, request
import cvlib as cv
from cvlib.object_detection import draw_bbox
import sys
import cv2
app = Flask(__name__)

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

    if 'person' in label:
        return 'person detected'

    return 'no person detected'


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')