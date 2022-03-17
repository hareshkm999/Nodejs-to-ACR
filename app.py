from wsgiref import simple_server
from flask import Flask, request, render_template
from flask import Response

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    return {"data": "Application ran successfully - FastAPI"}


if __name__ == "__main__":
    host = '0.0.0.0'
    port = 8800
    httpd = simple_server.make_server(host, port, app)
    # print("Serving on %s %d" % (host, port))
    print("hi")
    httpd.serve_forever()