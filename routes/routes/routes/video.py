from fastapi import APIRouter, HTTPException
import openai
import os

router = APIRouter()

@router.post("/generate_video_idea")
async def generate_video_idea(topic: str):
    try:
        openai.api_key = os.getenv("OPENAI_API_KEY")
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Generate a TikTok video idea for the topic: {topic}.",
            max_tokens=50
        )
        idea = response.choices[0].text.strip()
        return {"topic": topic, "idea": idea}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
