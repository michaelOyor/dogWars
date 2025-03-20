from flask import Flask, render_template
import os

app = Flask(__name__)
imgFolder = os.path.join("static", "img")
app.config["UPLOAD_FOLDER"] = imgFolder

@app.route("/")
@app.route("/home")
def home():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'],'26th.jpg')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'], 'Balloons.jpg')
    pic3 = os.path.join(app.config['UPLOAD_FOLDER'], 'kpmg.jpg')
    return render_template('index.html',user_image=pic1,user_image2=pic2,user_image3=pic3)





if __name__ == '__main__':
    app.run(debug=True)