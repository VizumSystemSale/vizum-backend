from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.post("/subscribe_user")
async def subscribe_user(user_id: str):
    try:
        return {"message": "Subscription activated for user", "user_id": user_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
