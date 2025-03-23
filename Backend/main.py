from fastapi import FastAPI
from pymongo import MongoClient
from pydantic import BaseModel

app = FastAPI()

# Kết nối MongoDB
client = MongoClient("mongodb://localhost:27017")
db = client["chatbot_db"]
workflows = db["workflows"]

# Model cho workflow
class Workflow(BaseModel):
    nodes: list
    edges: list

# API để lưu workflow
@app.post("/save-workflow")
async def save_workflow(workflow: Workflow):
    workflow_id = workflows.insert_one(workflow.dict()).inserted_id
    return {"status": "success", "workflow_id": str(workflow_id)}

# API để thực thi workflow
@app.post("/execute-workflow")
async def execute_workflow(workflow_id: str, message: dict):
    workflow = workflows.find_one({"_id": workflow_id})
    if not workflow:
        return {"status": "error", "message": "Workflow not found"}

    # Logic thực thi workflow (sẽ thêm sau)
    return {"status": "success", "result": "Workflow executed"}

# API root
@app.get("/")
async def root():
    return {"message": "Backend is running!"}