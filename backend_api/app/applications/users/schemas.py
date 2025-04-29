from pydantic import BaseModel, EmailStr, Field, model_validator, ValidationInfo

class BaseFields(BaseModel):
    email: EmailStr = Field(description='User email', examples=['mohnatuy0@gmail.com'])
    name: str = Field(description='User nickname', examples=['MOHNATUY'])

class PasswordField(BaseModel):
    password: str = Field(min_length=8)

    @model_validator(mode="before")
    def validate_password(cls, values: dict, info: ValidationInfo) -> dict:
        password = (values.get('password') or '').strip()
        if len(password) < 8:
            raise ValueError('Too short password')
        if  ' ' in password:
            raise ValueError('No spaces in password, please')
        return values

class RegisterUserFields(BaseFields, PasswordField):
    pass