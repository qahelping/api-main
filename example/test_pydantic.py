from pydantic import BaseModel, Field, HttpUrl, EmailStr, validator, field_validator


class User(BaseModel):
    id: int
    name: str = "John Doe"
    email: str | None = None
    is_active: bool = True


# Создание экземпляра
user = User(id=1, name="Alice")

# Автоматическое приведение типов
user2 = User(id="2", is_active="yes")

print(user.name)  # "Alice"

pass

class Profile(BaseModel):
    username: str = Field(min_length=3, max_length=20)
    website: HttpUrl  # автоматическая валидация URL
    email: EmailStr  # валидация email
    age: int = Field(gt=0, le=120)
    password: str

    @field_validator('password')
    def password_complexity(cls, v):
        if len(v) < 8:
            raise ValueError("Password must be at least 8 characters")
        if not any(c.isupper() for c in v):
            raise ValueError("Password must contain uppercase letter")
        return v

    class Config:
        extra = "forbid"  # запрещает дополнительные поля
        frozen = True  # делает модель неизменяемой
        allow_mutation = False  # запрещает изменение полей

profile_obj = Profile(username='ALena', website='', email='', age=-10, password='Qwerty123')
print(profile_obj)