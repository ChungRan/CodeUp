////#include <iostream>
//#define _CRT_SECURE_NO_WARNINGS
//#include<algorithm>
//#include<vector>
//#include<stdio.h>
//
//using namespace std;
//
//struct Data {
//	int value;
//	int initNum;
//	int afterNum;
//};
//
//bool comp1(Data a, Data b) {
//	return a.value < b.value;
//}
//
////입력순서를 올림차순으로 정렬
//bool comp2(Data a, Data b) {
//	return a.initNum < b.initNum;
//}
//
//int main() {
//	/*ios_base::sync_with_stdio(false);
//	cin.tie(NULL);
//	cout.tie(NULL);*/
//
//	int n;
//	scanf("%d", &n);
//
//	vector <Data> dataVector(n);
//
//	for (int i = 0; i < n; ++i) {
//		scanf("%d", &dataVector[i].value);
//		dataVector[i].initNum = i;
//	}
//
//	sort(dataVector.begin(), dataVector.end(), comp1);
//
//	for (int i = 0; i < n; ++i) {
//		dataVector[i].afterNum = i;
//	}
//	
//	sort(dataVector.begin(), dataVector.end(), comp2);
//
//	for (int i = 0; i < n; ++i) {
//		printf("%d ", dataVector[i].afterNum);
//	}
//
//	return 0;
//}

#include <iostream>
#include<algorithm>
#include<vector>
using namespace std;

struct Data {
	int value;
	int initNum;
	int afterNum;
};

bool comp1(Data a, Data b) {
	return a.value < b.value;
}

//입력순서를 올림차순으로 정렬
bool comp2(Data a, Data b) {
	return a.initNum < b.initNum;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int n;
	cin >> n;

	vector <Data> dataVector(n);

	for (int i = 0; i < n; ++i) {
		cin >> dataVector[i].value;
		dataVector[i].initNum = i;
	}

	sort(dataVector.begin(), dataVector.end(), comp1);

	for (int i = 0; i < n; ++i) {
		dataVector[i].afterNum = i;
	}

	sort(dataVector.begin(), dataVector.end(), comp2);

	for (int i = 0; i < n; ++i) {
		cout << dataVector[i].afterNum << " ";
	}

	return 0;
}
