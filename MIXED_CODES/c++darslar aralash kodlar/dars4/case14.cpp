#include<iostream>
#include<cmath>
using namespace std;
//class Myclass{
//    public:
//   protected:
//   private:
//}
//int myfunc(){

//}
int main(){
	int n;
	qaytish:
	cin>>n;
	
	switch(n){
	int a;
	float r1,r2,s;
		case 1:
			cin>>a;
			r1=a*sqrt(3)/6;
			r2=2*r1;
			s=a*sqrt(3)/4;
			cout<<r1<<" "<<r2<<" "<<s;break;
		case 2:
			cin>>r1;
			a=round(r1*6/sqrt(3));
			r2=2*r1;
			s=a*sqrt(3)/4;
			cout<<a<<" "<<r2<<" "<<s;break;
		case 3:
			cin>>r2;
			r1=r2/2;
			a=round(r1*6/sqrt(3));
			s=a*sqrt(3)/4;
			cout<<a<<" "<<r1<<" "<<s;break;
		case 4:
			cin>>s;
			a=round(4*s/sqrt(3));
			r1=a*sqrt(3)/6;
			r2=2*r1;
			cout<<a<<" "<<r1<<" "<<r2;break;
		default:
			cout<<"Berilgan parametr raqamini to'g'ri kiriting:"<<endl;goto qaytish;	
	}
		
	return 0;                                                   ;              
			
				
		
}
