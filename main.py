import os.path
from datetime import datetime

from fastapi import FastAPI, Path, Body, Response
from pydantic import BaseModel, parse_file_as
import glob

from starlette import status

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


def find_activity(activity_id: int = 0):
    file_mask = f"*{activity_id if activity_id else ''}.json"
    return glob.glob(os.path.join(ACTIVITIES_FOLDER, file_mask))


@app.get("/activity/get/all")
def get_activity():
    res = []
    files = find_activity()
    if files:
        for file in files:
            res.append(parse_file_as(Activity, file))

    return res


@app.get("/activity/get/{activity_id}")
def get_activity(activity_id: int):
    pass


@app.post("/activity/add/{activity_id}")
def add_activity(
    activity_id: int = Path(
        title="Айдишник активности!", description="Передается в заголовке"
    ),
    activity: Activity = Body(),
    response: Response = Response(),
):
    file = find_activity(activity_id)
    if file:
        response.status_code = status.HTTP_302_FOUND
        return response
    else:
        file_name = f"activity_{activity_id}.json"
        with open(os.path.join(ACTIVITIES_FOLDER, file_name), "w") as f:
            f.write(activity.json())

    return True
