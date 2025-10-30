# app.py
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List

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

sensors: List[sensor] = [
    sensor(sensor_id="SENSOR-000",
         data_points=[[1,1]],
         notes="Sample Data",
         timestamp="2025-10-29T18:15:39.697037+00:00", 
         shape="point")
]

@app.get("/sensors")
async def get_all_sensors():
    return sensors

@app.get("/sensors/{sensor_id}")
async def get__unique_sensor(sensor_id: str):
    """
    Retrieves a specific sensor by its unique ID.
    
    Needs to:
    1. Accept the sensor_id parameter from the URL path.
    2. Iterate through the 'sensors' list to find a match.
    """
    
    found_sensor =  next((s for s in sensors if s.sensor_id == sensor_id), None)

    if found_sensor is None:
        # If no sensor is found, raise an HTTP 404 Not Found error.
        raise HTTPException(
            status_code=404, 
            detail=f"Sensor with ID '{sensor_id}' not found."
        )
        
    return found_sensor

@app.post("/sensors", status_code=201)
async def add_sensor(new_sensor: sensor):
    """
    Adds a new sensor to the list. 
    Note: Changed endpoint from /sensors/{sensor_id} to /sensors 
    since the sensor object contains its own ID.
    """

    # Check for duplicates before adding
    if next((s for s in sensors if s.sensor_id == new_sensor.sensor_id), None):
        raise HTTPException(
            status_code=409, # 409 Conflict
            detail=f"Sensor with ID '{new_sensor.sensor_id}' already exists."
        )
    sensors.append(new_sensor)
    return new_sensor