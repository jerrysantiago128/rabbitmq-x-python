import json
import datetime
import random
import numpy as np

def generate_json_data(sensor_id_prefix="SENSOR-", min_length=1, max_length=10):
    """
    Generates a single 2D shape data entry in JSON format.

    Args:
        sensor_id: The unique identifier for the sensor.
        min_length: The minimum number of entires in the array
        max_length: The maximum number of entires in the array

    Returns:
        A string containing a single JSON record of 2D shape.
    """
    # generate random sensor_id value
    sensor_id = sensor_id_prefix + str(random.randint(100,110))
    
    # set a number of rows for the 2D array, if num_data_points = 2, then shape should be a line, if num = 3. shape should be triangle, etc, etc
    num_data_points = random.randint(min_length, max_length)

    # use numpy create array of num_data_points rows by 2 columns, all with random floats between 10 anmd 90
    data_points = np.random.uniform(10,90, size=(num_data_points, 2))

    notes = "Generated Data"
    timestamp = datetime.datetime.now(datetime.UTC).isoformat()
    

    entry = {
        "sensor_id": sensor_id,
        "data_points": data_points,
        "notes": notes,
        "timestamp": timestamp,
        
    }

    entry["data_points"] = entry["data_points"].tolist()

    return json.dumps(entry, indent=2)

# # Example usage:
# json_record = generate_single_battery_data()
# print(json_record)