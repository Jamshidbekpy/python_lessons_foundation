#include<iostream>
using namespace std;
int main(){
	int x1,y1,x2,y2;
	cin>>x1>>y1>>x2>>y2;
	bool result;
	result=x1>0 and x2>0 and x1<9 and x2<9 and y1>0 and y2>0 and y1<9 and y2<9 and (x1+y1)%2==1 and (x2+y2)%2==1 or x1>0 && x2>0 and x1<9 and x2<9 and y1>0 and y2>0 and y1<9 and y2<9 and (x1+y1)%2==0 and (x2+y2)%2==0;

	cout<<result;
	return 0;
}


