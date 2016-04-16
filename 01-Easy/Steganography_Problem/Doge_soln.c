#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[]){

	FILE* fp1;	//The original file
	FILE* fp2;	//The modified file

	if(NULL==(fp1=fopen(argv[1], "r"))){
		printf("Failed to read file :%s\n", argv[1]);
		printf("Usage: ./printDifference <original> <changed file>");
		exit(-1);
	}
	if(NULL==(fp2=fopen(argv[2], "r"))){
		printf("Failed to read file :%s\n", argv[2]);
		printf("Usage: ./printDifference <original> <changed file>");
		exit(-1);
	}

	//compare character by character, and if different, push into an array
	int ch1, ch2;
	char codedMessage[100];
	int index = 0;
	while((EOF!=(ch1 = getc(fp1)))&&(EOF!=(ch2 = getc(fp2)))){
		if(ch1 != ch2){
			printf("Difference: %d\n",ch2);
			codedMessage[index] = ch2;
			index++;
		}
	}
	codedMessage[index+1] = '\0';
	
	//figure out how long the message is
	int length = 0;
	while(codedMessage[length] != '\0'){length++;}

	//['t','e','s','t', '\0']

	int i, j;

	//print out everything so you can see it and select the message
	//we can run blindly through offsets of 0-255, since characters wrap
	for(j=0; j<255; j++){
		printf("Offset %d: ", j);
		for(i=0; i<length; i++){
			putchar(codedMessage[i] + j);			
		}
		putchar('\n');
	}

	//return the message with the offset you found here (64)
	for(i=0; i<length; i++){
		codedMessage[i] += 64;
	}
	printf("\n%s\n\n", codedMessage);
}
