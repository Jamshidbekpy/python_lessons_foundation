#include <iostream>
using namespace std;

// Funksiya prototiplari
void recursion1(int n);
void recursion2(int n);

void recursion1(int n) {
    if (n == 0)                                    
        return;  
		                                  
    cout << n << " ";     //4 2        1 3 5
	                 
    recursion2(n - 1);                             
}

void recursion2(int n) {                         
    if (n == 0) 
        return;
    recursion1(n - 1);    // 5 3 1
    cout << n << " ";
}

int main() {
    recursion2(5);  // << Bu qatorni o'zgartirish kerak
    return 0;
}
