# Rest Api Architecture:

## Endpoints and Resource Structure

Sensors have unique ids: (GET/POST)
list of sensors:
- /sensors

Single sensor: (GET/PUT/PATCH/DELETE)
- /sensors/<unqiue-sensor-id> 
	- ex: "SENSOR-001"

Each sensor_id has the following fields/structure:
        "sensor_id": sensor_id, (str)
        "data_points": data_points, (list of floats)
        "notes": notes, (str)
        "timestamp": timestamp, (str?)

Each shape can be "drawn" or plotted based on its data points provided (TODO)


## Data Format
The data format will be JSON:
"Content-type": "application/json"

## Error Handling
Error response for invalid requests will exists (400/500/etc)

## Tech
### FastAPI:

Harder to learn that Flask, but offers more control and has more use cases for AI/ML tasking in the future. 
Main selling point now is data validation.

https://realpython.com/api-integration-in-python/#fastapi