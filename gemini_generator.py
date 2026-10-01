class GeminiDocumentGenerator:
    def generate_document(
        self,
        document_type: str,
        parties: str,
        terms: str,
        effective_date: str
    ):
        return f"""
LEGAL DOCUMENT DRAFT
--------------------

Document Type: {document_type}

Parties:
{parties}

Terms and Conditions:
{terms}

Effective Date: {effective_date}

Note:
This is an AI-generated draft for educational purposes.
Please have it reviewed by a qualified legal professional
before using it as an official legal document.
"""