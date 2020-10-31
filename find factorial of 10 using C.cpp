#include<stdio.h>

int main()
{
	int i=1 , j=1 ;
	
	while (i<=10 )
	{
		j=j*i;
		i=i+1;
	}
	
	printf("Factorial 10 = %d",j);
	
}
