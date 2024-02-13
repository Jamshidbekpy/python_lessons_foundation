#include<iostream>
#include<cmath>
using namespace std;

int main(){
	int yosh;
qaytish:
cin >> yosh;
bool a;
a = (yosh > 19 && yosh<70);
switch (a) {
case 0:cout << "Yoshni xato kirittingiz qayta kiriting: "<<endl; goto qaytish;
case 1: 
    switch (yosh / 10) {
    case 2:cout << "Yigirma "; break;
    case 3:cout << "Ottiz "; break;
    case 4:cout << "Qirq "; break;
    case 5:cout << "Ellik "; break;
    case 6:cout << "Oltmish "; break;
    }
    switch (yosh % 10) {
    case 1:cout << "bir "; break;
    case 2:cout << "ikki "; break;
    case 3:cout << "uch "; break;
    case 4:cout << "tort "; break;
    case 5:cout << "besh "; break;
    case 6:cout << "olti "; break;
    case 7:cout << "yetti "; break;
    case 8:cout << "sakkiz "; break;
    case 9:cout << "toqqiz "; break;
       
    }


}
	return 0;
}
