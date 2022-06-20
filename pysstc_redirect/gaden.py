#!/usr/bin/python3
# Author @nu11secur1ty

from flask import Flask,redirect
print("the domain which you want to fake\n")
# Microsoft sucks!
print("For example: https://microsoft.com/")
person = input('domain? ')

truti = Flask(__name__)
@truti.route('/')
def hello():
    return redirect(person, code=302)

print("Your IP please")
ip = input('the IP?')

if __name__ == '__main__':
    truti.run(host=ip, port=80)
