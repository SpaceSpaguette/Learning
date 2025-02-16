#include <iostream>
using namespace std;

#define RED "\e[0;32m"
#define WHITE "\e[0;33m"
#define RESET "\033[0m"

int main() {
    int row = 0;
    int coll = 0;
    for(int row = 0;row<5;row++) {
        for(int coll = 0;coll <10;coll++) {
            if(row%2==0) {
                if(coll%2==0) {
                    cout << RED << "X";
                }
                else {
                    cout << WHITE<< "O";
                }
            }
            else {
                if(coll%2==0) {
                    cout << WHITE << "O";
                }
                else {
                    cout << RED << "X";
            }
        }
    } // coll Bracket
    cout << "\n";
} //Row Bracket
    cout << RESET << "\n";
    return 0;
} //Ending Bracket
