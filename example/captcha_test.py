from flask import Flask, render_template, request, session
from captcha import Captcha
from os import remove


app = Flask(__name__)
app.config['SECRET_KEY'] = "a really really really really long secret key"


@app.route("/captcha", methods=["GET", "POST"])
def main():
    if request.method == "GET":
        try:
            remove(f"static/img/{session['captcha']}.png")
        except:
            pass
        captcha_generation = Captcha([600, 200]).create_captcha(font_size=120, count=5)
        session["captcha"] = captcha_generation[0]
        return render_template("index.html", captcha=captcha_generation)
    elif request.method == "POST":
        captcha_generation = Captcha([600, 200]).create_captcha(font_size=120, count=5)
        if request.form["captcha_value"] == session["captcha"]:
            try:
                remove(f"static/img/{session['captcha']}.png")
            except:
                pass
            session["captcha"] = captcha_generation[0]
            return render_template("index.html", captcha=captcha_generation, status=True)
        else:
            try:
                remove(f"static/img/{session['captcha']}.png")
            except:
                pass
            session["captcha"] = captcha_generation[0]
            return render_template("index.html", captcha=captcha_generation, status=False)


app.run(port=80, debug=True)
