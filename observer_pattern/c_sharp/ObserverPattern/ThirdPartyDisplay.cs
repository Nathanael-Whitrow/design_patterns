using System;
using System.Collections.Generic;
using System.Text;

namespace ObserverPattern
{
    class ThirdPartyDisplay : IObserver, IDisplayElement
    {
        private string _thirdParty { get; set; }
        private readonly ISubject Subject;

        public ThirdPartyDisplay(ISubject weatherData)
        {
            Subject = weatherData;
            Subject.RegisterObserver(this);
        }
        public void Display()
        {
            Console.WriteLine($"THIRD PARTY: {_thirdParty}");
        }

        public void Update(float temp, float humidity, float pressure)
        {
            _thirdParty = $"temp: {temp}, hum: {humidity}, float: {pressure}";
            Display();
        }
    }
}
