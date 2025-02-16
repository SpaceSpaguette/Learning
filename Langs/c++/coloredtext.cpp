#include <iostream>

#define RED "\033[31m"
#define GREEN "\033[32m"
#define RESET "\033[0m"

int main() {
    std::cout << RED << "This is red text!" << RESET << std::endl;
    std::cout << GREEN << "This is green text!" << RESET << std::endl;
    return 0;
}
