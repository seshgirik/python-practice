from flask import Flask, request, jsonify
import os
app = Flask(__name__)

# READING
@app.route("/", methods=["GET"])
def testAPI():
    return("This is sample Flask document root method.")

# READING
@app.route("/testpawan", methods=["GET"])
def testAPI02():
    return("Hi Pawan.")

# WRITING
@app.route("/readFile", methods=["POST"])
def readFile():
    response = jsonify({"execution_msg": "Some error."})
    # print("I am in my method.", request)
    # print("type(request) ::", type(request))
    # print("dir(request) ::", dir(request))
    file_name = request.json["fileName"]
    # print("file_name ::", file_name)
    file_data, msg  = readFileContent(file_name)
    if file_data:
        d = {"file_content": file_data, "execution_msg": msg}
        response = jsonify(d)
        response.status_code = 200
    else:
        d = {"file_content": file_data, "execution_msg": msg}
        response = jsonify(d)
        response.status_code = 404
    return response

def readFileContent(file_name):
    data = None
    msg = ""
    if (os.path.isfile(file_name)):
        with open(file_name) as fh:
            data = fh.read()
    else:
        msg = "File {} does not exist.".format(file_name)
    return data, msg

if __name__ == "__main__":
    #print(dir(app))
    app.run()