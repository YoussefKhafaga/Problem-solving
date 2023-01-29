#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int main()
{
    int n,i,j,d1=0,d2=0;
    scanf("%d",&n);
    int a[n][n];
    for (i=0;i<n;i++)
    {

    for (j=0;j<n;j++)
    {
        scanf("%d",&a[i][j]);
    }
    }
    i=0;
    j=0;
while (i<n&&j<n) {
    d1=d1+a[i][j];
    i++;
    j++;
}
i=0;
j=n-1;
while (i<n&&j>=0){

    d2=d2+a[i][j];
    j--;
    i++;


}
printf("%d",abs(d1-d2));
/*if (n==3) {
    d1=a[0][0]+a[1][1]+a[2][2];
    d2=a[0][2]+a[1][1]+a[2][0];
    printf("%d",abs(d1-d2));
}
if (n==2) {
    d1=a[0][0]+a[1][1];
    d2=a[1][0]+a[0][1];
    printf("%d",abs(d1-d2));
}

*/
    return 0;
}
