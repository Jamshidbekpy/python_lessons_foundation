#include<iostream>
#include<cmath>
using namespace std;
int main(){
	int n;
	qaytish:
	cin>>n;
	switch(n){
		case 1:
		    {
			int R;
			cin>>R;
		    int D=2*R;
		    float L=2*M_PI*R;
		    float S=M_PI*R*R;
		    cout<<D<<" "<<L<<" "<<S;
			break;
			}
		case 2:
			{
			int D;
			cin>>D;
		    int R=D/2;
		    float L=2*M_PI*R;
		    float S=M_PI*R*R;
		    cout<<R<<" "<<L<<" "<<S;
			break;
			}
		case 3:
			{
			
			float L;
			cin>>L;
		    int R=round(L/(2*M_PI));
		    int D=2*R;
		    float S=M_PI*R*R;
		    cout<<R<<" "<<D<<" "<<S;
			break;
			}
		case 4:
			{
			float S;
			cin>>S;
		    int R=round(sqrt(S/M_PI));
		    int D=2*R;
		    float L=2*M_PI*R;
		    cout<<R<<" "<<D<<" "<<L;
			break;
		    }
		default:
			cout<<"Berilgan parametr tartib raqamini xato kiritdingiz (qayta kiriting):";goto qaytish;
			
	}
	return 0;
}
