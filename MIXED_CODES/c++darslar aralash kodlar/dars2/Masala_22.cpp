#include<iostream>
using namespace std;
int main(){
	int A,B;
	cin>>A>>B;
	cout<<"Berilgan:";
	cout<<A<<" "<<B<<endl;
	int c=A;
	A=B;
	B=c;
	cout<<"O'zgartirildi:"<<endl;
	cout<<A<<" "<<B;
	return 0;
}

