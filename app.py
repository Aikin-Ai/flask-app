import random

from flask import Flask, render_template

app = Flask(__name__)

# list of cat images
images = [
    "https://i.imgur.com/jfYnWiO.jpg",
    "https://i.imgur.com/ffwY6XJ.jpg",
    "https://i.imgur.com/dPeSlWF.jpg",
    "https://i.imgur.com/hqmy5In.jpg",
    "https://i.imgur.com/tGcZJtj.jpg",
    "https://i.imgur.com/G9m4HAX.jpg",
    "https://i.imgur.com/O4QfPOm.jpg"
]
@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
