from fastapi import APIRouter

router = APIRouter()


@router.post("/teste/")
def teste_route_one():
    return {"message": "Hello World!"}    