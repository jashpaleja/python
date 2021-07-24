#include<stdio.h>
int main()
{
int n,i=0,j=0;
scanf("%d",&n);
int num[100][100],sum1=0,sum2=0,diff=0;
// printf("enter number of digits to be added");
for(int i=0;i<n;i++)
{
    for(int j=0;j<n;j++)
    scanf("%d", &num[i][j]);
}
for(int i=0;i<n;i++)
{
    for(int j=0;j<n;j++)
    {
     if(i==j)
     {
     	sum = sum+num[i][j];
     }
// printf("\n");
}
 return 0;
    
}