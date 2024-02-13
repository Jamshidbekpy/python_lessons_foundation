#include<iostream>
using namespace std;
int main(){
	int a,b;
	cin>>a>>b;
	a==b=false;
	for(a;a==true;a++){
		b+=a;
	}
	cout<<b;
}