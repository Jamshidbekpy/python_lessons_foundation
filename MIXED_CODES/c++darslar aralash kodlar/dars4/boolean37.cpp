#include<iostream>
using namespace std;
int main(){
  int x,y,x1,y1;
  cin>>x1>>y1>>x>>y;
  bool result;
  result = x>=1 && y>=1 && x<=8 && y<=8 && x1>=1 && y1>=1 && x1<=8 && y1<=8 && abs(x-x1)<2 && abs(y-y1)<2 && abs(x-x1)+abs(y-y1)>0;
  cout<<result;
  return 0;
}

