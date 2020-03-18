using System;

namespace ObserverPattern
{
    class CurrentConditionsDisplay : IObserver, IDisplayElement
    {
        private float Temp;
        private float Pressure;
        private float Humidity;
        internal ISubject Subject { get; }

        public CurrentConditionsDisplay(ISubject subject)
        {
            Subject = subject;
            Subject.RegisterObserver(this);
        }

        public void Display()
        {
            Console.WriteLine($"CURRENT: {Temp}, {Pressure}, {Humidity}");
        }

        public void Update(float temp, float humidity, float pressure)
        {
            Temp = temp;
            Humidity = humidity;
            Pressure = pressure;
            Display();
        }
    }
}
