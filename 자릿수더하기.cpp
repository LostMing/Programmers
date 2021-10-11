#include <iostream>

using namespace std;
int solution(int n)
{
    int answer = 0;
    while (n / 10 > 0)
    {
        answer += n % 10;
        n /= 10;
    }
    answer += n % 10;
    return answer;
}

int main()
{
    int n1 = 123;
    int n2 = 987;
    cout << "n1 : " << solution(n1) << endl;
    cout << "n2 : " << solution(n2) << endl;
}