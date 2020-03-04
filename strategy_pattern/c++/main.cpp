#ifndef MAIN_CPP
#define MAIN_CPP

#include "Dog.hpp"
#include <iostream>

int main()
{
	Dog* socks = new Dog();
	socks->makeNoise();
	return 0;
}

#endif