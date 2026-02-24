from fastapi import HTTPException
from jose import jwt, JWTError
from app.config import SECRET_KEY, ALGORITHM

#登入與 Token 驗證
def get_role_from_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload.get("role")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
