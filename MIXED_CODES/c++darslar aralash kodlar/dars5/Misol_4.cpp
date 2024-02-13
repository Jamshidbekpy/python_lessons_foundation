//Dinamik massivni elementlarini p ta pozitsiya chapga surish
#include<iostream>
#include<stdlib.h>
#include<time.h>

using namespace std;

int main(){
	srand(time(0));
	int size;
	cout<<"Size=";
	cin>>size;
	float *x=new float[size];
	
	for(int i=0;i<size;i++){
		x[i]=(rand()%1000+1)/10.0;
		cout<<"x["<<i<<"]="<<x[i]<<endl;
	}
	int p;
	cout<<endl<<"p=";cin>>p;
	
	float *y=new float[size];
	
	for(int i=0;i<size;i++){
		if(i-p<0)
			y[i]=x[i-p+size];
		
		else 
		   y[i]=x[i-p];
	}
	
	for(int i=0;i<size;i++)
		x[i]=y[i];
	
	delete [] y;
	
	cout<<endl<<endl;
	
		for(int i=0;i<size;i++)
		cout<<"x["<<i<<"]="<<x[i]<<endl;
	
	
	delete [] x;
	return 0;
}