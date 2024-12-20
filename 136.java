class Solution {
    public int singleNumber(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        for(int i = 0; i < nums.length; ++i) {
            if(map.containsKey(nums[i])) {
                map.remove(nums[i]);
            }
            else {
                map.put(nums[i], 0);
            }
        }
        assert(map.size() == 1);
        return map.entrySet().iterator().next().getKey();
    }
}
