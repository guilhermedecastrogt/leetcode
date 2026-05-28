function isPalindrome(x: number): boolean {
    if(x < 0) {
        return false;
    }

    var arr = x.toString().split("").map(Number);

    var l = 0;
    var r = arr.length-1;

    while (r > l) {
        [arr[l], arr[r]] = [arr[r], arr[l]];
        r--;
        l++;
    }
    
    if(Number(arr.join("")) == x) {
        return true;
    }
    return false;
};