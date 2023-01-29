#include <stdio.h>
#include <stdlib.h>

int main()
{
    int i,j,n,k;
    scanf("%d",&n);
    for (i=0; i<n; i++)
    {

        for (j=0; j<n-i-1; j++)
        {
            printf(" ");

        }

        for (k=0;k<=i;k++)
       {


            printf("#");

        }
       if (i<=n-2) {
        printf("\n"); }
    }
    return 0;
}


