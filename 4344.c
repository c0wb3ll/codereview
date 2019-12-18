#include <stdio.h>

int main() {
	int test, score[1000], a, i, j, k;
	double avg, sum = 0, avgsco = 0;
	scanf_s("%d", &test);
	for (i = 0; i < test; i++) {
		scanf_s("%d", &a);
		for (j = 0; j < a; j++) {
			scanf_s("%d", &score[j]);
			sum += score[j];
		}
		avg = sum / a;
		for (k = 0; k < a; k++) {
			if (avg < score[k]) {
				avgsco++;
			}
		}
		printf("%.3f%%\n", (avgsco / a)*100);
		avgsco = 0;
		avg = 0;
		sum = 0;
	}
	return 0;
}