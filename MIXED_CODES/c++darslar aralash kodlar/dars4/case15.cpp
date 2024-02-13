#include<iostream>
using namespace std;

int main(){
	int n,m,count=0;			//count {goto qaytish1} ni sanash uchun.
	cout<<"n -kiriting:";		
	if(count>0){
		qaytish1:
		cin>>n;                //count>0 hol uchun faqat n ni kiritish zarurdir. m count=0 da kiritilib bo'lingan
							  //Agar result2=0 bo'lib count>0 bo'lsa,else dagi {qaytish2} bosqichiga o'tadi.
	}
	else{
		cin>>n;
		cout<<"m-ni kiriting:";
		qaytish2:
		cin>>m;	              //count=0 bo'lgandagina m ni so'raydi.Chunki,result2=1 shart qanoatlanganda,qayta m so'ralmaydi!
	} 
	count++;
	bool result1,result2;
	result1=n>0 and n<5;
	result2=m<=10 and m>=6;	  //Tanlashning aniqlanish sohasi
	
	
	cout<<"Natija:"<<endl;
		
	switch(result1){ 
	//result1=1 bo'lsa, m ni tanlash huquqi mavjud.result1=0 da ni kiritish bosqichiga qaytish kerak.
		case 0:
			cout<<"n-ni xato kiritdingiz!(Qayta kiriting):"<<endl;goto qaytish1;
		case 1:
			switch(result2){
				case 0:
			    	switch(m){
						case 11:
							cout<<"Valet ";break;
						case 12:
							cout<<"Dama ";break;
						case 13:
							cout<<"Karol ";break;
						case 14:
							cout<<"Tuz " ;break;
						default:
							cout<<"m ni xato kiritdingiz!(Qayta kiriting):"<<endl;goto qaytish2;
			}
			break;
		         case 1:
			           cout<<m<<" ";break;
				}
			
		}
	switch(n){
		case 1:cout<<"g'isht'";break;
		case 2:cout<<"olma";break;
		case 3:cout<<"chillak";break;
		case 4:cout<<"qarg'a";break;
	}
	return 0;
}
