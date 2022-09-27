import uvicorn
from fastapi import FastAPI, Depends
from routers import exam_router, root_router


# Metadata for the swagger documentation for each endpoint
tags_metadata = [
    {
        "name": "Exam",
        "description": "All endpoints related to Exams Questions answers"
    },
    {
        "name": "Root",
        "description": "Root endpoint"
    }
]


# API description
description = "API for Returning exams questions and answers with basic authentication"


# FastAPI initialization and metadata for the documentation
app = FastAPI(
    root_path="/",
    title="Exams Questions API",
    description=description,
    version="0.1.0",
    contact={
        "name": "Usama Tahir",
        "email": "usamatahir717@gmail.com"
    },
    license_info={
        "name": "Apache 2.0",
        "url": "hhtps://www.apache.org/license/LICENSE-2.0.html",
    },
    openapi_tags=tags_metadata
)


# Include routers
# router to root endpoint
app.include_router(root_router.router) # for root

# router for exams endpoint
app.include_router(exam_router.router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)