from datetime import datetime
from typing import Optional, List
from pydantic import Field, BaseModel

class TeacherProfileBase(BaseModel):
    qualification: Optional[str] = Field(None, max_length=300)
    department: Optional[str] = Field(None, max_length=200)
    office_number: Optional[str] = Field(None, max_length=30)
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
    name: str = Field(..., min_length=3, max_length=255)   # fixed typo
    email: str

class TeacherCreate(TeacherBase):
    profile: Optional[TeacherProfileCreate] = None

class CoursesBase(BaseModel):
    name: str = Field(..., max_length=300)
    code: str = Field(..., max_length=50)
    description: Optional[str] = None
    credit: Optional[int] = Field(default=5, ge=1, le=10)
    is_active: Optional[bool] = True

class CoursesCreate(CoursesBase):
    teacher_id: int = Field(..., gt=0)

class CoursesUpdate(CoursesBase):
    pass

class CoursesResponse(CoursesBase):
    id: int
    teacher_id: int
    created_at: datetime

    class Config:
        from_attributes = True

class TeacherResponse(TeacherBase):
    id: int
    created_at: datetime
    profile: Optional[TeacherProfileResponse] = None
    courses : List[CoursesResponse]=[]

    class Config:
        from_attributes = True
