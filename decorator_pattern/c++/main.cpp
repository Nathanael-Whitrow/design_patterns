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

    // pure virtual makes this class abstract
    virtual float  getCost()        const = 0;
    virtual string getDescription() const = 0;

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
    unique_ptr<Beverage> first_drink = make_unique<Espresso>();
    cout << "ordering one " << first_drink->getDescription() << " for " << first_drink->getCost() << endl;

    unique_ptr<Beverage> second_drink = make_unique<Mocha>(first_drink.get());
    cout << "Making it a " << second_drink->getDescription() << " for " << second_drink->getCost() << endl;

    return 0;
}
