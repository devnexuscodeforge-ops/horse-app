from flask import Flask, render_template, request
import smtplib

app = Flask(__name__)

MY_EMAIL = "youremail@gmail.com"
MY_PASSWORD = "abcdefghijklmnop"

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/send', methods=["POST"])
def send():
    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]
    message = request.form["message"]

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
        )

    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True)
