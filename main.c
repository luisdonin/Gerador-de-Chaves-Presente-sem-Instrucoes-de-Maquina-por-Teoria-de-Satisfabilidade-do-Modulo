#include <stdio.h>




int valida(int valCode[5]) {
    int sum, i;

        sum = valCode[0] + valCode[1] + valCode[2] + valCode[3] + valCode[4] ;
            

        if(sum %2 == 0){
            printf("\nWelcome!");
            return 1;
        }
        else{
            printf("\nInvalid Key!");
            printf("\nsum: %d\n", sum);
        }

        printf("\nValidation key: ");
        for( i=0; i<5;i++){
            printf(" %d", valCode[i]);
        }
        printf("\n");

        return 0;
}

int main(){
    int valCode[5];

    int i;
    printf("Validation key: ");
    for( i=0; i<5;i++){
        scanf("%d", &valCode[i]);
    }
    valida(valCode);
    return 0;
}
