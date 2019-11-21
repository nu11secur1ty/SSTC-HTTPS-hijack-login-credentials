#!/usr/bin/python3
#
from flask import Flask,redirect
print("the domain whish you want to redirect")
redir = raw_input("Enter your name : ")

truti = Flask(__name__)
@truti.route('/')
def hello():
    return redirect("$redir", code=302)

if __name__ == '__main__':
    truti.run(host='0.0.0.0', port=80)
