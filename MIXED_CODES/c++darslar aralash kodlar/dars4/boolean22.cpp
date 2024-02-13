#include<iostream>
using namespace std;
int main(){
	int a;
	cin>>a;
	bool result;
	result= a>99 && a<1000 && a/100==a%10;
	cout<<result;
	return 0;
}

