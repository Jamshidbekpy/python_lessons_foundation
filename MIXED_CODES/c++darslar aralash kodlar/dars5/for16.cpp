#include<iostream>
#include<cmath>
using namespace std;

int main(){
	int n;
	float daraja,a;
	cin>>n>>a;
	for(;n>0;n--){
		daraja=pow(a,n);
		cout<<daraja<<endl;
	}
	return 0;
}
