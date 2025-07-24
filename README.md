# ⚡ ZeroDevBox – One-Click Full-Stack Development Environment

ZeroDevBox is a complete template to quickly spin up a **full-stack development environment** using **React (Vite)**, **FastAPI**, and **PostgreSQL**, fully containerized with **Docker** and ready for **GitHub Codespaces**.

---

## 🚀 Features
- ✅ **Frontend:** React (Vite)
- ✅ **Backend:** FastAPI with JWT Authentication
- ✅ **Database:** PostgreSQL with persistent volume
- ✅ Secure login with bcrypt-hashed passwords
- ✅ Role-based access control (user / admin)
- ✅ Admin-only dashboard
- ✅ API documentation via Swagger
- ✅ One-command setup (`docker-compose up --build`)
- ✅ Works with Docker Desktop, Codespaces, DevPod

---

## 🧰 Requirements
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Git](https://git-scm.com/)

---

## 🛠️ Setup & Run

### 1️⃣ Clone the repository
```bash
git clone https://github.com/YOUR-USERNAME/ZeroDevBox.git
cd ZeroDevBox
```

### 2️⃣ Start the environment
- **Linux/Mac**
```bash
make start
```
- **Windows PowerShell**
```bash
docker-compose up --build
```

### 3️⃣ Stop the containers
```bash
docker-compose down
```

---

## 🌐 Available Services
| Service     | URL                                  |
|-------------|--------------------------------------|
| Frontend    | [http://localhost:3000](http://localhost:3000) |
| Backend API | [http://localhost:8000](http://localhost:8000) |
| Swagger Docs| [http://localhost:8000/docs](http://localhost:8000/docs) |
| PostgreSQL  | `localhost:5432` (user: `user`, password: `password`, db: `app`) |

---

## 🔐 Authentication
- Register and login using **JWT tokens**
- Token stored in `localStorage`
- Roles:
  - `user` → basic access
  - `admin` → dashboard access

---

## 📋 Main API Endpoints
| Method | Endpoint             | Description                |
|--------|----------------------|---------------------------|
| POST   | `/signup`           | Register new user        |
| POST   | `/login`            | Login and receive JWT    |
| GET    | `/users`            | List users (protected)   |
| PUT    | `/update_user/{id}` | Update user data         |
| DELETE | `/delete_user/{id}` | Delete user              |
| GET    | `/dashboard`        | Admin-only access        |

Full API Docs: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📂 Project Structure
```
ZeroDevBox/
├── frontend/         # React + Vite
│   ├── src/          # Frontend source code
│   ├── Dockerfile    # Frontend container
│   └── package.json
│
├── backend/          # FastAPI app
│   ├── main.py       # API logic
│   ├── requirements.txt
│   └── Dockerfile
│
├── docker-compose.yml
├── Makefile
└── README.md
```

---

## 🔄 Useful Commands
- Start:  
```bash
make start
```
or  
```bash
docker-compose up --build
```

- Stop:  
```bash
docker-compose down
```

- Rebuild:  
```bash
make rebuild
```

---

## 🧪 API Testing
Swagger UI:  
[http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🔮 Future Improvements
- ✅ GitHub Actions CI/CD pipeline
- ✅ Social Login (Google, GitHub)
- ✅ JWT refresh tokens & expiry
- ✅ File/image upload
- ✅ Advanced admin panel
- ✅ Auto deploy to Render / VPS

---

## ❤️ Contribute
- Fork this repository
- Create a new branch: `feature-name`
- Submit a Pull Request
