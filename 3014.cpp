#include <iostream>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int result[100001] = { 0, };
	int n, in;
	cin >> n;
	for (int i = 0; i < n; ++i) {
		cin >> in;
		++result[in];
	}
	for (int i = 0; i < 100001; ++i) {
		if (result[i] > 0){
			for (int j = 0; j < result[i]; ++j) {
				cout << i << " ";
			}
		}
	}

	return 0;
}