//Dinamik massivni teskari tartibda chiqarish
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
	}
	for( size=size-1; size>=0;size--){
		cout<<"arr["<<size<<"]="<<x[size]<<endl;
	}
	
	delete [] x;
	
	return 0;
}