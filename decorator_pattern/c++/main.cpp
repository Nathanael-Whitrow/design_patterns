#include <iostream>
#include <memory>
#include <string>

using namespace std;

// Abstract base class
// Don't store description in here, leave it as an interface
// Pure virtual makes interface easier to read
class Beverage {
public:
    virtual ~Beverage() = default; // destructor
    virtual double getCost() const = 0; // =0; makes this pure virtual
    virtual string getDescription() const = 0;
};

// Concrete implementations
class Espresso : public Beverage {
public:
    double getCost() const override { return 2.99; }
    string getDescription() const override { return "Espresso"; }
};

class HouseBlend : public Beverage {
public:
    double getCost() const override { return 3.50; }
    string getDescription() const override { return "House blend coffee"; }
};

// Abstract Decorator class
// Because the decorator class is so similar to beverage, it could be replaced
// with using CondimentDecorator = beverage; then have each of the decorator
// implementations hold a unique_ptr to a Beverage
class CondimentDecorator : public Beverage {
public:
    // Explicitely take ownership of the pointer we are handed
    CondimentDecorator(unique_ptr<Beverage> drink)
        : drink_ { move(drink) } {};

    double getCost() const override { return this->drink_->getCost(); }
    std::string getDescription() const override
    {
        return this->drink_->getDescription();
    }

protected:
    // Smart pointers mean no memory leaks, and, *apparently*, better
    // representation of memory ownership
    unique_ptr<Beverage> drink_;
};

// Concrete decorators
class Mocha : public CondimentDecorator {
public:
    Mocha(unique_ptr<Beverage> beverage)
        : CondimentDecorator { move(beverage) } {};
    double getCost() const override
    {
        return 1.00 + CondimentDecorator::getCost();
    };
    string getDescription() const override
    {
        return "Mocha " + CondimentDecorator::getDescription();
    };
};

class Whip : public CondimentDecorator {
public:
    Whip(unique_ptr<Beverage> beverage)
        : CondimentDecorator { move(beverage) } {};
    double getCost() const override
    {
        return 0.50 + CondimentDecorator::getCost();
    };
    string getDescription() const override
    {
        return "Whip " + CondimentDecorator::getDescription();
    };
};

// Decorator that doesn't use an abstract decorator class
class Latte : public Beverage {
public:
    Latte(unique_ptr<Beverage> drink)
        : drink_ { move(drink) } {};

    double getCost() const override { return this->drink_->getCost() + 2.00; }
    string getDescription() const override
    {
        return this->drink_->getDescription() + " with latte milk ";
    }

protected:
    unique_ptr<Beverage> drink_;
};

int main()
{
    const Beverage& beverage1 = Espresso {};
    cout << "ordering one " << beverage1.getDescription() << " for $"
         << beverage1.getCost() << endl;

    // Using smart pointers
    unique_ptr<Beverage> beverage2 {
        make_unique<HouseBlend>()
    }; // brace initialise
    cout << "ordering one " << beverage2->getDescription() << " for $"
         << beverage2->getCost() << endl;

    // Decorating
    // hand the unique pointer to the constructor, receive the new pointer and
    // assign to beverage2. move() enforces make_unique<Mocha> to use a move
    // constructor and not a copy constructor.
    beverage2 = make_unique<Mocha>(
        move(beverage2)); // assignment used to overwrite existing value
    cout << "ordering one " << beverage2->getDescription() << " for $"
         << beverage2->getCost() << endl;

    // trying out the Latte decorator
    unique_ptr<Beverage> beverage3 { make_unique<Espresso>() };
    beverage3 = make_unique<Latte>(move(beverage3));
    cout << "ordering one " << beverage3->getDescription() << " for $" << beverage3->getCost() << endl;

    return 0;
}
