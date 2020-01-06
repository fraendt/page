from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def index():
  return redirect("https://joshwang.me/r/", code=302)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
