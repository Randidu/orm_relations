
from sqlalchemy.ext.asyncio import AsyncSession
from response_models import StudentCreate
from db_models import Student, enrollment


class StudentRepository:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self,data: StudentCreate) -> Student:

        student = Student(name =data.name,email = data.email,enrollment_year = data.enrollment_year)

        if data.profile:
            Student.profile = Student(
                qualifications=data.profile.qualification,
                department=data.profile.department,
                office_number=data.profile.office_number,
                bio=data.profile.bio

            )
        self.db.add(Student)
        await self.db.commit()
        await self.db.refresh(Student)
        return student




