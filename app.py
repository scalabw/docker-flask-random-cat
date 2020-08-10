from flask import Flask, render_template
from urllib.request import urlopen
import json
import os

app = Flask(__name__)


def random_gif():
    publicKey = "i9Nzs6H4rcjfpKtsO0dkI2TaoHp6bFp1"
    finalURL = "https://api.giphy.com/v1/gifs/random?api_key=" + \
        publicKey + "&tag=cat"

    data = json.loads(urlopen(finalURL).read().decode('utf-8'))
    return data["data"]["image_url"]


@app.route("/")
def index():
    return render_template("index.html", url=random_gif())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
