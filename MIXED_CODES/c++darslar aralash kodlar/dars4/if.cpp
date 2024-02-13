#include<iostream>
#include<cmath>
using namespace std;

int main(){
	int count1=0,count2=0,a,b=0;
	qaytish:
	if(b!=3){
		cin>>a;
		if(a>0)
	 		count1++;
		if(a<0)
			count2++;
		b++;
		goto qaytish;
	}
	    
	cout<<count1<<" "<<count2;
	return 0;
	
	}
