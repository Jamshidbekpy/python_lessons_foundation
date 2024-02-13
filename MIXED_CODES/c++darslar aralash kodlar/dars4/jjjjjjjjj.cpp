#include<iostream>
#include<cmath>
using namespace std;

int main(){
	int n,m,count=0;
	qaytish1:
	cin>>n;
	if(count==0){
		qaytish2:
		cin>>m;	
	}
	count++;
	switch(n){
		case 6:cout<<"Olti ";break;
		case 11:cout<<"Valet ";break;
		case 12:cout<<"Dama ";break;
		case 13:cout<<"Karol ";break;
		case 14:cout<<"Tuz ";break;
		default:cout<<"n ni xato kiritdingiz!";goto qaytish1;
	}
		
	switch(m){
		case 1:cout<<"gisht";break;
		case 2:cout<<"olma";break;
		case 3:cout<<"chillik";break;
		case 4:cout<<"qarga";break;
		default:cout<<"m ni xato kiritdingiz!";goto qaytish2;
	}
	return 0;
}
