from weather_data import WeatherData
from display_elements import CurrentConditionsDisplay, \
							ForecastDisplay, StatisticsDisplay


def main():
	weatherStation = WeatherData()

	currentConditonsDisplay = CurrentConditionsDisplay(weatherStation)
	forecastDisplay = ForecastDisplay(weatherStation)
	statisticsDisplay = StatisticsDisplay(weatherStation)

	currentConditonsDisplay.display()
	forecastDisplay.display()
	statisticsDisplay.display()

	weatherStation.setMeasurements(12.0, 25.0, 10.0)
	weatherStation.setMeasurements(25.0, 15.0, 12.0)
	weatherStation.setMeasurements(5.0, 10.0, 8.0)


if __name__ == '__main__': main()