using System;
using System.Collections.Generic;
using System.Text;

namespace ObserverPattern
{
    class ForecastDisplay : IObserver, IDisplayElement
    {
        private string _forecast { get; set; }
        private readonly ISubject Subject;

        public ForecastDisplay(ISubject weatherData)
        {
            Subject = weatherData;
            Subject.RegisterObserver(this);
        }
        public void Display()
        {
            Console.WriteLine($"FORECAST:: {_forecast}");
        }
        public void Update(float temp, float humidity, float pressure)
        {
            var forecastCalc = temp * humidity * pressure;
            _forecast = forecastCalc < 100 ? "WET" : forecastCalc < 200 ? "MEDIUM" : "DRY";
            Display();
        }




    }
}
