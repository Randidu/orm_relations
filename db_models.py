from datetime import datetime
from typing import Optional, List
from sqlalchemy import String, Text, ForeignKey, func, Integer, Boolean, Table, Column
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass

enrollment = Table(
     "enrollments",Base.metadata,
    Column("student_id",Integer,ForeignKey("students.id",ondelete="CASCADE"),primary_key=True),
    Column("course_id",Integer,ForeignKey("courses.id",ondelete="CASCADE"),primary_key=True)
 )

class Teacher(Base):
    __tablename__ = "teachers"

    id: Mapped[int] = mapped_column(primary_key=True,index=True)
    name:Mapped[str] = mapped_column(String(255))
    email:Mapped[str] = mapped_column(String(255))
    created_at : Mapped[datetime] = mapped_column(
        server_default=func.now(), default=datetime.now()
    )

    profile:Mapped[Optional["TeacherProfile"]] = relationship(
        back_populates="teacher",
        uselist=False,
        cascade="all, delete-orphan",
        lazy="joined"
    )
    courses : Mapped[List["Courses"]] = relationship(
        back_populates="teacher",
        cascade="all , delete-orphan",
        lazy="selectin"
    )

class Courses(Base):
    __tablename__ = "courses"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    teacher_id: Mapped[int] = mapped_column(ForeignKey("teachers.id", ondelete="CASCADE"))
    name: Mapped[str] = mapped_column(String(300), nullable=False)
    code: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    credit: Mapped[int] = mapped_column(Integer, default=5, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now(), default=datetime.now)

    teacher: Mapped["Teacher"] = relationship(back_populates="courses")
    students:Mapped[List["students"]] =relationship(secondary=enrollment,back_populates="courses",lazy="selectin")

class TeacherProfile(Base):
    __tablename__ = "teacher_profiles"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    teacher_id: Mapped[int] = mapped_column(
        ForeignKey("teachers.id", ondelete="CASCADE")
    )
    qualifications: Mapped[Optional[str]] = mapped_column(String(300), nullable=True)
    department: Mapped[Optional[str]] = mapped_column(String(250), nullable=True)
    office_number: Mapped[Optional[str]] = mapped_column(String(250), nullable=True)
    bio: Mapped[str] = mapped_column(Text)

    teacher: Mapped["Teacher"] = relationship(back_populates="profile")


class Student(Base):
    __table__ = "students"

    id : Mapped[int]= mapped_column(primary_key=True,index=True)
    name : Mapped[str]= mapped_column(String(255))
    email : Mapped[str]= mapped_column(String(255))
    enrollment_year : Mapped[int]

    courses : Mapped[List["Courses"]] = relationship(secondary=enrollment,back_populates="students",lazy="selectin")


