from fastapi import FastAPI, HTTPException, Depends, Header
from typing import Optional
import jwt
from middleware import AuthService
from pydantic import BaseModel
from database import connect_to_db
import uvicorn
from middleware import AuthMiddleware
from crud import User  # Import de ta classe User

app = FastAPI()

class SignupModel(BaseModel):
    username: str
    email: str
    password: str
    role: str 
class SigninModel(BaseModel):
    email: str
    password: str

class UserUpdateModel(BaseModel):
    username: str
    email: str
    password: str
    role: str

class BookModel(BaseModel):
    title: str
    author: str
    description: str

class ReviewModel(BaseModel):
    rating: int
    comment: str
    book_id: int


# Middleware pour récupérer utilisateur via token JWT


@app.post("/signup")
def signup(data: SignupModel):  

    result = AuthService.signup(data.username, data.email, data.password, data.role)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result

@app.post("/signin")
def signin(data: SigninModel):
    print('Hello word')
    result = AuthService.signin(data.email, data.password)
    if "error" in result:
        raise HTTPException(status_code=401, detail=result["error"])
    return result


app.add_middleware(AuthMiddleware)
@app.get("/users")
def users():
    conn = None
    cur = None
    users = []
    try:
        conn = connect_to_db()
        if conn is None:
            raise ConnectionError("Could not connect to the database.")
        cur = conn.cursor()
        cur.execute("SELECT id, username, email, password, role FROM users")
        rows = cur.fetchall()
        for row in rows:
            user = User(username=row[1], email=row[2], password_hash=row[3], role=row[4], user_id=row[0])
            users.append({
                "id": row[0],
                "username": row[1],
                "email": row[2],
                "role": row[4]
            })
        return users
    except Exception as e:
        print("❌ Error while fetching users:", e)
        raise HTTPException(status_code=500, detail="Internal Server Error")
    finally:
        if cur: cur.close()
        if conn: conn.close()


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
