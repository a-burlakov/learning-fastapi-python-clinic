import os.path
from datetime import datetime

from fastapi import FastAPI, Path, Body
from pydantic import BaseModel

app = FastAPI()

#
# @app.get("/hello")
# def get_hello_world():
#     return {"answer": "Hello World"}
#
#
# @app.get("/items/{item_id}")
# def get_item(item_id: int):
#     return {"item_id": item_id}
#
#

ACTIVITIES_FOLDER = "activities"


class Activity(BaseModel):
    id: int
    name: str
    date: datetime


@app.post("/activity/add/{activity_id}")
def add_activity(
    activity_id: int = Path(
        title="Айдишник активности!", description="Передается в заголовке"
    ),
    activity: Activity = Body(),
):
    file_name = f"activity_{activity_id}.json"
    with open(os.path.join(ACTIVITIES_FOLDER, file_name), "w") as f:
        f.write(activity.json())

    return True
