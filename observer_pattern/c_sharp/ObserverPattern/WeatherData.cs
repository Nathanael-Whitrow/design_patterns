using System;
using System.Collections.Generic;
using System.Text;

namespace ObserverPattern
{
    class WeatherData : ISubject
    {
        public float temp { get; set; }
        public float humidity { get; set; }
        public float pressure { get; set; }
        private List<IObserver> _observers;

        public WeatherData()
        {
            _observers = new List<IObserver>();
        }

        public void RegisterObserver(IObserver o)
        {
            _observers.Add(o);
        }

        public void RemoveObserver(IObserver o)
        {
            _observers.Remove(o);
        }

        public void NotifyObservers()
        {
            foreach(var observer in _observers)
            {
                observer.Update(temp, humidity, pressure);
            }
        }

        public void MeasurementsChanged()
        {
            NotifyObservers();
        }

        public void SetMeasurements(float t, float h, float p)
        {
            temp = t;
            humidity = h;
            pressure = p;
            MeasurementsChanged();
        }
    }
}
