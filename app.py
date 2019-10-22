from flask import Flask, render_template, flash, request, redirect, url_for
import Mods.calbot as calbot
from werkzeug.utils import secure_filename
import os, json, time

UPLOAD_FOLDER = "static/images/.."
ALLOWED_EXTENSIONS = set(['png', 'jpg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("index.html")

# Runs when text is sent.
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    #TODO: Query the bot for a response.
    # return userText
    return calbot.query(userText)

# Runs when an image is uploaded.
@app.route("/img")
def get_img_response():
    fileName = request.args.get("file")
    filePath = "static/images/" + fileName
    while not os.path.exists(filePath):
        time.sleep(0.5) 
    food = calbot.calculate(filePath)
    return str(json.dumps(food))

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            print("No file part.")
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            print("No selected file.")
            return redirect(request.url)

        # File upload is successful.
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            # Save the path into the specified folder.
            filePath = os.path.join(app.config['UPLOAD_FOLDER'], "images/" + filename)
            file.save(os.path.join(filePath))
            #TODO: Post the image as an upload.
            #TODO: Query the bot for a response.
            # Closes the new window it opens.
            return "<script>window.close()</script>"


if __name__ == "__main__":
    app.run(app.run(host="0.0.0.0"))
