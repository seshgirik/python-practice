# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 10:07:53 2020

@author: skondaveti
"""

from flask import Flask
import os

app=Flask(__name__)

@app.route("/", methods=["GET"])

def testAPI():
    return "This is simple flask doc root method"


@app.route("/fileCreate",methods=["PUT"]) 

def createFile():
    file_name=request.json("fileName")
    file_data= readFileContent(file_name)  
    os.path


def DelFile():
    file_name=request.json("fileName")
    file_data= readFileContent(file_name)  
    os.path.exists


@app.route("/readFile",methods=["GET"])    

#def readFile():
#    file_name="date.py"
#    data=None
#    if(os.path.isfile(file_name)):
#        with open(file_name) as fh:
#            data=fh.read()
#            return data
#    else:
#        print("File {} does not exist".format(file_name))
#        
#jsonify

      
def readFile():
    file_name=request.json("fileName")
    file_data= readFileContent(file_name)
    

    
def readFileContent(file_name):
    data=None
    msg=""
    if (os.path.isfile(file_name)):
        with open(file_name) as fh:
            data=fh.read()

    else:
        msg="file not found"

        
        
if __name__ == "__main__":
    app.run()
    