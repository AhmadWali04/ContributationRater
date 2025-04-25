import os
import sys
import uuid
import datetime

from typing import Optional, List, Dict, Any

from pydantic import BaseModel

class User(BaseModel):
    id: uuid.UUID = uuid.uuid4()
    username: str
    email: str
    password: str
    created_at: datetime.datetime
    updated_at: datetime.datetime

class Platform(BaseModel):
    pass

class Project(BaseModel):
    pass

class ProjectPlatform(BaseModel):
    pass

class ProjectUser(BaseModel):
    pass

class ActivityLog(BaseModel):
    pass