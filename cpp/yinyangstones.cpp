#include <iostream>
using namespace std;

int main()
{
    string stones;
    int w = 0, b = 0;
    getline(cin, stones);
    for (int i = 0; i < stones.length(); i++) {
        if (stones[i] == 'W') {
            w++;
        } else {
            b++;
        }
    }
    cout << (w == b) << endl;
    return 0;
}