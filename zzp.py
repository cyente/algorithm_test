#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;
const int M = 1000;
const int INF = 0x3f3f3f3f;
int n, ans, sum;
int w[M];
void dfs(int i, int cursum) {
    if (i == n) {
        ans = min(ans, abs(sum-2*cursum));
        return;
    }
    dfs(i+1, cursum+w[i]);
    dfs(i+1, cursum);
}
int main()
{
    while (scanf("%d", &n) != EOF) {
        sum = 0;
        for (int i = 0; i < n; ++i) {
            scanf("%d", &w[i]);
            sum += w[i];
        }
        ans = INF;
        if(n<=1) cout<<-1<<endl;
        else {
            dfs(0, 0);
            printf("%d\n", ans);
        }
    }
    return 0;
}