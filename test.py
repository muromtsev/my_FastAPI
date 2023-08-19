from datetime import datetime
from typing import List, Union

from pydantic import BaseModel


# создаём модель данных, которая обычная расположена в файле models.py
class User(BaseModel):
    id: int
    name: str = "John Doe"
    signup_ts: Union[datetime, None] = None
    friends: List[int] = []

# Внешние данные, имитирует входящий JSON
external_data = {
    "id": "123",
    "signup_ts": "2017-06-01 12:22",
    "friends": [1, "2", b"3"],
}

user = User(**external_data)
print(user)