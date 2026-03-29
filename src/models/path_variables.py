from pydantic import BaseModel
from enum import Enum

class User(BaseModel):
    admin_user: str = "admin"
    monitor_user: str = "monitor"
    normal_user: str = "user"