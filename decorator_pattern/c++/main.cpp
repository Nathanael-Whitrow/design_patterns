#include <iostream>
#include <string>

using namespace std;

class beverage
{
public:
    beverage() {}
    ~beverage() {};

    string getDescription() { return drink; }

private:
    string drink = "unknown beverage";
};

int main()
{
    beverage first_drink;
    cout << "hello world!" << endl;
    cout  << first_drink.getDescription() << endl;

    return 0;
}
