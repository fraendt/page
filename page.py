from flask import Flask, redirect, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('page.html')
  return redirect("https://joshwang.me/r/pe", code=302)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
