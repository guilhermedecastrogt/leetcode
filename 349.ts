function intersection(nums1: number[], nums2: number[]): number[] {
    let seen = new Set<number>()
    let intersection: number[] = []

    for(let n of nums1) {
        if(!seen.has(n))
            seen.add(n)
    }

    for(let n2 of seen) {
        if(nums2.includes(n2))
            intersection.push(n2)
    }

    return intersection;
};