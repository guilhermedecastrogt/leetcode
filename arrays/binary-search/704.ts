function search(nums: number[], target: number): number {
    let hi = nums.length;
    let low = 0;

    while (low < hi) {
        let mid = Math.floor((hi+low)/2);

        if(nums[mid] == target) {
            return mid;
        }
        if(nums[mid] < target) {
            low = mid+1;
        }
        else{
            hi = mid;
        }
    }
    return -1
};