#include <string.h>
#include <stdio.h>

int main(){
	char str[] = "a,b,c,d,e,f";
	char *token;

	token = strtok(str,",");
	printf("%s",strtok(NULL,","));
	while(token != NULL){
		printf("%s\n",token);
		token = strtok(NULL,",");
	}

}