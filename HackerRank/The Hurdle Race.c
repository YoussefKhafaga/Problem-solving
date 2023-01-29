#include <stdio.h>
#include <stdlib.h>


    int main()
{   int n,counter=0,b,g;
    scanf("%d",&n); //scan el twl bta3o
    // scan 3dd el bto3
    scanf("%d",&g);
    int i;
    int a[n];
    scanf("%d",&a[n]);
    int max=a[n];
    for (i=0;i<n-1;i++)
    {
        scanf("%d",&a[i]);

        if (a[i]>max) { b=a[i];
        max=b;

        }


         }
        if (g<max) counter=max-g;
    printf("%d",counter);

    return 0;
}
