from flask import Blueprint, render_template, redirect, url_for, request
from website.code import vowel_ratio, atm_disp, triplet
import os

auth = Blueprint("auth",__name__)


@auth.route("/assn1")
def assn1():
    return render_template("assn1.html")


@auth.route("/assn2", methods=['GET','POST'])
def assn2():
    if request.method == "GET":
        return render_template("assn2.html")

    if request.method == "POST":
        text = request.form.get('string_val')

        if text == "":
            prompt = "Please enter valid text"
            return render_template("assn2.html", output = prompt)
            
        else:
            return render_template("assn2.html", output = vowel_ratio.word_check(text))


@auth.route("/assn3", methods=['GET','POST'])
def assn3():
    if request.method == "GET":
        return render_template("assn3.html")

    if request.method == 'POST':
        file_name = request.files['txt_file']
        
        if file_name.filename == "":
            prompt = "Please upload a file"
            return render_template("assn3.html", output = prompt)
    
        else:
            txt_string = file_name.read()
            txt_string = str(txt_string, 'utf-8')
            return render_template("assn3.html", output = vowel_ratio.word_check(txt_string))


@auth.route("/assn4", methods=['GET','POST'])
def assn4():
    if request.method == "GET":
        return render_template("assn4.html")
    if request.method == "POST":
        money = request.form.get('currency')

        if money == "":
            prompt = "Please enter a value before pressing submit"
            return render_template("assn4.html", output = prompt)
        else:
            return render_template("assn4.html", output = atm_disp.currency_sort(money))


@auth.route("/assn5", methods=['GET','POST'])
def assn5():
    if request.method == "GET":
        return render_template("assn5.html")

    if request.method == "POST":
        val = request.form.get('array_val')
        tar = request.form.get('target')

        if val == "" or tar == "":
            prompt = "Please make sure both values are entered"
            return render_template("assn5.html", output = prompt)
        else:
            return render_template("assn5.html", output = triplet.target_triplet(val, tar))


@auth.route("/")
@auth.route("/home")
def home():
    return render_template("home.html")

