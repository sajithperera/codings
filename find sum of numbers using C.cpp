#include<stdio.h>

int main()
{
	int i , sum=0 ;
	
	do
	{
		printf("\nEnter a number:");
		scanf("%d",&i);
		sum=sum+i;
	}
	
	while(i!=1);
	
	
	printf("Sum= %d " , sum);
}
