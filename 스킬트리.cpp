#include <iostream>
#include <string>
#include <vector>

using namespace std;

int solution(string skill, vector<string> skill_trees)
{
	int answer = 0;
	vector<string> v_skill;
	for (int i = 0; i < skill.length(); i++)
	{
		v_skill.push_back(skill.substr(i, 1));
	}
	int count = 0;
	int skill_size = v_skill.size();

	for (int j = 0; j < skill_trees.size(); j++)
	{
		count = 0;
		for (int i = 0; i < skill_trees.at(j).length(); i++)
		{
			for (int k = count; k < skill_size; k++)
			{
				if (skill_trees.at(j).substr(i, 1) == v_skill.at(k))
				{
					if (k > count)
					{
						count = -1;
						break;
					}
					count++;
				}
			}
			if (count == -1)
			{
				break;
			}
		}
		if (count != -1)
			answer++;
	}
	return answer;
}

int main()
{
	string skill = "CBD";
	vector<string> skill_tree = { "BACDE", "CBADF", "AECB", "BDA" };
	cout << "가능한 스킬 트리 : " << solution(skill, skill_tree) << endl;
}