#include <stdio.h>
#include <stdlib.h>

int main()
{
    int i,n,target,found,index;
    scanf("%d",&target);
    scanf("%d",&n);
    int a[n];
    for( i=0; i<n ; i++ )
    {
        scanf("%d",&a[i]);
        if (a[i]==target)
        {
            found=1;
            index=i;
            break;
        }

    }
    if (found==1)
    {
        printf("%d",i);
    }

    return 0;
}
