import json
import datetime
import random

def generate_json_data(sensor_id="SENSOR-001", min_level=20, max_level=100):
    """
    Generates a single battery sensor data entry in JSON format.

    Args:
        sensor_id: The unique identifier for the sensor.
        min_level: The minimum battery level percentage.
        max_level: The maximum battery level percentage.

    Returns:
        A string containing a single JSON record of battery data.
    """

    timestamp = datetime.datetime.now(datetime.UTC).isoformat()
    battery_level = random.randint(min_level, max_level)
    voltage = round(random.uniform(3.0, 4.2), 2)
    current = round(random.uniform(-0.5, 1.0), 2)
    charging_status = random.choice(["Charging", "Discharging", "Idle"])
    notes = "Generated Battery Data"

    entry = {
        "sensor_id": sensor_id,
        "battery_level": battery_level,
        "voltage": voltage,
        "current": current,
        "charging_status": charging_status,
        "timestamp": timestamp,
        "notes": notes
    }

    return json.dumps(entry, indent=2)

# # Example usage:
# json_record = generate_single_battery_data()
# print(json_record)