#include <iostream>
#include <memory>
#include <string>

using namespace std;


// Abstract base class
class Beverage
{
public:
    Beverage() {};
    virtual ~Beverage() {};

    virtual float  getCost()        const = 0; // pure virtual makes this class abstract
    virtual string getDescription() const = 0; // pure virtual makes this class abstract

protected:
    string description;
    float cost;
};



// Concrete implementation
class Espresso : public Beverage
{
public:
    Espresso() {
       description = "espresso";
       cost = 2.99;
    };
    ~Espresso() {};

    float  getCost()        const override { return cost; }
    string getDescription() const override { return description; }
};


// Decorator class
class Decorator : public Beverage
{
public:
    Decorator(Beverage* drink) : drink_(drink) {};
    ~Decorator() {};

    // delegate as much as possible to the wrapped components
    float       getCost()        const override { return this->drink_->getCost(); }
    std::string getDescription() const override { return this->drink_->getDescription(); }

protected:
    Beverage* drink_;
};


// Concrete decorator
class Mocha : public Decorator
{
public:
    Mocha(Beverage* beverage) : Decorator(beverage) {};
    ~Mocha() override {};

    float getCost()         const override { return 1.00 + Decorator::getCost(); };
    string getDescription() const override { return "Mocha " + Decorator::getDescription(); };
};



int main()
{
    Beverage* first_drink = new Espresso();
    cout  << first_drink->getDescription() << endl;
    Beverage* second_drink = new Mocha(first_drink);
    cout << second_drink->getDescription() << endl;


    delete first_drink;
    delete second_drink;

    return 0;
}
