#include <iostream>
using namespace std;

int main() {
    int n = 8;
    int a[] = {3, 10, -8, 7, -6, 16, 13, 20};

    int birinchiManfiy = 0;
    int yigindi = 0;

    for (int j = 0; j < n; ++j) {
        if (a[j] < 0) {
            birinchiManfiy = a[j];
            break;
        }
    }

    for (int j = 0; j < n; ++j) {
        yigindi += a[j];
        if (a[j] == birinchiManfiy) {
            break;
        }
    }

    cout << "Birinchi manfiy element: " << birinchiManfiy << endl;
    cout << "Birinchi manfiy elementgacha bo'lgan elementlarning yig'indisi: " << yigindi << endl;

    return 0;
}
