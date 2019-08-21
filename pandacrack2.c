#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main (int argc, char** argv) {

	//vars
	void *uVar1;
	unsigned int seed;
	int intInSize;
	int rand1;
	int rand2;
	int readInCounter;
	int counter;
	FILE *infile;
	FILE *outfile;
	long longInSize;
	void *output;
	long ranx[1000];
	long rany[1000];
	
	readInCounter = 0;
	
	// conver seed val string to int.
	seed = atoi((char *)argv[1]);

	//open file in and out
	infile = fopen((char *)argv[2],"r");
	outfile = fopen((char *)argv[3],"w+");

	if ((infile != (FILE *)0x0) && (outfile != (FILE *)0x0)) {
		fseek(infile,0,2);
		longInSize = ftell(infile);
		intInSize = (int)longInSize;
		fseek(infile,0,0);
		//output = calloc((long)(intInSize+1),1);
		output = calloc((long)(intInSize+1),1);
		printf("longInSize: %ld intInSize: %i readInCounter: %i\n",longInSize,intInSize,readInCounter);
		printf("readInCounter: %ld, output: %s, longInSize: %ld\n",readInCounter,output,longInSize);
		while (readInCounter < intInSize) {
		fread((void *)((long)readInCounter + (long)output),1,1,infile);
		readInCounter = readInCounter + 1;
		}
		fclose(infile);
		srand(seed);
		counter = 0;
		//printf("readInCounter %ld output %s intInSize %ld",readInCounter,output,intInSize);
		while (counter < 1000) {
			rand1 = rand();
			rand1 = rand1 % (intInSize + -1);
			rand2 = rand();
			rand2 = rand2 % (intInSize + -1);
			ranx[999-counter]=rand1;
			rany[999-counter]=rand2;
			counter++;
		}
		counter = 0;
		while (counter < 1000) {
			//printf("c: %d readInCounter: %ld intInSize: %ld rand1: %ld rand2: %ld output: %ld\n",counter,readInCounter,intInSize, rand1, rand2, (long)output);
			uVar1 = *(unsigned char *)((long)output + (long)rany[counter]);
			*(unsigned char *)((long)output + (long)rany[counter]) = *(unsigned char *)((long)output + (long)ranx[counter]);
			*(unsigned char *)((long)ranx[counter] + (long)output) = uVar1;

			/*uVar1 = *(unsigned char *)((long)output + (long)rand2);
			*(unsigned char *)((long)output + (long)rand2) = *(unsigned char *)((long)output + (long)rand1);
			*(unsigned char *)((long)rand1 + (long)output) = uVar1;*/

			counter = counter + 1;
		}
		fwrite(output,1,(long)intInSize,outfile);
		fclose(outfile);
		printf("%s",output);
		return 0;
	}
	perror("error opening file.\n");
	exit(1);
}
