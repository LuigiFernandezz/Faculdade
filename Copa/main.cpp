#include <iostream>
#include <stdlib.h>
#include <time.h>
#include <locale.h>

using namespace std;


///STRUCTS
struct Grupo{
    string times[4], nome;
};

struct Time{
    string nome;
    int pote, forca, pontos=0;
};

struct Jogo{
    string times[2];
    int gols1, gols2, resultado;
};

struct Copa{
    string times[32] = {"Alemanha","Arábia Saudita","Argentina","Austrália","Bélgica","Brasil","Camarões","Canadá","Catar","Coreia do Sul","Costa Rica","Croácia","Dinamarca","Equador","Espanha","Estados Unidos","França","Gana","Holanda","Inglaterra","Irã","Japão","Marrocos","México","País de Gales","Polônia","Portugal","Senegal","Sérvia","Suíça","Tunísia","Uruguai"};;
    char grupos[8] = {'A','B','C','D','E','F','G','H'};

};

///FUNÇÕES

void SortearGrupos(Copa copa){
    Grupo grupo;

    for(int i=0; i<8;i++){
        grupo.nome = copa.grupos[i];
        cout<<endl<<grupo.nome<<endl;

        for(int j=0; j<4; j++){
            int numTime;
            do{
                numTime = rand()%32;
            }while(copa.times[numTime] == "escolhido");
            grupo.times[j] = copa.times[numTime];
            copa.times[numTime]= "escolhido";
            cout<<grupo.times[j]<<endl;
        }
    }
}


int main()
{
    setlocale(LC_ALL,"Portuguese");
    //semente randômica
    srand(time(NULL));

    ///INICIALIZAÇÃO DA VARIÁVEL INICIAL DO TIPO COPA
    Copa padrao;

    SortearGrupos(padrao);

    return 0;
}
