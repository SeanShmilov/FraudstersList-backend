from fastapi import APIRouter, HTTPException
from bson import ObjectId
from bson.errors import InvalidId
from database import fraudsters_collection
from models import Fraudster

router = APIRouter()


@router.get("/fraudsters")
async def get_fraudsters():
    fraudsters = []
    async for fraudster in fraudsters_collection.find():
        fraudster["_id"] = str(fraudster["_id"])
        fraudsters.append(fraudster)
    return fraudsters


@router.post("/fraudsters", status_code=201)
async def create_fraudster(fraudster: Fraudster):
    result = await fraudsters_collection.insert_one(fraudster.model_dump())
    return {"id": str(result.inserted_id)}


@router.delete("/fraudsters/{fraudster_id}")
async def delete_fraudster(fraudster_id: str):
    try:
        oid = ObjectId(fraudster_id)
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid fraudster id")
    await fraudsters_collection.delete_one({"_id": oid})
    return {"message": "Fraudster deleted"}
