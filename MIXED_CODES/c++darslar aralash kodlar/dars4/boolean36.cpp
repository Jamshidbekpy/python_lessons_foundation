#include<iostream>
using namespace std;
int main(){
	
	int x1,y1,x2,y2;
	cin>>x1>>y1>>x2>>y2;
	bool result1,result2,result3=0;
	result1=x1>0 && x2>0 and x1<9 and x2<9 and y1>0 and y2>0 and y1<9 and y2<9;
    result2=((x1+y1)%2) ^ ((x1+y1)%2);
    cout<<result2;
	cout<<result3;
	return 0;
	
}

