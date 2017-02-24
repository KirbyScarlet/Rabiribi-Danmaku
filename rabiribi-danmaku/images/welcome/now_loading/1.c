#include<stdio.h>
#include<stdlib.h>

void main()
{
	char ch[100];
	int i;
	for(i=0;i<360;i++)
	{
		if(i<10) sprintf(ch, "mv Comp\\ 1_0000%d.png now_loading_00%d.png", i, i);
		if(i>=10&&i<100)  sprintf(ch, "mv Comp\\ 1_000%d.png now_loading_0%d.png", i, i);
		if(i>=100) sprintf(ch, "mv Comp\\ 1_00%d.png now_loading_%d.png", i, i);
		system(ch);
	}
} 
