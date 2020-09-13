import cv2
import io
import json
import numpy as np
import requests
img = cv2.imread('up.jpg')
height, width, _ = img.shape
#roi = img[0: height, 100:width]
#ocr
#'''
url_api = "https://api.ocr.space/parse/image"
_, compressedimage = cv2.imencode(".jpg", img, [1, 90])
file_bytes = io.BytesIO(compressedimage)
result = requests.post(url_api,
              files = {"screenshot.jpg": file_bytes},
              data = {"apikey": "d860f7c49e88957",
                      "language": "eng"})
result = result.content.decode()
#print(result.content.decode())

result = json.loads(result)
print(result)
text_detected = result.get("ParsedResults")[0].get("ParsedText")
print(text_detected)
#'''
print(img.shape)
cv2.imshow("output",img)
cv2.waitKey(0)