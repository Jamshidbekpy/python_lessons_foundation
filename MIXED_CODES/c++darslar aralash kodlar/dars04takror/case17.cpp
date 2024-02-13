#include<iostream>
#include<cmath>
using namespace std;

int main(){
	int num;
	cout<<"Sonni kiriting(raqam):";
	qaytish:
	cin>>num;
	bool result=num>9 and num<41;
	switch(result){
		case 0:
			cout<<"To'gri oraliqda kiritmadiz!(qayta kiriting):"<<endl;
			goto qaytish;
		case 1:
			switch(num/10){
				case 1:cout<<"O'n ";break;
				case 2:cout<<"Yigirma ";break;
				case 3:cout<<"O'ttiz ";break;
				case 4:cout<<"Qirq ";break;
	}
		switch(num%10){
			case 1:cout<<"bir ";break;
			case 2:cout<<"ikki ";break;
			case 3:cout<<"uch ";break;
			case 4:cout<<"to'rt ";break;
			case 5:cout<<"besh ";break;
			case 6:cout<<"olti ";break;
			case 7:cout<<"yetti ";break;
			case 8:cout<<"sakkiz ";break;
			case 9:cout<<"to'qqiz ";break;
	}
			
	}
	
	
	cout<<"masala";
	return 0;
}