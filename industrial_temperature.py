def trigger_alarm(temperatures, threshold = 80):
    sensores = []
    for sensor, temp in temperatures.items():
        if temp > threshold:
            sensores.append(sensor)
    return sensores