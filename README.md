# Ecommerce Management System

A robust and scalable e-commerce platform built with Django. This system provides a seamless shopping experience for users, featuring product management, user authentication, and a streamlined checkout process.

## 🚀 Features

- **Product Browsing**: Dynamic product display with category filtering.
- **User Authentication**: Secure signup, login, and logout functionality.
- **Shopping Cart**: Real-time cart management for adding and managing items.
- **Checkout Process**: Integrated checkout system with order placement and tracking.
- **Contact Form**: Direct communication channel for user inquiries.
- **Order Updates**: Real-time tracking of order status updates.
- **Email Notifications**: Integrated SMTP for sending transactional emails (e.g., account activation).

## 🛠️ Tech Stack

- **Backend**: Python, Django
- **Database**: SQLite (default)
- **Frontend**: HTML, CSS (integrated with Django templates)
- **Tools**: GitHub CLI, Git

## 📥 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/samiur434/ecommerce_management.git
   cd ecommerce_management
   ```

2. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

3. **Create a superuser**:
   ```bash
   python manage.py createsuperuser
   ```

4. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

## 📂 Project Structure

- `ecapp/`: Main application logic, including product management and core views.
- `shopcart/`: Handles user authentication and shopping cart functionality.
- `ecommerce/`: Project settings and configuration.
- `static/`: Static files (CSS, Images, JS).
- `templates/`: HTML templates for the application.
- `media/`: User-uploaded media files.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.
