from datetime import timedelta
from jose import JWTError,jwt
import uvicorn
from fastapi import FastAPI,Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from user import create_access_token,authenticate_user, fake_users_db, ACCESS_TOKEN_EXPIRE_MINUTES,SECRET_KEY,ALGORITHM,User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post('/token')
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="사용자가 존재하지 않습니다.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


async def get_jwt_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='인증 정보를 검증할 수 없습니다.',
        headers={'WWW-Authenticate': 'Bearer'},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_dict: dict = payload.get('user')
        if not user_dict:
            raise credentials_exception
        user = User(**user_dict)
    except JWTError:
        raise credentials_exception
    if user is None:
        raise credentials_exception
    return user

if __name__ == "__main__":
    uvicorn.run(app='main:app', host="0.0.0.0", port=8000, reload=True)