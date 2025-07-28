# ZeroDevBox – Full-Stack Development Environment (React + FastAPI + PostgreSQL)

ZeroDevBox provides a complete **full-stack development environment** using **React (Vite)** for the frontend, **FastAPI** for the backend, and **PostgreSQL** as the database, fully containerized with **Docker**. Designed for local development and GitHub Codespaces.

---

## 🚀 Features

* ✅ **Frontend**: React + Vite (development mode with hot reload)
* ✅ **Backend**: FastAPI with REST API support and Swagger UI
* ✅ **Database**: PostgreSQL with persistent storage
* ✅ **Dockerized Architecture**: One-command setup using Docker Compose
* ✅ **API Documentation**: Integrated Swagger UI
* ✅ Works seamlessly with **Docker Desktop**, **Codespaces**, and **DevPod**

---

## 🧰 Requirements

* [Docker](https://www.docker.com/)
* [Docker Compose](https://docs.docker.com/compose/)
* [Git](https://git-scm.com/)

---

## 🛠️ Setup & Run

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/ZeroDevBox.git
cd ZeroDevBox
```

### 2. Start the environment in development mode

```bash
docker-compose down --volumes --remove-orphans
docker-compose build --no-cache
docker-compose up -d
```

### 3. Stop the containers

```bash
docker-compose down
```

---

## 🌐 Available Services

| Service      | URL                                                              |
| ------------ | ---------------------------------------------------------------- |
| **Frontend** | [http://localhost:5173](http://localhost:5173)                   |
| **Backend**  | [http://localhost:8000](http://localhost:8000)                   |
| **Swagger**  | [http://localhost:8000/docs](http://localhost:8000/docs)         |
| **Database** | `localhost:5432` (user: `user`, password: `password`, db: `app`) |

---

## 🔐 Authentication (Future Features)

* JWT Authentication with access and refresh tokens
* Role-based access control (user / admin)
* Secure password hashing using bcrypt
* Admin dashboard for managing users and data

---

## 📋 Main API Endpoints (Planned)

| Method | Endpoint     | Description            |
| ------ | ------------ | ---------------------- |
| POST   | `/signup`    | Register a new user    |
| POST   | `/login`     | Login and receive JWT  |
| GET    | `/users`     | List all users (admin) |
| GET    | `/dashboard` | Admin-only access      |

Full interactive docs available at: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📂 Project Structure

```
ZeroDevBox/
├── frontend/         # React + Vite source code
│   ├── src/          # Frontend components and pages
│   ├── Dockerfile    # Frontend container setup
│   └── package.json
│
├── backend/          # FastAPI backend app
│   ├── main.py       # API entry point
│   ├── requirements.txt
│   └── Dockerfile
│
├── docker-compose.yml
└── README.md
```

---

## 🔄 Useful Commands

### Start Development Environment

```bash
docker-compose up --build
```

### Stop Containers

```bash
docker-compose down
```

### Rebuild Everything

```bash
docker-compose build --no-cache
```

---

## 🧪 API Testing

Use Swagger UI for interactive API testing:

```
http://localhost:8000/docs
```

---

## 🔮 Future Enhancements

* ✅ GitHub Actions CI/CD pipeline
* ✅ Social Login (Google, GitHub)
* ✅ JWT refresh tokens & expiration handling
* ✅ File/Image upload support
* ✅ Advanced admin dashboard
* ✅ Deployment templates for Render/VPS

---

## ❤️ Contribute

* Fork this repository
* Create a new feature branch
* Submit a Pull Request
