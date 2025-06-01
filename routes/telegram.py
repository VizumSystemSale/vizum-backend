from fastapi import APIRouter, HTTPException
import requests
import os

router = APIRouter()

@router.post("/create_telegram_bot_hook")
async def create_telegram_bot_hook(url: str):
    try:
        telegram_token = os.getenv("TELEGRAM_BOT_TOKEN")
        set_webhook_url = f"https://api.telegram.org/bot{telegram_token}/setWebhook"
        response = requests.post(set_webhook_url, data={"url": url})
        if response.status_code == 200:
            return {"message": "Webhook set successfully"}
        else:
            raise HTTPException(status_code=response.status_code, detail=response.text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
