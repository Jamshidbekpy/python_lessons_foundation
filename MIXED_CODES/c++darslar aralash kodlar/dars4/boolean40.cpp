#include<iostream>
#include<cmath>
using namespace std;
int main(){
	int x1,x2,y1,y2;
	cin>>x1>>x2>>y1>>y2;
	bool result1,result2,result3;
	result1=x1>0 and x1<9 and x2>0 and x2<9 and y1>0 and y1<9 and y2>0 and y2<9 and abs(x1-x2)+abs(y1-y2)>0;
	result2=((x2==x1+1 or x2==x1-1) and (y2==y1+2 or y2==y1-2)) or ((x2==x1+2 or x2==x1-2) and (y2==y1+1 or y2==y1-1));
	result3=result1==1 and result2==1;
	cout<<result3;
	return 0;
}

