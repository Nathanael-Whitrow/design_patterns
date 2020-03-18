using System;
using System.Collections.Generic;
using System.Text;

namespace ObserverPattern
{
    interface ISubject
    {
        public void RegisterObserver(IObserver o);

        public void RemoveObserver(IObserver o);

        public void NotifyObservers();

        public void SetMeasurements(float t, float h, float p);
    }
}
