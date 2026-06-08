# horse-app
# 🐴 Horse App

A beautiful web application built with Python Flask and Bootstrap 4 that allows users to contact the Horse App team directly through a contact form that sends real emails using Gmail SMTP.

---

## 🌟 Features

- 🏠 Beautiful home page with a horse background image
- 📱 Fully responsive design for mobile, tablet, and desktop
- 📬 Contact form that sends real emails
- ✅ Success page after sending a message
- 🎨 Clean and modern UI with Bootstrap 4
- 🔗 Smooth navbar navigation
- 📲 App Store and Google Play download buttons

---

## 🖥️ Tech Stack

| Technology | Purpose |
|---|---|
| Python 3 | Backend language |
| Flask | Web framework |
| Bootstrap 4 | CSS framework |
| HTML5 | Structure |
| CSS3 | Styling |
| smtplib | Email sending |
| Gmail SMTP | Email service |

---

## 📁 Project Structure

```
horse-app/
├── main.py
├── static/
│   └── style.css
└── templates/
    ├── index.html
    ├── contact.html
    └── success.html
```

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/horse-app.git
cd horse-app
```

### 2. Install Flask
```bash
pip install flask
```

### 3. Setup your Gmail
- Go to myaccount.google.com
- Turn on 2-Step Verification
- Go to App Passwords
- Create a new app password
- Copy the 16 letter password

### 4. Add your email to main.py
```python
MY_EMAIL = "youremail@gmail.com"
MY_PASSWORD = "your16letterpassword"
```

### 5. Run the app
```bash
python3 main.py
```

### 6. Open in browser
```
http://127.0.0.1:5000
```

---

## 📸 Pages

### 🏠 Home Page
- Beautiful horse background image
- Welcome message
- Contact Us button
- Download App buttons

### 📬 Contact Page
- Name field
- Email field
- Phone field
- Message field
- Send button

### ✅ Success Page
- Confirmation message
- Go back home button

---

## 📱 Responsive Design

| Device | Size | Status |
|---|---|---|
| Desktop | 1200px+ | ✅ |
| Tablet | 768px - 1199px | ✅ |
| Mobile | 320px - 767px | ✅ |

---

## 🔒 Security Notes

- Never push your real email or password to GitHub
- Always use Gmail App Password not your real password
- Keep your credentials in a .env file for production

---

## 🚀 How It Works

```
User opens website
        ↓
User clicks Contact
        ↓
User fills the form
        ↓
User clicks Send
        ↓
Flask sends email via Gmail SMTP
        ↓
Success page shows ✅
```

---

## 👨‍💻 Author

- GitHub: [@yourusername](https://github.com/yourusername)
- Project: [horse-app](https://github.com/yourusername/horse-app)

---

## 📚 What I Learned

- How to build a Flask web application
- How to use HTML forms with POST method
- How to send emails with Python smtplib
- How to use Bootstrap 4 for responsive design
- How to organize Flask project with static and templates folders
- How to use Gmail SMTP for sending emails

---

## 📄 License

This project is open source and available under the MIT License.

---

## 🙏 Credits

- Course: 100 Days of Code - The Complete Python Bootcamp
- Teacher: Angela Yu
- Horse Image: Unsplash
- Icons: Bootstrap 4
