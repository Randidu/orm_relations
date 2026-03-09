import email
import profile
from datetime import datetime
from typing import Optional

from pydantic import Field, BaseModel


class TeacherProfileBase(BaseModel):
    qualification: Optional[str] = Field(None, max_length=300)
    department: Optional[str] = Field(None,max_length=200)
    office_number: Optional[str] = Field(None,max_length=30)
    bio: Optional[str] = None

class TeacherProfileCreate(TeacherProfileBase):
    pass

class TeacherProfileUpdate(TeacherProfileBase):
    pass

class TeacherProfileResponse(TeacherProfileBase):
    id: int
    teacher_id: int

    class Config:
        from_attributes = True

class TeacherBase(BaseModel):
    name: str = Field(..., min_lengthh=3, max_length=255)
    email: str

class TeacherCreate(TeacherBase):
    profile: Optional[TeacherProfileCreate] =None

class TeacherResponse(TeacherBase):
    id:int
    created_at: datetime
    profile: Optional[TeacherProfileResponse] =None

    class Config:
        from_attributes =True