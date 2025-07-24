from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from passlib.context import CryptContext  # type: ignore
from jose import JWTError, jwt  # type: ignore
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer
from typing import Optional
import re
import os
import time

# === Config ===
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@db:5432/app")
SECRET_KEY = "secretkeyjwtdevonly"
ALGORITHM = "HS256"
EMAIL_REGEX = r"[^@]+@[^@]+\.[^@]+"

# === App init ===
app = FastAPI()

# === CORS ===
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# === DB setup ===
Base = declarative_base()
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)

# === Password hashing ===
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# === Auth ===
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def create_access_token(data: dict):
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token non valido",
            headers={"WWW-Authenticate": "Bearer"},
        )

# === User model ===
class User(Base): # type: ignore
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)
    role: Mapped[str] = mapped_column(String, default="user", nullable=False)

# === Crea le tabelle quando il DB è pronto ===
for _ in range(10):
    try:
        Base.metadata.create_all(bind=engine)
        break
    except Exception:
        print("⏳ Waiting for DB...")
        time.sleep(2)

# === Endpoints ===

@app.get("/")
def root():
    return {"message": "Benvenuto in ZeroDevBox API"}

@app.get("/users")
def get_users():
    session = SessionLocal()
    users = session.query(User).all()
    return [{"id": u.id, "name": u.name, "email": u.email, "role": u.role} for u in users]

@app.post("/add_user")
def add_user(user: dict):
    session = SessionLocal()
    if not re.match(EMAIL_REGEX, user["email"]):
        raise HTTPException(status_code=400, detail="Email non valida")
    if session.query(User).filter(User.email == user["email"]).first():
        raise HTTPException(status_code=409, detail="Email già registrata")
    hashed = pwd_context.hash(user["password"])
    new_user = User(
        name=user["name"],
        email=user["email"],
        password=hashed,
        role=user.get("role", "user")
    )
    session.add(new_user)
    session.commit()
    return {"message": f"Utente {user['name']} aggiunto"}

@app.delete("/delete_user/{user_id}")
def delete_user(user_id: int):
    session = SessionLocal()
    user = session.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Utente non trovato")
    session.delete(user)
    session.commit()
    return {"message": f"Utente {user.name} eliminato"}

@app.put("/update_user/{user_id}")
def update_user(user_id: int, user_data: dict):
    session = SessionLocal()
    user = session.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Utente non trovato")
    if "name" in user_data:
        user.name = user_data["name"]
    if "email" in user_data:
        if not re.match(EMAIL_REGEX, user_data["email"]):
            raise HTTPException(status_code=400, detail="Email non valida")
        user.email = user_data["email"]
    if "role" in user_data:
        user.role = user_data["role"]
    session.commit()
    return {"message": f"Utente {user.name} aggiornato"}

@app.post("/login")
def login(user: dict):
    session = SessionLocal()
    db_user = session.query(User).filter(User.email == user["email"]).first()
    if not db_user or not pwd_context.verify(user["password"], db_user.password):
        raise HTTPException(status_code=400, detail="Credenziali errate")
    token = create_access_token({
        "sub": db_user.name,
        "email": db_user.email,
        "role": db_user.role
    })
    return {"access_token": token, "token_type": "bearer"}

@app.get("/protected")
def protected_route(current_user: dict = Depends(verify_token)):
    return {"message": "Accesso autorizzato", "user": current_user}

@app.get("/dashboard")
def get_dashboard(current_user: dict = Depends(verify_token)):
    if current_user.get("role") != "admin":
        raise HTTPException(status_code=403, detail="Accesso riservato agli admin")
    return {"message": f"Benvenuto nella dashboard, {current_user['sub']}"}
