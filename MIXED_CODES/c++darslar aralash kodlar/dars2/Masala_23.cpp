#include<iostream>
using namespace std;
int main(){
	int k;
	cin>>k;
	int c=k%7;
		switch(c){
			case 0:cout<<"Y";break;
			case 1:cout<<"D";break;
			case 2:cout<<"S";break;
			case 3:cout<<"CH";break;
			case 4:cout<<"P";break;
			case 5:cout<<"J";break;
			case 6:cout<<"SH";break;
			default:cerr<<"ERROR";
		}
		
		return 0;
			
}

