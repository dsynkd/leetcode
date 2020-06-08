class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        int m = 0;
        for(int i = 0; i < candies.size(); ++i)
            if(candies[i] > m)
                m = candies[i];
        vector<bool> r;
        for(int i = 0; i < candies.size(); ++i) {
            if(candies[i] + extraCandies >= m)
                r.push_back(true);
            else
                r.push_back(false);
        }
        return r;
    }
};
