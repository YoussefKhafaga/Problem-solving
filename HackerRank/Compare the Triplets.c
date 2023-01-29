#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a[3],b[3],scalice=0,scorebob=0,sc[2];
    scanf("%d%d%d%d%d%d",a,a+1,a+2,b,b+1,b+2);
    if (a[0]>b[0]) {scalice++; }else if (a[0]<b[0]){scorebob++;}
    if (a[1]>b[1]) {scalice++; } else if (a[1]<b[1]) {scorebob++;}
    if (a[2]>b[2]) {scalice++;} else if (a[2]<b[2]){scorebob++;}
    sc[0]=scalice;
    sc[1]=scorebob;
    printf("%d %d",sc[0],sc[1]);
    return 0;
}
