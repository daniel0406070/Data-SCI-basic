#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define pattern_size 8
#define text_size 140000005

int f[pattern_size]={0,};

void FailureFunction(int m, int* pattern){

	for (int i = 1, j = 0; i < m; i++) {
		while (j > 0 && pattern[i] != pattern[j]) j = f[j - 1];

		if (pattern[i] == pattern[j]) f[i] = ++j;
        else f[i] = 0;
	}
}

//모든 부분을 탐색
int kmp(int n, int m, int* text, int* pattern){

	int i = 0;
	int j = 0;

    // int kmp_idx_arr[text_size]={0,};
    int kmp_count=0;

    for(int i=0; i<n; i++){
        while (j > 0 && text[i] != pattern[j]) j = f[j - 1];

        if (text[i] == pattern[j]) {
            if(j==m-1){
                // kmp_idx_arr[kmp_count]=i-j;
                (kmp_count)++;
                j=f[j];
            }
            else j++;
        }
    }

    return kmp_count;
}

int lotto_sel[pattern_size]={0,};
int lotto_arr[text_size]={0,};

int main(){
    int n;
    scanf("%d", &n);

    for(int i=0; i<text_size; i++){
        lotto_arr[i]=rand()%45+1;
        for(int j=i-5; j<i; j++){
            if(lotto_arr[i]==lotto_arr[j]){
                i--;
                break;
            }
        }
    }
    printf("\n");

    printf("init done\n");

    
    for(int i=0; i<20; i++){
        for(int i=0; i<6; i++){
        lotto_sel[i]=rand()%45+1;
        for(int j=0; j<i; j++){
            if(lotto_sel[i]==lotto_sel[j]){
                i--;
                break;
            }
        }
    }

        FailureFunction(6, lotto_sel);
        int win_count=kmp(n, 6, lotto_arr, lotto_sel);

        printf("%d\n", win_count);
    }

}
