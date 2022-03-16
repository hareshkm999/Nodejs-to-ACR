from wsgiref import simple_server
from flask import Flask, request, render_template
from flask import Response

app = Flask(__name__)

@app.route("/train", methods=['GET', 'POST'])
#@cross_origin()
def trainRouteClient():
    return "hi"


if __name__ == "__main__":
    host = '0.0.0.0'
    port = 5000
    httpd = simple_server.make_server(host, port, app)
    # print("Serving on %s %d" % (host, port))
    print("hi")
    httpd.serve_forever()