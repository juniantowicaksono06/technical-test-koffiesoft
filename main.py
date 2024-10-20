from fastapi import FastAPI, Depends
from fastapi.responses import HTMLResponse, JSONResponse
from dotenv import load_dotenv
from pathlib import Path
from models.User import User
from config.database import SessionLocal, engine
from models.schemas import UserResponse, UserCreate, UserLogin
from utils import create_access_token, get_password_hash, verify_password, verify_jwt
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
import uuid
from middleware import IsAuthenticated
import os

load_dotenv()

oauth2_schema = OAuth2PasswordBearer(tokenUrl="token") # Inisialisasi OAuth2PasswordBearer

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

# Endpoint untuk registrasi
@app.post("/api/auth/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    hashed_password = get_password_hash(user.password)
    userid = uuid.uuid4()
    new_user = User(id=userid, name=user.name, username=user.username, password=hashed_password)
    db.add(new_user)
    try:
        db.commit()
        db.refresh(new_user)
    except IntegrityError:
        db.rollback()
        return JSONResponse(status_code=409, content={"message": "Username already registered"})
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500, content={"message": "Internal server error"})
    return new_user

# Endpoint untuk login
@app.post("/api/auth/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if not db_user or not verify_password(user.password, db_user.password):
        return JSONResponse(status_code=400, content={"message": "Invalid username or password"})
    access_token = create_access_token(data={"username": db_user.username, "name": db_user.name})  # Generate JWT token
    return {"access_token": access_token, "token_type": "bearer"}

# Endpoint untuk mengambil data Profile User
@app.get('/api/profile')
def profile(token: str = Depends(oauth2_schema)):
    payload = verify_jwt(token)
    return payload

@app.get('/register', response_class=HTMLResponse)
async def login_view():
    # Load the HTML content from a file
    html_file_path = Path("templates/register.html")
    html_content = html_file_path.read_text(encoding="utf-8")
    return HTMLResponse(content=html_content)

@app.get('/login', response_class=HTMLResponse)
async def login_view():
    # Load the HTML content from a file
    html_file_path = Path("templates/login.html")
    html_content = html_file_path.read_text(encoding="utf-8")
    return HTMLResponse(content=html_content)

app.add_middleware(IsAuthenticated)

@app.get("/", response_class=HTMLResponse)
async def read_root():
    # Load the HTML content from a file
    html_file_path = Path("templates/index.html")
    html_content = html_file_path.read_text(encoding="utf-8")
    return HTMLResponse(content=html_content)


if __name__ == "__main__":
    port = os.getenv("PORT", 8000)
    port = int(port)
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=port)
