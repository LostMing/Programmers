#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int solution(vector<int> numbers)
{
    int answer = 0;
    int size = 0;
    sort(numbers.begin(), numbers.end());
    for (int i = 0; i < 10; i++)
    {
        if (i != numbers[size])
            answer += i;
        else
            size++;
    }
    return answer;
}

int main()
{
    vector<int> numbers1 = { 1, 2, 3, 4, 5, 6, 7, 8, 0 };
    vector<int> numbers2 = { 5,8,4,0,6,7,9 };
    cout << "numbers1 : " << solution(numbers1) << endl;
    cout << "numbers2 : " << solution(numbers2) << endl;
}