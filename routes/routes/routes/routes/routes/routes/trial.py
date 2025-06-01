from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.post("/activate_trial")
async def activate_trial(user_id: str):
    try:
        return {
            "message": "Trial activated for user",
            "user_id": user_id,
            "limitations": {
                "max_products": 1,
                "max_videos": 1,
                "days": 3
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
