from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials, OAuth2PasswordBearer
from fastapi.responses import JSONResponse
import jwt
from utils import generate_jwt, verify_jwt
from datetime import timedelta

app = FastAPI()

# Basic Auth setup
security_basic = HTTPBasic()

# OAuth2 setup for JWT Bearer Token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# Route for Basic Authentication
@app.get("/basic-auth")
def basic_auth(credentials: HTTPBasicCredentials = Depends(security_basic)):
    if credentials.username == "admin" and credentials.password == "password":
        return {"message": "Successfully authenticated using Basic Auth!"}
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Basic"},
        )

# Route for JWT Authentication
@app.get("/jwt-auth")
def jwt_auth(token: str = Depends(oauth2_scheme)):
    try:
        payload = verify_jwt(token, "supersecretkey")
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid token")

    return {"message": "Successfully authenticated using JWT Auth!"}

# Route to get JWT token
@app.post("/login")
def login(credentials: HTTPBasicCredentials = Depends(security_basic)):
    if credentials.username == "admin" and credentials.password == "password":
        token = generate_jwt({"user": credentials.username}, "supersecretkey", timedelta(minutes=30))
        return {"token": token}
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Basic"},
        )

