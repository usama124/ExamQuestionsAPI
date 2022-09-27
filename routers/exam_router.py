from fastapi import APIRouter, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from schemas.examSchema import ExamSchema
from services import exams

security = HTTPBasic()

# Router declaration (replace the prefix if needed)
# Metadata for the swagger documentation
router = APIRouter(
    prefix="",
    tags=["Exam"]
)


auth_obj = {
"alice": "wonderland",
"bob": "builder",
"clementine": "mandarine"
}


# The analytics route, receive the example input as body
# Then it uses the services to process thedataset

# Route for minimum dataset input
@router.get("/exams/questions", summary="API for returning exams questions")
async def get_exams_data(examSchema: ExamSchema, credentials: HTTPBasicCredentials = Depends(security)):
    exam_data = []
    auth_obj_found = auth_obj.get(credentials.username, None)
    if not auth_obj_found:
        return {"error": True, "message": "user not found"}
    if auth_obj_found != credentials.password:
        return {"error": True, "message": "Password does not matched."}

    exam_data = exams.get_exams_questions_data("Data/questions.xlsx", examSchema.limit, examSchema.testType, examSchema.subject)

    return {"error": False, "message": "Exams data found", "data": exam_data}