#include <iostream>
#include <iomanip>
#include <math.h>

using namespace std;

int main(){
    double sum=0, had=0, n;
    cin >> n;  
    for(double i=1,j=1.1; j<=n/10+1+0.1; j+=0.1,i++){
        had=(pow((-1),(i+1))*j);
        sum=sum+had;
        cout <<"("  << had << ")" << " + ";
    }
    cout << " = " << sum << endl;
    cout << "sum = " << sum;
    
    return 0;
}