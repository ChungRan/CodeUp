#include <iostream>
#include <vector>
using namespace std;

int main() {
	int lenX, lenY;
	cin >> lenY >> lenX;

	int** board = new int* [lenY];
	for (int i = 0; i < lenY; ++i) {
		board[i] = new int[lenX];
		//memset(board[i], 0, sizeof(int) * lenX);
	}

	int** newboard = new int* [lenY];
	for (int i = 0; i < lenY; ++i) {
		newboard[i] = new int[lenX];
		//memset(board[i], 0, sizeof(int) * lenX);
	}

	for (int i = 0; i < lenY; ++i) {
		for (int j = 0; j < lenX; ++j) {
			cin >> board[i][j];
		}
	}

	for (int i = 0; i < lenY; ++i) {
		for (int j = 0; j < lenX; ++j) {
			if (i == 0 && j == 0) {
				newboard[i][j] = board[i][j];
			}
			else if (i == 0) {
				newboard[i][j] = board[i][j] + newboard[i][j - 1];
			}
			else if (j == 0) {
				newboard[i][j] = board[i][j] + newboard[i - 1][j];
			}
			else {
				newboard[i][j] = board[i][j] + newboard[i - 1][j] + newboard[i][j - 1] - newboard[i - 1][j - 1];
			}
		}
	}

	for (int i = 0; i < lenY; ++i) {
		for (int j = 0; j < lenX; ++j) {
			cout << newboard[i][j] << " ";
		}
		cout << endl;
	}



	for (int i = 0; i < lenY; ++i) { delete[] board[i]; }
	delete[] board;

	for (int i = 0; i < lenY; ++i) { delete[] newboard[i]; }
	delete[] newboard;


	return 0;
}