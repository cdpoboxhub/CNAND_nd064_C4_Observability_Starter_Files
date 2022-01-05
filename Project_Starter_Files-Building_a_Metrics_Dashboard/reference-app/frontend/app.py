from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("main.html")

@app.route('/healthz')
def healthcheck():
    app.logger.info('Status request successfull')
    return jsonify({"result": "OK - healthy"})


if __name__ == "__main__":
    app.run()
