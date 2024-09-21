from fastapi import APIRouter
from service.generate_quiz_service import GenerateQuiz

router = APIRouter(prefix="/api")

class Quiz:
    
    @router.get("/quiz")
    def generate_quiz():
        return GenerateQuiz.generate_quiz()
