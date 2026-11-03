from pydantic import BaseModel, field_validator


class UserCreate(BaseModel):

    username: str

    password: str

    @field_validator("password")
    @classmethod
    def password_max_72_bytes(cls, v: str):

        if len(v.encode("utf-8")) > 72:
            raise ValueError("Password too long (bcrypt limit is 72 bytes).")

        return v