#include<stdio.h>
int main(int argc, char const *argv[])
{
     int i,j,n,arr[100],q=0,max=0;
     scanf("%d",&n);
     for(i = 0; i < n; i++){
        scanf("%d",&arr[i]);
     }
     

     for (i = 0; i < n-1; i++){        
    for (j = 0; j < n-i-1; j++){  
        if (arr[j] > arr[j+1]){  
            swap(&arr[j], &arr[j+1]);
        }
        }
        }
    max = arr[n-1];
    for(i=0;i<n;i++)
    {
        if (i==max)
        {
            q=q+1;
        }
    }
    printf("%d",q);
    return 0;
}
void swap(int *xp, int *yp) 
{ 
    int temp = *xp; 
    *xp = *yp; 
    *yp = temp; 
} 
  
