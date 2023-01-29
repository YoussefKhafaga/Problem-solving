#include <stdio.h>
#include <stdlib.h>


    int main()
{   int n,counter=1,b;
    scanf("%d",&n);
    int i;
    int a[n];
    scanf("%d",&a[n]);
    int max=a[n];
    for (i=0;i<n-1;i++)
    {
        scanf("%d",&a[i]);
         if (a[i]==max) {
            counter=counter+1;

        }

        if (a[i]>max) { b=a[i];
        max=b;

        }


         }
    printf("%d",counter);

    return 0;
}
