#include <iostream>

int main() {
    int prev = 0, current = 0; 
    int number = 0;

    if (std::cin >> current) {
        prev = current;
        number = 1; 
        while (std::cin >> current) {
            if (current == prev) {
                number += 1;
            } else {
                std::cout << "Number: " << prev << " -> " << number << std::endl;
                number = 1;
            }
            prev = current;
        }
    }
    return 0;
}

