from fastapi import APIRouter, HTTPException
import openai
import os

router = APIRouter()

@router.post("/generate_product")
async def generate_product(name: str):
    try:
        openai.api_key = os.getenv("OPENAI_API_KEY")
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Generate a product description for {name}.",
            max_tokens=50
        )
        description = response.choices[0].text.strip()
        return {"name": name, "description": description}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
