from pydantic import BaseModel, EmailStr, Field

class UserFields(BaseModel):
    email: EmailStr = Field(description='User email', examples=['example@gmail.com'])
