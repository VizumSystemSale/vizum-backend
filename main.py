from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routes import products, shopify, video, telegram, subscribe, trial
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Mount the static directory
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(products.router, prefix="/products")
app.include_router(shopify.router, prefix="/shopify")
app.include_router(video.router, prefix="/video")
app.include_router(telegram.router, prefix="/telegram")
app.include_router(subscribe.router, prefix="/subscribe")
app.include_router(trial.router, prefix="/trial")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
