# app.py
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

# def _find_next_id():
#     return max(sensor.sensor_id for sensor in sensors) + 1

class sensor(BaseModel):
    #sensor_id: str = Field(default_factory=_find_next_id, alias="id")
    sensor_id: str
    data_points: list
    notes: str
    timestamp: str
    shape: str

sensors = [
    sensor(sensor_id="SENSOR-000",
         data_points=[[1,1]],
         notes="Sample Data",
         timestamp="2025-10-29T18:15:39.697037+00:00", 
         shape="point")
]

@app.get("/sensors")
async def get_sensors():
    return sensors

@app.post("/sensors", status_code=201)
async def add_sensor(sensor: sensor):
    sensors.append(sensor)
    return sensor