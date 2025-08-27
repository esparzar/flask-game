from flask import Flask, render_template, request
import random

app = Flask(__name__)
secret_number = random.randint(1, 20)

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    if request.method == "POST":
        guess = int(request.form.get("guess"))
        if guess < secret_number:
            message = "Too low! Try again."
        elif guess > secret_number:
            message = "Too high! Try again."
        else:
            message = "🎉 Correct! You guessed it!"
    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)