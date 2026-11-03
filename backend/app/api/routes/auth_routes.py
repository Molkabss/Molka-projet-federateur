from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from datetime import timedelta

from app.schemas.user_schema import UserCreate
from app.crud.user_crud import get_user_by_username, create_user
from app.core.security import hash_password, verify_password, create_access_token
from app.core.config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post("/register")
async def register_user(user: UserCreate):

    db_user = await get_user_by_username(user.username)

    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")

    hashed_password = hash_password(user.password)

    await create_user(user.username, hashed_password)

    return {"message": "User created successfully"}


@router.post("/token")
async def login_for_access_token(
        form_data: OAuth2PasswordRequestForm = Depends()
):

    user = await get_user_by_username(form_data.username)

    if not user or not verify_password(form_data.password, user["hashed_password"]):

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    access_token = create_access_token(
        data={"sub": user["username"]},
        expires_delta=access_token_expires,
    )

    return {"access_token": access_token, "token_type": "bearer"}


async def verify_token(token: str = Depends(oauth2_scheme)):

    try:

        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        username = payload.get("sub")

        if username is None:

            raise HTTPException(status_code=403, detail="Token invalid")

        return payload

    except JWTError:

        raise HTTPException(status_code=403, detail="Token invalid")


@router.get("/verify-token")
async def verify_user_token(payload: dict = Depends(verify_token)):

    return {"message": "Token is valid"}