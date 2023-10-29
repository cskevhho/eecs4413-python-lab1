from flask import Flask, render_template, request, session

app = Flask(__name__)

@app.route('/')
def hello():
    client_ip = request.remote_addr
    client_port = request.environ.get('REMOTE_PORT')
    client_protocol = request.scheme
    client_method = request.method
    query_string = request.query_string.decode('utf-8') # decodes query string
    query_param = request.args.get("foo")
    request_uri = request.url
    request_path = request.path
    app_nzame = app.name

    response_text = f"Client IP: {client_ip}\n"
    response_text += f"Client Port: {client_port}\n"

    if client_ip == "127.0.0.1":
        response_text += "This IP has been flagged!\n"

    response_text += f"Client Protocol: {client_protocol}\n"
    response_text += f"Client Method: {client_method}\n"
    response_text += f"Query String: {query_string}\n"
    response_text += f"Query Param: {query_param}\n"
    response_text += f"Request URI: {request_uri}\n"
    response_text += f"Request Path: {request_path}\n"
    response_text += f"Application Name: {app_name}"
    return render_template("index.html", response = response_text)