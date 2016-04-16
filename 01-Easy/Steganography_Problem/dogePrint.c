#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[]){

	int ch;
	FILE *fp;
	if((fp = fopen(argv[1], "r"))==NULL){
		printf("Failed to open file: %s", argv[1]);
		printf("\n\nUsage: ./dogePrint <filename>\n\n");
		exit(-1);
	}
	else{
		int count = 0;
		while(EOF != (ch = getc(fp))){
			putchar(ch);
		}
	}
	putchar('\n');
	fclose(fp);
}
