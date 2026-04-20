function maximumLengthSubstring(s: string): number {
    let pL = 0;
    let pR = 0;
    let max = 1;
    let charCount = new Map<string, number>();
    charCount.set(s[0], 1);

    while (pR < s.length - 1) {
        pR++;

        if (charCount.get(s[pR])) {
            charCount.set(s[pR], charCount.get(s[pR])! + 1);
        } else {
            charCount.set(s[pR], 1);
        }

        while (charCount.get(s[pR])! == 3) {
            const charLeft = s[pL];

            charCount.set(charLeft, charCount.get(charLeft)! - 1);
            pL++;
        }

        max = Math.max(max, pR - pL + 1);
    }

    return max;
};