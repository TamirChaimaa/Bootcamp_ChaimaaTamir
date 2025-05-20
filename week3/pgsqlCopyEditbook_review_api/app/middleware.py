import datetime
from typing import Optional
from fastapi import HTTPException, Header, Request, Response
from jose import ExpiredSignatureError, JWTError
import jwt
import bcrypt
from crud import User  # Assure-toi que la classe User est bien connectée à PostgreSQL # Contient SECRET_KEY
from starlette.middleware.base import BaseHTTPMiddleware


class AuthService:
     @staticmethod
     def signup(username: str, email: str, password: str, role: str):
        existing_user = User.find_by_email(email)
        if existing_user:
            return {"error": "Email déjà utilisé."}

        # On crée un user avec rôle admin pour pouvoir appeler create_user (car create_user vérifie self.role == 'admin')
        admin_user = User(username, email, password,role)

        # On modifie les attributs admin_user pour correspondre à l'utilisateur à créer
        admin_user.username = username
        admin_user.email = email
        admin_user.role = role
        # Le password sera hashé dans __init__, mais ici on doit créer le hash manuellement
        # car on n'appelle pas __init__ sur admin_user, donc on hash ici :
        admin_user.password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        try:
            admin_user.create_user()
            return {"message": "Utilisateur créé avec succès", "email": email}
        except Exception as e:
            return {"error": f"Erreur lors de la création : {e}"}

     @staticmethod
     def signin(email: str, password: str):
        user = User.find_by_email(email)
        if not user:
            return {"error": "Identifiants invalides."}

        if not bcrypt.checkpw(password.encode("utf-8"), user.password_hash.encode("utf-8")):
            return {"error": "Identifiants invalides."}

        payload = {
            "email": user.email,
            "role": user.role,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }

        token = jwt.encode(payload, "123456", algorithm="HS256")
        User.token_user = token
        return {"token": token}
     
class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        public_paths = ["/signin","/signup"]
        if any(request.url.path.startswith(path) for path in public_paths):
            return await call_next(request)

        token = request.headers.get("Authorization")
        if not token:
            raise HTTPException(status_code=403, detail="No auth token provided")

        try:
            scheme, jwt_token = token.split()
            if scheme.lower() != "bearer":
                raise HTTPException(status_code=403, detail="Invalid token scheme")
            payload = jwt.decode(jwt_token, "123456", algorithms="HS256")
            request.state.user = payload
        except (JWTError, ValueError):
            raise HTTPException(status_code=403, detail="Invalid or expired token")

        return await call_next(request)