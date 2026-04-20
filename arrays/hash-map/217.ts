function containsDuplicate(nums: number[]): boolean {
    let seen = new Set<number>();

    for(let n of nums) {
        if(seen.has(n)) {
            return true;
        }
        seen.add(n);
    }

    return false;
};