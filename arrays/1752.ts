function check(nums: number[]): boolean {
    var broke = 0;
    for(let i = 0; i < nums.length; i++) if((i == 0 && nums[i] < nums[nums.length-1]) || (nums[i] < nums[i-1])) broke++;
    if(broke>1) return false;
    return true;
};