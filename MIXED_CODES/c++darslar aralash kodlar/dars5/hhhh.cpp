#include<iostream>
using namespace std;

int main(){
	float sum=0;
	int n;
	cin>>n;    
	   
	float oxirgi_toq=(n%2+n%2/10.0)+(n%2*(n/2))*0.2;
	
	for( n=n/2;   n>0   ;n--){  
		sum+=-0.1;
	}
	sum+=oxirgi_toq;
	cout<<sum;
	return 0;
}
