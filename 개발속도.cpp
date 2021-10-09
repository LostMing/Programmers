#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds)
{
	vector<int> answer;

	int day;
	int max_day = 0;
	for (int i = 0; i < progresses.size(); ++i)
	{
		day = (99 - progresses[i]) / speeds[i] + 1;

		if (answer.empty() || max_day < day)			//empty() 벡터가 비어 있으면 true		먼저 100% 채워지면 뒷부분만 계산
			answer.push_back(1);
		else
			++answer.back();							//마지막원소 ++

		if (max_day < day)
			max_day = day;
	}

	return answer;
}

int main()
{
	vector<int> progresses = { 93,30,55 };
	vector<int> speeds = { 1,30,5 };
	vector<int> progresses1 = { 95,90,99,99,80,89 };
	vector<int> speeds1 = { 1,1,1,1,1,1 };
	vector<int> result;
	result = solution(progresses, speeds);
	for (int i = 0; i < result.size(); i++)
	{
		cout << result.at(i) << " ";
	}
	cout << endl;
	result = solution(progresses1, speeds1);
	for (int i = 0; i < result.size(); i++)
	{
		cout << result.at(i) << " ";
	}
	cout << endl;
}
