from fastapi import APIRouter, status


router_users = APIRouter()

@router_users.post('/create', status_code=status.HTTP_201_CREATED)
async def create_user():
    return {"st": 200}

