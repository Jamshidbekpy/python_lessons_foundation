#include<iostream>
using namespace std;
int main(){
	int A , a,b,c;
  bool x;
  cin >> A;
  a=A/100;
  b=A/10%10;
  c=A%10;
  cout << a ;
  cout << b ;
  cout << c << endl;
  x= A>=100 && A<1000 && a<=b && b<=c && a<=c;
  cout << x << endl;
  
    return main();
}

