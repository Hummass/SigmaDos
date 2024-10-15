from flask import Flask, request, redirect
from flask import render_template

app = Flask (__name__)

@app.route('/')

def main():
	return render_template("sigma.html")


@app.route('/mission')

def mission():
	return render_templates("mission.html")
