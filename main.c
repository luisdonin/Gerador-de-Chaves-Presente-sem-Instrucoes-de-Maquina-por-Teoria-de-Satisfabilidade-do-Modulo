#include <stdio.h>




int main() {

        int valCode[5];

        int sum;
        int i;
        printf("Validation code: ");
        for( i=0; i<5;i++){
            scanf("%d", &valCode[i]);
        }

        sum = valCode[0] + valCode[1] + valCode[2] + valCode[3] + valCode[4] ;
            

        if(sum %2 == 0){
            printf("\nWelcome!");
        }
        else{
            printf("\nInvalid Key!");
            printf("\nsum: %d\n", sum);
        }

        printf("Validation: ");
        for( i=0; i<5;i++){
            printf(" %d", valCode[i]);
        }
        printf("\n");

        return 0;
}
