#include <stdio.h>

int main() {
	char n;
	printf("please enter grade \n");
	scanf("%c",&n);
	
	switch(n){
		case'A':
		printf("Excellent");
		break;
		
		case'B':
		printf("Well done");
		break;
		
		case'C':
		printf("Try again");
		break;
		
		default:
		printf("Invalid grade");
		
	}
	return 0;
}
