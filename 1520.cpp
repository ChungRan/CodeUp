#include <iostream>
using namespace std;

int main() {
	// 입력
	int a, b, x, y, z, k, total;
	cin >> a >> b >> x >> y >> z;
	int board[172][172] = { 0, };
	int newBoard[172][172] = { 0, };

	for (int i = 1; i <= a; ++i) {
		for (int j = 1; j <= b; ++j) {
			cin >> board[i][j];
		}
	}
	cin >> k;

	// 구현
	for (int time = 0; time < k; ++time) {
		//cout << "time: " << time;
		for (int i = 1; i <= a; ++i) {
			for (int j = 1; j <= b; ++j) {
				total = board[i - 1][j - 1] + board[i - 1][j] + board[i - 1][j + 1] + board[i][j - 1] + board[i][j + 1] + board[i + 1][j - 1] + board[i + 1][j] + board[i + 1][j + 1];
				if (board[i][j] == 0) {
					// 생명이 없다면
					if (total == x) { newBoard[i][j] = 1; }
					else { newBoard[i][j] = 0; }
				}
				else {
					if (total >= y && total < z) { newBoard[i][j] = 1; }
					else { newBoard[i][j] = 0; }
				}
			}
		}

		// 보드 복사, 아니면 스위치방식으로 전환
		for (int i = 1; i <= a; ++i) {
			for (int j = 1; j <= b; ++j) {
				board[i][j] = newBoard[i][j];
			}
		}
	}

	// 출력
	for (int i = 1; i <= a; ++i) {
		for (int j = 1; j <= b; ++j) {
			cout << board[i][j] << " ";
		}
		cout << "\n";
	}
	return 0;
}