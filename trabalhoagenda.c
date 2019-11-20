#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int contadorGlobal = 0;
typedef struct agenda{
    char *nome;
    char telefone[15];
    char *endereco;
    char *cidade;
    char estado[4];
    int dia;
    int mes;
    int ano;
}agenda;

agenda contatos[100];


agenda cadastro(){
    
    char *ptr1=NULL;
    char *ptr2=NULL;
    char *ptr3=NULL;
    agenda novo;
    char aux1[100];
    char aux2[100];
    char aux3[100];

    fflush(stdin);
    printf("\n\n");
    printf("Digite o nome: ");
    getchar();fflush(stdin);
    fgets(aux1,100,stdin);
    contatos[contadorGlobal].nome=(char*)malloc(strlen(aux1)*sizeof(char));
    for(int i=0; i<strlen(aux1); i++){
        contatos[contadorGlobal].nome[i]=aux1[i];
    }

    printf("\n\n");
    printf("Digite o telefone: ");
    fflush(stdin);
    fgets(contatos[contadorGlobal].telefone,15,stdin);

  

    printf("\n\n");
    printf("Digite o endereco: ");
    fflush(stdin);
    fgets(aux2,100,stdin);
    contatos[contadorGlobal].endereco=(char*)malloc(strlen(aux2)*sizeof(char));
    for(int i=0; i<strlen(aux2); i++){
        contatos[contadorGlobal].endereco[i]=aux2[i];
    }
    
    

    printf("\n\n");
    printf("Digite o cidade: ");
    fflush(stdin);
    fgets(aux3,100,stdin);
    contatos[contadorGlobal].cidade=(char*)malloc(strlen(aux3)*sizeof(char));
    for(int i=0; i<strlen(aux3); i++){
        contatos[contadorGlobal].cidade[i]=aux3[i];
    }
    printf("\n\n");
    printf("Digite o estado(sigla): ");
    fflush(stdin);
    fgets(contatos[contadorGlobal].estado,4,stdin);
   

    printf("\n\n");
    printf("Digite o dia de nascimento(dd mm aaaa separado por espaco): ");
    
    scanf("%d %d %d",&contatos[contadorGlobal].dia,&contatos[contadorGlobal].mes,&contatos[contadorGlobal].ano);

}

int pesquisar(){
    char nome[100];
    char* ptr;
    int x;
    int result;
    getchar();fflush(stdin);

    printf("\n\nDigite o nome do contato: ");
    fgets(nome,99,stdin);
    for(int i=0; i<100;i++){
        x = strcmp(contatos[i].nome,nome);
        
        if (x == 0){
            printf("\nNome: %s",contatos[i].nome);
            printf("\nTelefone: %s",contatos[i].telefone);
            printf("\nEnderco: %s",contatos[i].endereco);
            printf("\nCidade: %s",contatos[i].cidade);
            printf("\nEstado: %s",contatos[i].estado);
            printf("\nNascimento: %d/%d/%d",contatos[i].dia,contatos[i].mes,contatos[i].ano);
            result=i;
            break;
        }
    }
    if (x != 0){
        printf("\nContato nao encontrado\n");
        result=111;
    }
    return result;
}

agenda modificar(){
    int indice;
    printf("Modificação de contato");
    indice = pesquisar();
    
    if (indice!=111){
        contatos[indice]=cadastro();
    }

}



void showAll(){
    char nomes[100];
    for(int i=0; i<=contadorGlobal;i++){
        printf("%c\n",*(contatos[i].nome));
    }
    printf("Para mais detalhes sobre o contato selecione a opcao 2.\n");

}

void menu () {
    printf("\nEscolha uma das opções abaixo:\n");
    printf("1 - Cadastrar contato\n");
    printf("2 - Buscar contato\n");
    printf("3 - Editar contato\n");
    printf("4 - Mostrar todos os contatos\n");
    printf("0 - Sair\n\n");
}

int main(){
    int action;
    menu();
    scanf("%d",&action);
    while(action != 0) {
        
        if(action==1){
            if(contadorGlobal<100){
                cadastro();
                contadorGlobal++;


            }
        }
        if(action==2){
            pesquisar();
        }
        if(action==3){
            modificar();
        }
        if(action==4){
            showAll();
        }
        menu();
        scanf("%d",&action);
        
    }
}   