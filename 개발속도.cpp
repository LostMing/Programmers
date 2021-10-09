#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds)
{
	//100% 넘어가도 계속 계산해줌
	vector<int> answer;
	vector<int> day(progresses.size(), 0);
	int count = 0;
	int num = progresses.size();
	while (num > 0)
	{
		count++;
		for (int i = 0; i < progresses.size(); i++)
		{
			progresses.at(i) += speeds.at(i);
			if (day.at(i) == 0 && progresses.at(i) >= 100)
			{
				day.insert(day.begin() + i, count);
				day.erase(day.begin() + i + 1);
				num--;
			}
		}
	}
	num = day.at(0);
	count = 0;
	for (int i = 1; i < day.size(); i++)
	{
		count++;
		if (num < day.at(i))
		{
			answer.push_back(count);
			num = day.at(i);
			count = 0;
		}
	}
	answer.push_back(++count);
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
