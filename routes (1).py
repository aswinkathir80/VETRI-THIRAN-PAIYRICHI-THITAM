from fastapi import APIRouter
from pydantic import BaseModel
from ai_core.gemini_generator import GeminiDocumentGenerator

router = APIRouter()
generator = GeminiDocumentGenerator()

class DocumentRequest(BaseModel):
    document_type: str
    parties: str
    terms: str
    effective_date: str

@router.post("/generate")
def generate_document(data: DocumentRequest):
    result = generator.generate_document(
        document_type=data.document_type,
        parties=data.parties,
        terms=data.terms,
        effective_date=data.effective_date
    )
    return {"document": result}