using System;
using System.Collections.Generic;
using System.Text;

namespace ObserverPattern
{
    class StatisticsDisplay : IObserver, IDisplayElement
    {
        private List<Statistics> _stats;
        private readonly ISubject Subject;

        public StatisticsDisplay(ISubject weatherData)
        {
            this.Subject = weatherData;
            Subject.RegisterObserver(this);
            _stats = new List<Statistics>();
        }
        public void Display()
        {
            Console.WriteLine("STATS:");
            foreach(var stat in _stats)
            {
                Console.WriteLine($"{stat.Temp}, {stat.Pressure}, {stat.Humidity}");
            }
            
        }

        public void Update(float temp, float humidity, float pressure)
        {
            _stats.Add(new Statistics
            {
                Temp = temp,
                Humidity = humidity,
                Pressure = pressure
            });
            Display();
        }
    }

    public class Statistics
    {
        public float Temp { get; set; }
        public float Humidity { get; set; }
        public float Pressure { get; set; }
    }
}
