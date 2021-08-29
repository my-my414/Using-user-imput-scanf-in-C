#include<stdio.h>
int main()
{
    int a,b,c,d;
    printf("Enter the value of a,b,c and d :\n");
    scanf("%d%d%d%d",&a,&b,&c,&d);
    /*here  scanf() is a function to read character string numeric data from keyboard and & is used for addressing the variable*/
    printf("%d\n",(a+b)+(c*d));
    return 0;
}
