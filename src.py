from flask import Flask, request, Response
import numpy as np
import cv2
import pytesseract
import os
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

app = Flask(__name__)

fileName = "image.jpg"

@app.route('/')
@app.route('/index', methods=['GET'])
def index():
	return "ESP32-CAM Flask Server", 200


@app.route('/upload', methods=['POST','GET'])
def upload():
    received = request
    img = None
    if received.files:
        print(received.files['imageFile'])
        file  = received.files['imageFile']
        nparr = np.fromstring(file.read(), np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        try:
            os.remove(fileName)
        except:
            pass
        cv2.imwrite(fileName, img)	
        text = pytesseract.image_to_string(Image.open(fileName))[0:-2]
        print(text)
        return "[SUCCESS] Image Received", 201
    else:
        return "[FAILED] Image Not Received", 204


# change the ip address to your pc ip address
app.run(host="192.168.5.194", port=5000)