class Solution {
    public int[] runningSum(int[] nums) {
        int s = 0;
        int[] sums = new int[nums.length];
        for(int i = 0; i < nums.length; ++i) {
            s += nums[i];
            sums[i] = s;
        }
        return sums;
    }
}
