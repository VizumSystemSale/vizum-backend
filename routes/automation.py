from fastapi import APIRouter, HTTPException
import openai
import os

router = APIRouter()

@router.post("/generate_full_tiktok_package")
async def generate_full_tiktok_package(topic: str):
    """Generate TikTok package: text, hook, hashtags, and CTA."""
    try:
        openai.api_key = os.getenv("OPENAI_API_KEY")
        prompt = (
            f"Create a TikTok marketing package for the topic: {topic}.\n"
            f"Return JSON with keys: text, hook, hashtags, cta."
        )
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150,
            temperature=0.7
        )
        return {"package": response.choices[0].text.strip()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/publish_to_etsy")
async def publish_to_etsy(data: dict):
    """Stub endpoint for future Etsy integration."""
    return {"status": "success", "message": "Etsy integration coming soon."}

@router.post("/publish_to_facebook")
async def publish_to_facebook(data: dict):
    """Stub endpoint for future Facebook integration."""
    return {"status": "success", "message": "Facebook integration coming soon."}
