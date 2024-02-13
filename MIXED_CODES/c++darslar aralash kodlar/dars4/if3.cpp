#include<iostream>
#include<cmath>
using namespace std;
int main(){
	int a;
	cin>>a;
	cout<<"a ning dastlabki qiymati:"<<a<<endl;
	if(a>0){
		a++;	
	}
	else 
	    if(a<0){
	    	a=a-2;
		}
	else 
		a=10;
		
	cout<<"a ning keyingi qiymati:"<<a;
	
	return 0;
}
