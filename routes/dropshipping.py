from fastapi import APIRouter, HTTPException
import requests
import os

router = APIRouter()

@router.post("/dropshipping/connect")
async def connect_to_dropshipping(partner: str):
    """
    Подключение к дропшип-платформе: cj, autods, zendrop
    """
    try:
        if partner not in ["cj", "autods", "zendrop"]:
            raise HTTPException(status_code=400, detail="Unknown partner")

        # Загружаем ключи из .env
        api_key = os.getenv(f"{partner.upper()}_API_KEY")
        if not api_key:
            raise HTTPException(status_code=400, detail="API key not found")

        # Пример запроса (можно расширять под каждого партнёра)
        if partner == "cj":
            url = "https://developers.cjdropshipping.com/api2.0/v1/authentication/getAccessToken"
            headers = {"CJ-Access-Token": api_key}
            response = requests.get(url, headers=headers)
        elif partner == "autods":
            url = "https://api.autods.com/v1/store"
            headers = {"Authorization": f"Bearer {api_key}"}
            response = requests.get(url, headers=headers)
        elif partner == "zendrop":
            url = "https://api.zendrop.com/v1/me"
            headers = {"Authorization": f"Bearer {api_key}"}
            response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return {"message": f"Connected to {partner} successfully"}
        else:
            raise HTTPException(status_code=500, detail=f"{partner} API error: {response.text}")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
