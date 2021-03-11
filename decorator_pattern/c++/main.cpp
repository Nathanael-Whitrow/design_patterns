#include <string>
#include <iostream>

using namespace std;

class beverage
{
public:
    beverage() {}
    string getDescription() { return beverage; }

private:
    string beverage = "unknown beverage";
};

int main(int argc, char* argv[])
{

    cout << "hello world!" << endl;

    return 0;
}