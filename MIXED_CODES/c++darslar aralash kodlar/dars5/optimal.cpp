#include <iostream>
#include <string>
using namespace std;

class Kinofilm {
protected:
    string nomlanishi;
    string rejessor;
    int davomiyligi;
    int aktyorlarSoni;

public:
    Kinofilm(const string& nom, const string& rej, int dav, int akt) :
        nomlanishi(nom), rejessor(rej), davomiyligi(dav), aktyorlarSoni(akt) {}

    virtual int Narx() const {
        if (rejessor == "Stiven Spilberg" || rejessor == "Djeyms Kemeron") {
            return davomiyligi * 20 + aktyorlarSoni * 30;
        } else {
            return davomiyligi * 20 + aktyorlarSoni * 30;
        }
    }

    void Axborot() const {
        cout << "Film haqida ma'lumotlar:\n";
        cout << "Nomlanishi: " << nomlanishi << endl;
        cout << "Rejessor: " << rejessor << endl;
        cout << "Davomiyligi: " << davomiyligi << " minut" << endl;
        cout << "Aktyorlar soni: " << aktyorlarSoni << endl;
        cout << "Narxi: " << Narx() << " so'm" << endl;
    }
};

class Multifilm : public Kinofilm {
public:
    Multifilm(const string& nom, const string& rej, int dav, int akt) :
        Kinofilm(nom, rej, dav, akt) {}

    int Narx() const override {
        return davomiyligi * 25 + aktyorlarSoni * 10;
    }
};

int main() {
    Kinofilm kinofilm1("Titanik", "Stiven Spilberg", 180, 5);

    Kinofilm kinofilm2("Avatar", "Jorj Gofman", 160, 7);

    Multifilm multifilm("Shrek", "Andrew Adamson", 90, 4);

    cout << "1. Kinofilm:\n";
    kinofilm1.Axborot();
    cout << endl;

    cout << "2. Kinofilm:\n";
    kinofilm2.Axborot();
    cout << endl;

    cout << "Multifilm:\n";
    multifilm.Axborot();

    return 0;
}
