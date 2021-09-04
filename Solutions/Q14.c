#include <stdio.h>

int main(void) {
	// your code goes here
	int T;
	scanf("%d",&T);
	while(T--)
	{   int A,B,C,D,E;
	    scanf("%d %d %d %d %d",&A,&B,&C,&D,&E);
	    /*int minum =0;
	    if (A <= B && A <= C)
	        minum = A;
	    else if(B <= A && B <= C)
	        minum = B;
	    else
	        minum = C;
	   */
	    int sum = A+B+C;
	    if (sum-A <=D && A<=E)
	        printf("YES\n");
	    else if (sum-B <=D && B<=E)
	        printf("YES\n");
	    else if (sum-C <=D && C<=E)
	        printf("YES\n");
	    else
	        printf("NO\n");
	}
	return 0;
}

