#include<iostream>
using namespace std;
int main(){
	int a;
	cin>>a;
	bool b;
	b=a>99 and a<1000 and a/100!=(a-(a/100)*100)/10 and (a-(a/100)*100)/10!=a%10 and a/100!=a%10;
	cout<<b<<endl;
	return 0;
}
