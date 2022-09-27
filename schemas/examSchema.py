from pydantic import BaseModel

class ExamSchema(BaseModel):
    testType: str = None
    subject: str = None
    limit: int = None