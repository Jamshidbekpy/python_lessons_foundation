#include<iostream>
#include<cmath>
using namespace std;
void mean(float a,float b,float c,float d){
	cout<<"Arifmetik(a,b)="<<(a+b)/2<<endl<<"Geometrik(a,b)="<<sqrt(a*b)<<endl;
	cout<<"Arifmetik(a,c)="<<(a+c)/2<<endl<<"Geometrik(a,c)="<<sqrt(a*c)<<endl;
	cout<<"Arifmetik(a,d)="<<(a+d)/2<<endl<<"Geometrik(a,d)="<<sqrt(a*d)<<endl;
	
}
int main(){
	mean(2,3,4,5);
	return 0;
}