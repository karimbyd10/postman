# 🍔 Food Ordering Web Application

## 📌 Project Overview

The **Food Ordering Web Application** is a web-based system built using the Django framework that allows users to browse a restaurant menu and place orders online. The application provides a modern and simple interface where customers can explore food items, add them to a cart, and complete an order.

The system also includes an **admin management panel** where restaurant administrators can manage menu items, categories, and customer orders.

---

# 🚀 Features

### Customer Features

* Browse restaurant menu
* View detailed food information
* Search foods
* Filter foods by category
* Add items to cart
* Place food orders
* Responsive design (mobile and desktop)

### Admin Features

* Add new food items
* Update food information
* Delete food items
* Manage food categories
* View customer orders

---

# 🛠️ Technologies Used

* **Backend:** Django (Python)
* **Frontend:** HTML, , Bootstrap
* **Database:** SQL
* **Version Control:** Git & GitHub
* **Image Handling:** Pillow

---

# 🗄️ Database Schema Design (ERD)

The application database consists of the following main entities:

* Users
* Categories
* Food
* Orders
* OrderItems

## Entity Relationship Overview

User
│
│ 1
│
│ N
Order
│
│ 1
│
│ N
OrderItem
│
│ N
│
│ 1
Food
│
│ N
│
│ 1
Category

---

## Tables Description

### Users

Stores registered user accounts.

| Field    | Type         | Description        |
| -------- | ------------ | ------------------ |
| id       | Integer (PK) | Unique user ID     |
| username | VARCHAR      | Username           |
| email    | VARCHAR      | Email address      |
| password | VARCHAR      | Encrypted password |

---

### Category

Stores food categories.

| Field | Type         |
| ----- | ------------ |
| id    | Integer (PK) |
| name  | VARCHAR(100) |

Relationship:

* One category can contain multiple food items.

---

### Food

Stores all menu items.

| Field       | Type         |
| ----------- | ------------ |
| id          | Integer (PK) |
| name        | VARCHAR(200) |
| description | TEXT         |
| price       | DECIMAL      |
| image       | VARCHAR      |
| available   | BOOLEAN      |
| category_id | FK           |

Relationship:

* One food belongs to one category.

---

### Order

Stores customer orders.

| Field         | Type         |
| ------------- | ------------ |
| id            | Integer (PK) |
| customer_name | VARCHAR      |
| phone         | VARCHAR      |
| address       | TEXT         |
| created_at    | DATETIME     |
| user_id       | FK           |

Relationship:

* One order can contain many items.

---

### OrderItem

Represents items inside an order.

| Field    | Type         |
| -------- | ------------ |
| id       | Integer (PK) |
| order_id | FK           |
| food_id  | FK           |
| quantity | INTEGER      |

Relationship:

* Connects **orders and foods (many-to-many)**.

---

# 🔗 API Endpoints

The backend exposes several API endpoints to manage menu items, orders, and users.

---

## Authentication Endpoints

### Register User

POST /api/register

Creates a new user account.

Example request:

```json
{
  "username": "john123",
  "email": "john@email.com",
  "password": "password123"
}
```

---

### Login User

POST /api/login

Authenticates a user and returns an authentication token.

Example response:

```json
{
  "token": "user-authentication-token"
}
```

---

# 📂 Category API

### Get All Categories

GET /api/categories

Returns a list of available categories.

---

### Create Category (Admin)

POST /api/categories

Creates a new food category.

---

# 🍕 Food Menu API

### Get All Foods

GET /api/foods

Returns all food items.

Optional filters:

GET /api/foods?category=2
GET /api/foods?search=pizza

---

### Get Food Details

GET /api/foods/{id}

Returns detailed information about a food item.

---

### Create Food (Admin)

POST /api/foods

Adds a new food item.

---

### Update Food (Admin)

PUT /api/foods/{id}

Updates food details.

---

### Delete Food (Admin)

DELETE /api/foods/{id}

Removes food from the menu.

---

# 🛒 Cart API

### View Cart

GET /api/cart

Returns items currently in the user's cart.

---

### Add Item to Cart

POST /api/cart

Example request:

```json
{
  "food_id": 3,
  "quantity": 2
}
```

---

### Remove Item From Cart

DELETE /api/cart/{food_id}

Removes an item from the cart.

---

# 📦 Order API

### Create Order

POST /api/orders

Creates a new order from cart items.

Example request:

```json
{
  "customer_name": "John",
  "phone": "123456789",
  "address": "123 Main Street"
}
```

---

### Get All Orders (Admin)

GET /api/orders

Returns all orders in the system.

---

### Get Order Details

GET /api/orders/{id}

Returns information about a specific order.

---

# ⚙️ Installation Guide

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/food-ordering-app.git
cd food-ordering-app
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

Windows:

```bash
venv\Scripts\activat
```

---

### 3. Install Dependencies

```bash
pip install django pillow
```

---

### 4. Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 5. Create Admin User

```bash
python manage.py createsuperuser
```

---

### 6. Run the Development Server

```bash
python manage.py runserver
```

Open browser:

http://127.0.0.1:8000

Admin panel:

http://127.0.0.1:8000/admin

---

# 📅 Project Timeline

### Week 1

Project setup and database design.

### Week 2

Menu system and food detail pages.

### Week 3

Cart and ordering system.

### Week 4

Testing, UI improvements, and documentation.

---

# 📌 Future Improvements

* Payment integration
* Order tracking system
* Food ratings and reviews
* Real-time notifications
* Mobile application support

---

# 👨‍💻 Author

Food Ordering Application Project
Built using **Django Web Framework**
