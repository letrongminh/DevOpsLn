import motor.motor_asyncio
import os
from model import Student, student_helper
import pydantic
from bson import ObjectId

pydantic.json.ENCODERS_BY_TYPE[ObjectId] = str

# mongoHost = os.getenv("MONGODB_HOST", "mongodb")
mongoHost = os.getenv("MONGODB_HOST", "localhost")
url = f"mongodb://{mongoHost}:27017/vdt2023"
client = motor.motor_asyncio.AsyncIOMotorClient(url)

database = client.VDT
collection = database.student


async def fetch_all_students():
    students = []
    async for student in collection.find():
        students.append(student_helper(student))
    return students


async def fetch_one_student(id):
    student = await collection.find_one({"_id": ObjectId(id)})
    if student:
        return student


async def create_student(data: dict) -> dict:
    student = await collection.insert_one(data)
    new_student = await collection.find_one({"_id": student.inserted_id})
    return student_helper(new_student)


async def update_student(id: str, data: dict):
    if len(data) < 1:
        return False
    student = await collection.find_one({"_id": ObjectId(id)})
    if student:
        updated_student = await collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_student:
            return True
        return False


async def remove_student(id):
    student = await collection.find_one({"_id": ObjectId(id)})
    if student:
        await collection.delete_one({"_id": ObjectId(id)})
        return True
