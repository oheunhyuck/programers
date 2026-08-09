#include <vector>
using namespace std;
#include <unordered_map>

int solution(vector<int> nums)
{
    unordered_map<int, int> mp;
    for (auto n : nums)
        mp[n]++;
    if(mp.size()>nums.size()/2){
        return  nums.size()/2;
    }
    else{
         return mp.size();
    }
    
    int answer = 0;
    return answer;
}