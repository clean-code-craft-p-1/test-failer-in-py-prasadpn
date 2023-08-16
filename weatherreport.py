

def sensorStub():
    return {
        'temperatureInC': 50,
        'precipitation': 70,
        'humidity': 26,
        'windSpeedKMPH': 52
    }


def rainy_sensorStub_for_failure():
    return {
        'temperatureInC': 50,
        'precipitation': 65,
        'humidity': 26,
        'windSpeedKMPH': 23
    }

def precipitation_sensorStub_for_failure():
    return {
        'temperatureInC': 50,
        'precipitation': 65,
        'humidity': 26,
        'windSpeedKMPH': 49
    }


def report(sensorReader):
    readings = sensorReader()
    weather = "Sunny Day"

    if readings['temperatureInC'] > 25:
        if readings['precipitation'] >= 20 and readings['windSpeedKMPH'] >= 40:
            weather = "Partly Cloudy"
        elif readings['precipitation'] >= 20 and readings['windSpeedKMPH'] < 40:
            weather = "Alert, Stormy with heavy rain"
    return weather


def testRainy():
    #weather = report(sensorStub)
    weather = report(rainy_sensorStub_for_failure)
    print(weather)
    assert("rain" in weather)


def testHighPrecipitation():
    # This instance of stub needs to be different-
    # to give high precipitation (>60) and low wind-speed (<50)

    #weather = report(sensorStub)
    weather = report(precipitation_sensorStub_for_failure)

    # strengthen the assert to expose the bug
    # (function returns Sunny day, it should predict rain)
    print(weather)
    assert("Cloudy" in weather)


testRainy()
testHighPrecipitation()


# def main():
#     testRainy()
#    # testHighPrecipitation()
#     print("All is well (maybe)\n");
