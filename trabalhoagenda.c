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
    char aux1[100];
    char aux2[100];
    char aux3[100];

    fflush(stdin);
    printf("\n\n");
    printf("Digite o nome: ");
    getchar();fflush(stdin);
    fgets(aux1,100,stdin);
    contatos[contadorGlobal].nome=(char*)malloc(strlen(aux1)*sizeof(char));
    strcpy(contatos[contadorGlobal].nome,aux1);
   

    printf("\n\n");
    printf("Digite o telefone: ");
    fflush(stdin);
    fgets(contatos[contadorGlobal].telefone,15,stdin);

  

    printf("\n\n");
    printf("Digite o endereco: ");
    fflush(stdin);
    fgets(aux2,100,stdin);
    contatos[contadorGlobal].endereco=(char*)malloc(strlen(aux2)*sizeof(char));

    strcpy(contatos[contadorGlobal].endereco,aux2);
    
    
    

    printf("\n\n");
    printf("Digite o cidade: ");
    fflush(stdin);
    fgets(aux3,100,stdin);
    contatos[contadorGlobal].cidade=(char*)malloc(strlen(aux3)*sizeof(char));
    strcpy(contatos[contadorGlobal].cidade,aux3);
    
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
    char comp[100];
    int x=1;
    int result;
    getchar();fflush(stdin);

    printf("\n\nDigite o nome do contato: ");
    fgets(nome,99,stdin);
    for(int i=0; i<contadorGlobal;i++){
        
        
        x = strcmp(contatos[i].nome,nome);

        
        if (x == 0){
            printf("--------------\nNome: %s",contatos[i].nome);
            printf("\nTelefone: %s",contatos[i].telefone);
            printf("\nEnderco: %s",contatos[i].endereco);
            printf("\nCidade: %s",contatos[i].cidade);
            printf("\nEstado: %s",contatos[i].estado);
            printf("\nNascimento: %d/%d/%d\n--------------",contatos[i].dia,contatos[i].mes,contatos[i].ano);
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

int modificar(){
    int indice;
    int dois;
    if (contadorGlobal>0){
    printf("Modificação de contato\n--------------");
    
    for(int i=0; i<contadorGlobal;i++){
        printf("\n%d-%s",i+1,contatos[i].nome);
    }
    printf("\nEscolha um contato\n");
    scanf("%d",&indice);
    indice--;
    while(indice<0 || indice>contadorGlobal-1){
        printf("\nValor inválido\n");
        printf("\nEscolha um contato\n");
        scanf("%d",&dois);
        indice = dois-1;
        return indice;
    }

    return indice;
    }else if(contadorGlobal==0){
        printf("\nNao ha contatos salvos\n");
        return 400;
    }


}

agenda modificarParte2(int change){

    char aux1[100];
    char aux2[100];
    char aux3[100];

    fflush(stdin);
    printf("\n\n");
    printf("Digite o nome: ");
    getchar();fflush(stdin);
    fgets(aux1,100,stdin);
    contatos[change].nome=(char*)malloc(strlen(aux1)*sizeof(char));
    strcpy(contatos[change].nome,aux1);
   

    printf("\n\n");
    printf("Digite o telefone: ");
    fflush(stdin);
    fgets(contatos[change].telefone,15,stdin);

  

    printf("\n\n");
    printf("Digite o endereco: ");
    fflush(stdin);
    fgets(aux2,100,stdin);
    contatos[change].endereco=(char*)malloc(strlen(aux2)*sizeof(char));

    strcpy(contatos[change].endereco,aux2);
    
    
    

    printf("\n\n");
    printf("Digite o cidade: ");
    fflush(stdin);
    fgets(aux3,100,stdin);
    contatos[change].cidade=(char*)malloc(strlen(aux3)*sizeof(char));
    strcpy(contatos[change].cidade,aux3);
    
    printf("\n\n");
    printf("Digite o estado(sigla): ");
    fflush(stdin);
    fgets(contatos[change].estado,4,stdin);
   

    printf("\n\n");
    printf("Digite o dia de nascimento(dd mm aaaa separado por espaco): ");
    
    scanf("%d %d %d",&contatos[change].dia,&contatos[change].mes,&contatos[change].ano);

}



void showAll(){
    char nomes[100];
    if (contadorGlobal>0){
        for(int i=0; i<contadorGlobal;i++){
            printf("--------------\n%d-%s\n",i+1,contatos[i].nome);
        }
        printf("--------------\n");
    }else if(contadorGlobal==0){
        printf("\nNao ha contatos salvos\n");
      
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
    int mudanca;
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
            mudanca=modificar();
            if(mudanca!=400){
            modificarParte2(mudanca);
            }
        }
        if(action==4){
            showAll();
        }
        menu();
        scanf("%d",&action);
        
    }
}   
