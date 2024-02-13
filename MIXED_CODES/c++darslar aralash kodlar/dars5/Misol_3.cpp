//Dinamik massivda berilgan indexdagi qiymatni topish
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
	int index;
	cout<<"index=";cin>>index;
	if(index>=0 and index<size){
		if(index==0)
		cout<<x[0];
	else if(index==size-1)
		cout<<x[size-1];
	else
		cout<<"*x ning "<<index<<"-indeksdagi element qiymati:"<<(x[index-1]+x[index]+x[index+1])/3.0;	
	}
	else 
		cout<<"Indexni xato kiritdingiz!";
	
	delete [] x;
	
	
	return 0;
}