# 🛠️ Admin-User Management System – FastAPI Project

A secure and modern **Admin-User Management Web Application** built using **FastAPI**, **JWT Authentication**, **PostgreSQL**, and deployed live on **Render**.

Admins can sign in, create new users/admins, and manage all user data. Users can sign up, log in, and view their personal dashboards.

---

## 🌐 Live Demo

🔗 **Try it here**: [https://priyansh-lk90.onrender.com/](https://priyansh-lk90.onrender.com/)  
👀 Or visit a short URL: [https://rebrand.ly/iq9r4mr](https://rebrand.ly/iq9r4mr)

---

## 🚀 Features

- 🔐 **JWT Authentication** for secure login/signup
- 👥 **Role-based access** (Admin vs User)
- 📋 Admin dashboard: View & delete users
- ➕ Admin can create new users/admins
- 🧠 Password hashing with bcrypt
- 💡 Responsive UI using **HTML**, **CSS**, **Jinja2**, and **Vanilla JS**
- 🧱 PostgreSQL database with **SQLAlchemy ORM**
- 🔄 **Alembic** migrations for DB versioning
- ☁️ Deployed on **Render**
- 🌿 `.env` support via `python-dotenv`

---

# Project Screenshots
![alt text](<project-images/Screenshot (242).png>) ![alt text](<project-images/Screenshot (241).png>) ![alt text](<project-images/Screenshot (240).png>) ![alt text](<project-images/Screenshot (239).png>) ![alt text](<project-images/Screenshot (238).png>) ![alt text](<project-images/Screenshot (237).png>) ![alt text](<project-images/Screenshot (236).png>) ![alt text](<project-images/Screenshot (235).png>) ![alt text](<project-images/Screenshot (234).png>) ![alt text](<project-images/Screenshot (233).png>)



## 🧰 Tech Stack

| Layer           | Tech                          |
|----------------|-------------------------------|
| Backend         | FastAPI, SQLAlchemy, Uvicorn |
| Database        | PostgreSQL (via Neon)        |
| Auth            | JWT + OAuth2PasswordBearer   |
| Migrations      | Alembic                       |
| Frontend        | HTML, CSS, Jinja2, JS         |
| Deployment      | Render Cloud Platform         |

---

## 📁 Project Structure

```
Project
│   .env
│   .env.example
│   alembic.ini
│   requirements.txt
│   start.sh
│   
├───alembic
│   │   env.py
│   │   README
│   │   script.py.mako
│   │
│   ├───versions
│
└───app
    │   main.py
    ├───auth
    │   │   dependency.py
    │   │   hash.py
    │   │   jwt.py
    ├───database
    │   │   db.py
    ├───models
    │   │   admin_model.py
    │   │   user_model.py
    │   │   __init__.py
    ├───routers
    │   │   admin_routes.py
    │   │   page_routes.py
    │   │   user_routes.py
    ├───schemas
    │   │   admin_schema.py
    │   │   user_schema.py
    ├───static
    │   └───css
    │           style.css
    │
    ├───templates
    │       admin.html
    │       AdminCreates.html
    │       adminDashboard.html
    │       adminLogin.html
    │       adminSignup.html
    │       base.html
    │       dashboard.html
    │       index.html
    │       login.html
    │       signup.html
    │
    ├───utils
    ├───__init__.py
```


---

## ⚙️ Setup Instructions

1. **Clone the repo**  
   ```bash
   git clone https://github.com/your-username/fastapi-admin-app.git
   cd fastapi-admin-app
    ```
2. **Create virtual environment**
    ```
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

    ```
3. **Install dependencies**
    ```
    pip install -r requirements.txt

    ```
4. **Setup .env**
    ```
    DB_URL=your_postgres_connection_url
    SECRET_KEY=your_jwt_secret
    ALGORITHM=HS256
    ACCESS_TOKEN_EXPIRE_MINUTES=30

    ```
5. **Run migrations**

    ```
    alembic upgrade head
    ```
6. **Start the app**
    ```
    uvicorn app.main:app --reload
    ```

# 🚀 Deployment on Render
- App is deployed using:

- start.sh script

- requirements.txt

- Build command: ./start.sh

- Note: Use Render's environment variable panel to securely provide your .env values.



---



# ✍️ Author
## Priyansh Verma

## 📇 Contact & Info

**👨‍💻 LinkedIn**: [priyanshv](https://www.linkedin.com/in/priyanshv/)  
📧 **Email**: [priyanshverma157@gmail.com](mailto:priyanshverma157@gmail.com)  
💻 **GitHub**: [priyanshgitthat](https://github.com/priyanshgitthat)  
🌐 **Portfolio**: [Priyansh Verma](https:priyanshverma.netlify.app) 




# 📣 Let's Connect!
#####  If you liked this project, feel free to star ⭐️ the repo and connect with me on LinkedIn,or Email for more updates on backend development & projects!

