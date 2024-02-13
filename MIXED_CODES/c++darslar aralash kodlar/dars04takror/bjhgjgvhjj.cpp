#include<iostream>
#include<stdlib.h>
#include<time.h>
using namespace std;

void tekshir(int matritsa[][100], int n) {
    cout << "Matritsaning monoton satrlari: ";
    for (int i = 0; i < n; ++i) { 
        bool omon = true; 
        bool kmon = true;
        
        for (int j = 1; j < n; ++j) {
            if (matritsa[i][j] <= matritsa[i][j - 1]) 
                omon = false;
            if (matritsa[i][j] >= matritsa[i][j - 1]) 
                kmon = false;
        }
        
        if (omon)
            cout << i + 1 << " - o'suvchi ";
        else if (kmon)
            cout << i + 1 << " - kamayuvchi ";
    }
    cout << endl;
}

int main() {
	srand(time(NULL));
    int n;
    cout << "Matritsa o'lchamini kiriting: ";
    cin >> n;

    int matritsa[100][100];
    cout << "Matritsani elementlar bilan to'ldirish:\n";
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            matritsa[i][j]=rand()%100+1;
        }
    }

    tekshir(matritsa, n);

    return 0;
}
