#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

long long solution(int w, int h) {
    long long W = w, H = h;
    long long i = 1;
    long long cnt = 0;
    long long ans = 0;
    long long l = 0;
    while (i <= W) {
        long long temp = -1;
        if ((i * H) % W == 0) {
            temp = H * i / W;
            cnt += H * i / W - l;
            break;
        } else {
            temp = H * i / W;
            cnt += H * i / W + 1 - l;
        }
        l = temp;
        i++;
    }
    ans += (W / i) * cnt;

    return W * H - ans;
}