#ifndef DOG_HPP
#define DOG_HPP

//#include "BarkInterface.hpp"
#include "Animal.hpp"

class Dog : public Animal
{
public:
	void makeNoise() override;
	//BarkInterface barker;

};

#endif