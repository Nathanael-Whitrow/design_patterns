#ifndef DOG_CPP
#define DOG_CPP

#include "Dog.hpp"
#include <iostream>

/*
Dog::Dog()
{
	Dog::barker = new Bark();
}
*/
void Dog::makeNoise()
{
	//barker.bark();
	std::cout << "Woof!" << std::endl;
	return;
}


#endif