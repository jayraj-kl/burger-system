# Burger Ordering System 🍔

A web-based burger ordering system built with Django that allows customers to browse burger menus, customize their orders with add-ons, and place orders online.

## Features

- **Interactive Menu**: Browse through various burgers with detailed descriptions, prices, ingredients and nutritional information
- **Add-on Selection**: Customize burgers with various add-ons and toppings
- **Order Management**: Add items to cart, review orders and submit with special instructions
- **Responsive Design**: Works on desktop and mobile devices
- **Order Tracking**: Monitor your order status after submission

## Tech Stack

- **Backend**: Django (Python web framework)
- **Database**: SQLite
- **Frontend**: HTML, CSS, JavaScript
- **AJAX**: For seamless order processing without page refreshes

## Project Structure

```
burger-system/
├── delivery/               # Main application
│   ├── models.py           # Database models for Burgers and Add-ons
│   ├── views.py            # View functions to render pages and process orders
│   ├── urls.py             # URL routing for the application
│   ├── templates/          # HTML templates for the UI
│   └── static/             # CSS and JavaScript files
├── food/                   # Project configuration
│   ├── settings.py         # Django settings
│   └── urls.py             # Project URL configuration
├── manage.py               # Django command-line utility
├── db.sqlite3              # SQLite database
└── requirements.txt        # Required Python packages
```

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/yourusername/burger-system.git
   cd burger-system
   ```

2. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

   Or if using pipenv:

   ```
   pipenv install
   ```

3. Run migrations:

   ```
   python manage.py migrate
   ```

4. Start the development server:

   ```
   python manage.py runserver
   ```

5. Open your browser and navigate to `http://localhost:8000/delivery/home/`

## Usage

1. Browse the menu of available burgers
2. Select burgers and customize with add-ons
3. Add items to your order
4. Review your order and add any special instructions
5. Submit your order and receive confirmation
