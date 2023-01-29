#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n,i;
    long int sum=0;
    scanf("%d",&n);
    long int  a[n];
    for (i=n;i>0;i--)
    {
       
        scanf("%ld",&a[i]);
        sum=sum+a[i];
    }
    printf("%ld",sum);
    return 0;
}

