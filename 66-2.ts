function plusOne(digits: number[]): number[] {
    var added = true;
    var p = digits.length-2;

    if(digits[digits.length-1] != 9) {
        digits[digits.length-1]++; 
        return digits;
    }
    else if(digits[0] == 9 && digits.length == 1) {
        digits[0] = 1;
        digits[1] = 0;
        return digits;
    }

    digits[digits.length-1] = 0;
  
    while(added) {
        if(p == 0 && digits[p] == 9) {
            digits[p] = 1;
            digits[digits.length] = 0;
            added = false
        } else if (digits[p] != 9) {
            digits[p]++;
            added = false;
        }
        else {
            digits[p] = 0;
        }
        p--;
    }

    return digits;
};