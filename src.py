from flask import Flask, request, Response
import numpy as np
import cv2
import pytesseract
import os
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

app = Flask(__name__)

fileName = "image.jpg"

# change the "/api/test" to the end point that you want to send the request to
@app.route('/api/test', methods=['POST'])
def test():
    r = request
    nparr = np.frombuffer(r.data, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    try:
        os.remove(fileName)
    except:
        pass

    cv2.imwrite(fileName, img)

    text = pytesseract.image_to_string(Image.open(fileName))[0:-2]


    print(text)

    return Response(response="hi", status=200)


# change the ip address to your pc ip address
app.run(host="192.168.5.194", port=5000)