#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n,i;
    float counter1=0,counter2=0,counter3=0;
    scanf("%d",&n);
    int a[n];
    for(i=0;i<n;i++)
    {

        scanf("%d",&a[i]);

        if(a[i]>0){counter1++;}
        if(a[i]<0) {counter2++;}
        if(a[i]==0) {counter3++;}

    }
    printf("%.6f\n",counter1/n);
    printf("%.6f\n",counter2/n);
    printf("%.6f\n",counter3/n);
    return 0;
}
