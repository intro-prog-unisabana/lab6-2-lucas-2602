def trigger_alarm(temperatures, threshold = 80):
    for temperatura in temperatures.values():
        if temperatura > threshold:
            print("Paila")

temperatures = {
    "sensor_A": 79.0,
    "sensor_B": 81.2,
    "sensor_C": 75.4,
    "sensor_D": 85.7
}

trigger_alarm(temperatures)