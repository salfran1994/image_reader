from flask import Flask, request, render_template, redirect, url_for
from PIL import Image
import pytesseract
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        file = request.files['photo']
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

        text = pytesseract.image_to_string(Image.open(filepath))
        return render_template('result.html', text=text)

    return render_template('upload.html')

if __name__ == '__main__':
    app.run()