#include<iostream>
#include<cmath>
using namespace std;
int main(){
  float a,b,c,s;
  cin>>a>>b>>c;
  s=b;
  b=a;
  a=c;
  c=s;
  cout<<a<<" "<<b<<" "<<c;
    return 0;
}
