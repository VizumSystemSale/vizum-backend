from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routes import products, shopify, video, telegram, subscribe, trial, automation
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(title="Vizum System Sale", description="Автоматизированная AI-платформа для e-commerce")

# Безопасность: все API ключи берутся только из .env и нигде не отображаются на клиенте
if not os.getenv("OPENAI_API_KEY") or not os.getenv("SHOPIFY_API_KEY"):
    raise RuntimeError("Ключи API не установлены. Убедитесь, что .env файл заполнен.")

# Подключение frontend статики (мультиязычный лендинг)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Подключение маршрутов
app.include_router(products.router, prefix="/products")
app.include_router(shopify.router, prefix="/shopify")
app.include_router(video.router, prefix="/video")
app.include_router(telegram.router, prefix="/telegram")
app.include_router(subscribe.router, prefix="/subscribe")
app.include_router(trial.router, prefix="/trial")
app.include_router(automation.router, prefix="/automation")

# Локальный запуск (не используется на Render)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
