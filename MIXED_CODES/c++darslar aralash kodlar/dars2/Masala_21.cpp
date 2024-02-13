#include<iostream>
#include<cmath>
using namespace std;
int main(){
	float x1,y1,x2,y2,x3,y3;
	cin>>x1>>y1>>x2>>y2>>x3>>y3;
	
	if(fabs(x2-x1)>fabs(y2-y1)&&fabs(x3-x1)>fabs(y3-y1)&&fabs(x2-x3)>fabs(y2-y3)){
		
			float a=sqrt(pow((x2-x1),2)-pow((y2-y1),2));
			
			float b=sqrt(pow((x3-x2),2)-pow((y3-y2),2));
			
			float c=sqrt(pow((x3-x1),2)-pow((y3-y1),2));
			
			if(a<b+c&&b<a+c&&c<a+b){
				float p=(a+b+c)/2;
	  		  	float S=sqrt(p*(p-a)*(p-b)*(p-c));
     			cout<<p<<" "<<S;
		}
			else cerr<<"ERROR!";
	
	
	
	}
	else cerr<<"ERROR!";
	
	return 0;
	}
	

