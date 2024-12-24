from fastapi import APIRouter, status, HTTPException
from util.db import start_db_data


router = APIRouter()

@router.get('/reset', status_code=status.HTTP_200_OK)
def get_available_routes():
    try:
        start_db_data()
    except HTTPException as e:
        raise e  
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred: {str(e)}"
        )
    
    return {"message": "DB Reset Concluded !!!"}