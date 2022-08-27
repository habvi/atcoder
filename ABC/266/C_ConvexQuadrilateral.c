#include <stdio.h>
 
int isInside(double ax, double ay, double bx, double by, double cx, double cy, double tx, double ty)
{
    double abXat, bcXbt, caXct;
 
    abXat = (bx-ax)*(ty-ay) - (by-ay)*(tx-ax);
    bcXbt = (cx-bx)*(ty-by) - (cy-by)*(tx-bx);
    caXct = (ax-cx)*(ty-cy) - (ay-cy)*(tx-cx);
    if(( abXat > 0.0 && bcXbt > 0.0 && caXct > 0.0) || ( abXat < 0.0 && bcXbt < 0.0 && caXct < 0.0))
    {
        return 1;
    }
    else if(abXat*bcXbt*caXct == 0.0)
    {
        return 0;
    }
    return 0;
}
 
int isConcave(double px[], double py[])
{
    int i;
    for(i=0; i<4; i++)
    {
        if(isInside(px[i%4], py[i%4], px[(i+1)%4], py[(i+1)%4], px[(i+2)%4], py[(i+2)%4], px[(i+3)%4], py[(i+3)%4]))
        {
            return 1;
        }
    }
    return 0;
}
 
int main()
{
    double px[4], py[4];
    int i;
    for(i=0; i<4; i++)
    {
        scanf("%lf", &px[i]);
        scanf("%lf", &py[i]);
    }
    if(isConcave(px,py))
    {
        printf("No\n");
    }
    else
    {
        printf("Yes\n");
    }
}