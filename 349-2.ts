function intersection(nums1: number[], nums2: number[]): number[] {
    return [...new Set<number>(nums1)].filter(n => new Set<number>(nums2).has(n))
}