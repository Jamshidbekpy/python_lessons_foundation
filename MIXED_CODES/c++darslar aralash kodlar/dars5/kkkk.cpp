#include<iostream>
#include<cmath>
using namespace std;

int main(){
	float a,b,c;
	cin>>a>>b;
	if(a!=b){
		if(a>b){
			c=a; //a
			a=b;
			b=c;
			cout<<a<<" "<<b;
		}
		else
			cout<<a<<" "<<b;
		
			
						
	}
	return 0;
}
