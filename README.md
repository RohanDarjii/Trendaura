# 👗 Tendora – Clothing Brand Website (Django + Python)

Tendora is a full-stack e-commerce clothing website developed using Django. It offers a seamless online shopping experience with product browsing, cart management, coupon handling, and user authentication.

---

## 🚀 Features

### 🔐 User Authentication
- User registration, login, and logout
- Session-based authentication
- Secure password handling
- Email verification
- Profile image upload

### 🛍️ Product Management
- Add, edit, and delete products via Django admin
- Category management with image support
- Slug-based SEO-friendly URLs
- Multiple images per product (gallery view)

### 🎨 Product Variants and Pricing
- Size and color variant support
- Additional pricing per size/color
- Dynamic price calculation logic

### 🛒 Cart Functionality
- Add to cart with selected size, color, and quantity
- Real-time cart updates
- Remove items from cart
- Cart total calculation including variants and quantity

### 💸 Coupons and Discounts
- Apply coupons to eligible carts
- Minimum amount and expiration validation
- Dynamic discount application

### 💻 Frontend & UI
- Responsive design using HTML, CSS, and Bootstrap
- Mobile-friendly layout
- Clean product listings and detail views

### ⚙️ Admin Dashboard
- Django admin panel for managing:
  - Users
  - Products
  - Categories
  - Coupons
  - Orders

---

## 🛠️ Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: SQLite (can be switched to PostgreSQL or MySQL)
- **Image Uploads**: Django Media Files
- **Other Tools**: Django Messages, UUID, Slugify

---

## 📸 Screenshots

*Add screenshots of your home page, product page, cart, and checkout UI here*

---

## 🧰 Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/tendora.git
   cd tendora
````

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create a superuser:

   ```bash
   python manage.py createsuperuser
   ```

6. Start the server:

   ```bash
   python manage.py runserver
   ```

7. Visit `http://127.0.0.1:8000/` to use the app.

---

## 📂 Folder Structure

```
tendora/
├── accounts/
├── products/
├── templates/
├── static/
├── media/
├── db.sqlite3
└── manage.py
```

---

## 📃 License

This project is licensed under the MIT License.

---

## 🙋‍♂️ Contact

For any questions or contributions, feel free to open an issue or submit a pull request.

```

Let me know if you'd like this exported as a `.md` file or pushed to your GitHub repository.
```


