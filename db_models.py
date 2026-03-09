from datetime import datetime
from tkinter.constants import CASCADE
from typing import Optional
from sqlalchemy import String, Text, ForeignKey, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass

class Teacher(Base):
    __tablename__ = "teachers"

    id: Mapped[int] = mapped_column(primary_key=True,index=True)
    name:Mapped[str] = mapped_column(String(255))
    email:Mapped[str] = mapped_column(String(255))
    created_at : Mapped[datetime] = mapped_column(
        server_default=func.now(), default=datetime.now()
    )

    profile:Mapped[Optional["Teacher_Profiles"]] = relationship(
        back_populates="teacher",
        uselist=False,
        cascade="all, delete-orphan"
    )

class TeacherProfile(Base):
    __tablename__ = "teacher_profiles"

    id:Mapped[int] = mapped_column(primary_key=True, index=True)
    teacher_id: Mapped[int] = mapped_column(
        ForeignKey("teacher.id", ondelete=CASCADE)
    )
    qualification:Mapped[Optional[str]] = mapped_column(String(300), nullable = True)
    department: Mapped[str] = mapped_column(String(250), nullable= True)
    office_number: Mapped[str] = mapped_column(String(250), nullable=True)
    bio: Mapped[str] = mapped_column(Text)