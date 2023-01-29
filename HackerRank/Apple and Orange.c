#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{   int na,no,i,suma=0,sumo=0;
    int at,ot,s,t;
    scanf("%d%d",&s,&t);
    scanf("%d%d",&at,&ot);
    scanf("%d%d",&na,&no);
    int a[na],o[no];
    for (i=0;i<na;i++)
    {
        scanf("%d",&a[i]);
        if(a[i]+at<=t && a[i]+at>=s) suma++;
    }
    for(i=0;i<no;i++)
    {
        scanf("%d",&o[i]);
        if(o[i]+ot<=t && o[i]+ot>=s) sumo++;
    }
   printf("%d\n%d",suma,sumo);
}

