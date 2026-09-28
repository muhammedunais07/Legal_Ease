import os

from dotenv import load_dotenv
from google import genai

from ai_core.templates import get_template


# =========================================================
# LOAD ENVIRONMENT VARIABLES
# =========================================================

load_dotenv()


API_KEY = os.getenv("GEMINI_API_KEY")

MODEL_NAME = os.getenv(
    "GEMINI_MODEL",
    "gemini-3.8-flash"
)


# =========================================================
# API KEY VALIDATION
# =========================================================

if not API_KEY:

    raise ValueError(
        "GEMINI_API_KEY is missing from .env file"
    )


# =========================================================
# GEMINI CLIENT
# =========================================================

client = genai.Client(
    api_key=API_KEY
)


# =========================================================
# DOCUMENT GENERATOR
# =========================================================

class GeminiDocumentGenerator:

    def generate_document(
        self,
        document_type,
        parties,
        terms,
        dates
    ):

        # -------------------------------------------------
        # Get document template
        # -------------------------------------------------

        template = get_template(
            document_type
        )

        sections = template["sections"]


        # -------------------------------------------------
        # Convert sections to readable format
        # -------------------------------------------------

        section_list = "\n".join(
            f"{index + 1}. {section}"
            for index, section in enumerate(sections)
        )


        # -------------------------------------------------
        # Gemini Prompt
        # -------------------------------------------------

        prompt = f"""
You are LegalEase, an AI-powered legal document
drafting assistant.

Your task is to create a professional legal-document
DRAFT based ONLY on the information supplied by the user.

========================================================
DOCUMENT INFORMATION
========================================================

Document Type:
{document_type}

Parties:
{parties}

Terms and Conditions:
{terms}

Important Dates:
{dates}


========================================================
REQUIRED DOCUMENT SECTIONS
========================================================

{section_list}


========================================================
DRAFTING RULES
========================================================

1. Create a professional and well-structured legal
   document.

2. Use the required sections listed above.

3. Use clear, formal, and professional legal language.

4. DO NOT invent facts.

5. DO NOT invent:
   - Names
   - Addresses
   - Dates
   - Payment amounts
   - Percentages
   - Duties
   - Legal obligations
   - Locations
   - Signatory information

6. If required information is missing, write:

   [INSERT INFORMATION]

   instead of making up information.

7. Keep the information supplied by the user accurate.

8. Do not introduce facts that were not provided.

9. Include a proper signature section at the end.

10. Use numbered clauses where appropriate.

11. Keep the document organized and easy to edit.

12. Do not claim that this document is automatically
    legally valid or legally binding.

13. Do not provide a legal opinion.

14. At the end of the document, include this notice:

    "IMPORTANT NOTICE:
    This document is an AI-generated draft and is not
    legal advice. It should be reviewed and customized
    by a qualified legal professional before use."


========================================================
OUTPUT FORMAT
========================================================

Return ONLY the completed legal document.

Do not include:

- Markdown code fences
- Explanations about the AI
- Analysis
- Comments before the document
- Comments after the document

Start directly with the document title.
"""


        # -------------------------------------------------
        # Gemini API Request
        # -------------------------------------------------

        interaction = client.interactions.create(
            model=MODEL_NAME,
            input=prompt
        )


        # -------------------------------------------------
        # Extract Response
        # -------------------------------------------------

        if not interaction.output_text:

            raise ValueError(
                "Gemini returned an empty response"
            )


        return interaction.output_text