class Solution {
public:
    int numTriplets(vector<int>& nums1, vector<int>& nums2) {
        int c = 0;
        unordered_map<int,int> m;
        for(int i : nums1) {
            m.clear();
            long n = (long)i*i;
            for(auto j : nums2) {
                if(n % j == 0) {
                    c += m[n / j];
                }
                m[j] += 1;
            }
        }
        for(int i : nums2) {
            m.clear();
            long n = (long)i*i;
            for(auto j : nums1) {
                if(n % j == 0) {
                    c += m[n / j];
                }
                m[j] += 1;
            }
        }
        return c;
    }
};
