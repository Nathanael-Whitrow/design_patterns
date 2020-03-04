#ifndef BARK_CPP
#define BARK_CPP

#include "BarkInterface.hpp"
#include <iostream>

class Bark : public BarkInterface
{
public:
	void bark()
	{
		std::cout << "Woof!!" << std::endl;
	}
};

#endif