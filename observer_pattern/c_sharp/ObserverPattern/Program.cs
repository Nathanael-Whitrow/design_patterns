using System;

namespace ObserverPattern
{
    class Program
    {
        static void Main(string[] args)
        {
            var weatherData = new WeatherData();

            var forecastDisplay = new ForecastDisplay(weatherData);
            var statisticsDisplay = new StatisticsDisplay(weatherData);
            var thirdPartyDisplay = new ThirdPartyDisplay(weatherData);
            var currentConditionsDisplay = new CurrentConditionsDisplay(weatherData);

            weatherData.SetMeasurements(80.0f, 100.0f, 1100.012f);
            weatherData.SetMeasurements(90.0f, 130.0f, 1500.012f);
            weatherData.SetMeasurements(910.0f, 120.0f, 1700.012f);


        }
    }
}
