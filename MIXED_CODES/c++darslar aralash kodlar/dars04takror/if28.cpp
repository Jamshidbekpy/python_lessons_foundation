#include<iostream>
#include<cmath>
using namespace std;

int main(){
	int year;
	cin>>year;
	if(year%4==0){
		cout<<"Ushbu yilda 366 kun mavjud!"<<endl;
	}
	if(year%400==0){
		cout<<"Hamda bu yil kabisa yili!";
	}
	else if(year%4!=0)
		cout<<"Ushbu yillarda 365 kun mavjud!";
	return 0;
}
