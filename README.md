# 💼 Django Portfolio Tracker

Track your investments in real-time with a simple Django web application using live data from Yahoo Finance (`yfinance`).

---

## 🔧 Features

- Add, view, and delete investments
- Real-time stock/crypto prices
- Profit shown in dollars and percentages
- Admin panel for easier management
- Auto-refreshes every 10 seconds

---

## 📦 Installation

1. Clone this repository:

```bash
git clone https://github.com/ErayBahar/django-portfolio-app.git
cd django-portfolio-app
```

2. Set up the project:

```bash
# (Optional) Create a virtual environment
python -m venv venv
venv\Scripts\activate       # Windows
# source venv/bin/activate  # macOS/Linux

# Install all required dependencies
pip install -r requirements.txt

# Run database migrations
python manage.py migrate

# Create superuser for admin access
python manage.py createsuperuser

# Start the development server
python manage.py runserver
```

Visit your app at:  
http://127.0.0.1:8000/

---

## 🔐 Admin Access

Access the admin panel at:  
http://127.0.0.1:8000/admin

---

## 📁 Project Structure

```
myPortfolioApp/
├── manage.py
├── db.sqlite3
├── requirements.txt
├── portfolio/
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── templates/
│       └── portfolio/
│           ├── portfolio_list.html
│           ├── add_investment.html
│           └── delete_investment.html
└── static/  # Optional for CSS/JS
```

---

## 💡 Notes

- Make sure you're connected to the internet. The app pulls live stock/crypto prices using `yfinance`.
- Use valid Yahoo Finance symbols like `AAPL`, `GOOGL`, `BTC-USD`, etc.

---

## 🧠 Author

Created by Eray Bahar  
GitHub: [https://github.com/ErayBahar](https://github.com/ErayBahar)