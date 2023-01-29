#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int main()
{
    int n;

    
    scanf("%d",&n);
    int a[n];
    int i;

    for (i=n; i>0; i--)
    {
        
        scanf("%d",&a[i]);
    }
    for(i=n; i>0; i--)
    {
        if (a[i]>=38)
        {
            if ((a[i]+2)%5==0)
            {
                printf("%d\n",a[i]+2);
            }
            else if ((a[i]+1)%5==0)
            {
                printf("%d\n",a[i]+1);
            }
            else
            {
                printf("%d\n",a[i]);
            }
        }
        else printf("%d\n",a[i]);


    }


    return 0;
}
