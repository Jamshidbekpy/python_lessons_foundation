#include <iostream>

using namespace std;

int main(){
                           // 9-mavzu 9-masala
    int a,b,c;
    
    cout<<"birinchi a="; cin>>a;
    cout<<"ikkinchi b="; cin>>b;
    cout<<"uchinchi c="; cin>>c;
    
    if(a!=b&&b==c or a==b and b!=c or a==c and c!=b or a==b and b==c)
        
        cout<<"Hech bo'lmaganda ikkitasi bir biriga teng!"<<endl;
    
    else{
        cout<<"Har xil raqamli!"<<endl;
    }
    
    main();
    return 0;
    }