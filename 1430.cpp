#include <iostream>
using namespace std;

int arr[10000001] = { 0, };
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int n, m;
	int input;
	cin >> n;
	for (int i = 0; i < n; ++i) {
		cin >> input;
		++arr[input];
	}
	cin >> m;
	for (int i = 0; i < m; ++i) {
		cin >> input;
		if (arr[input] > 0) {
			cout << "1 ";
		}
		else {
			cout << "0 ";
		}
	}
}