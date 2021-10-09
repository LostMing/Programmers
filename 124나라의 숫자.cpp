#include <iostream>
#include <string>
#include <vector>

using namespace std;

string solution(int n)
{
	string answer = "";
	vector<string> temp = { "4","1","2" };
	while (n > 0)
	{
		answer = temp.at(n % 3) + answer;

		if (n % 3 == 0)
			n = n / 3 - 1;
		else
			n = n / 3;
	}
	return answer;
}

int main()
{
	int n[4] = { 1,2,3,4 };
	for (int i = 0; i < 4; i++)
	{
		cout << solution(n[i]) << endl;
	}
}