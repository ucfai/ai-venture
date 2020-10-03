import uvicorn
from typing import Any, Dict
from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()

# Using PyDantic to parse/validate the request body from DF

class Intent(BaseModel):
    displayName: str


class Request(BaseModel):
    intent: Intent
    parameters: Dict[str, Any]


@app.post("/")
async def home(queryResult: Request = Body(..., embed=True)):
    intent = queryResult.intent.displayName
    count = len(queryResult.parameters)
    text = f"I'm responding to the {intent} intent with {count} slots found: "
    text += ",".join(queryResult.parameters.values())
    return {"fulfillmentText": text}



if __name__=="__main__":
    uvicorn.run("app:app", host="localhost", port=9000, log_level="info")
