#include <iostream>

int main() {
    int start, end;
    std::cin >> start >> end;
    
    int current = start;
    while (current <= end) {
        std::cout << current << std::endl;
        ++current;
    }

    return 0;
}

