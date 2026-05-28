function plusOne2(digits: number[]): number[] {
    return String(Number(digits.join(""))+1).split("").map(Number);
};