#include <stdio.h>






int registerAcc(int *data) {
    int password;
    printf("Register Password: ");
    scanf("%d", &password);
    *data = password;
    printf("Password registered successfully.\n");
    return password;
}





int login(int *data, int *password) {
    printf("Enter password: ");
    scanf("%d", &password);
    if (*password != *data) {
        printf("incorrect password, try again\n");
	return main();
    }else
    return password;
}



int main() {
    int option = 0, password = 0, data = 0;

    while (1) {
        printf("1- Login | 2- Register password\n");
        scanf("%d", &option);
        switch (option) {
            case 1: {
                password = login(&data, password);
                break;
            }
            case 2: {
                password = registerAcc(&data);
                return main();
                break;
            }
            default: {
                printf("Invalid option, please try again.\n");
                continue;
            }
        }
        printf("Welcome!\n");
       
        printf("Your password is: %d\n", password);
        break;
    }

    return 0;
}
