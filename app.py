import json

from flask import Flask, Response

from logic import recommend

app = Flask(__name__)


@app.route("/")
def index():
    v = recommend()
    return Response(json.loads(v), content_type='application/json')


if __name__ == '__main__':
    app.run()
