class Solution {
public:
static bool compare(pair<int,int>&p1,pair<int,int>&p2)
{
    return p1.second>p2.second;
}
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<int>ans;
        unordered_map<int,int>m1;
        for(int x:nums)
        {
            m1[x]++;
        }
        vector<pair<int,int>>v;
        for(auto x:m1)
        {
            v.push_back({x.first,x.second});
        }
        sort(v.begin(),v.end(),compare);
        for(int i=0;i<k;i++)
        {
            ans.push_back(v[i].first);
        }
        return ans;
    }
};