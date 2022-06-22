from fastapi import APIRouter, Query

router = APIRouter(prefix='/ads/amount/observer')


@router.get('/stat')
async def get_stat():
    pass


@router.post('/add')
async def add_observation(
    query: str = Query(),
    location_id: int = Query()
):
    pass
