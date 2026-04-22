function reverseOnlyLetters(s: string): string {
    const arr = s.split("");
    let l = 0;
    let r = arr.length-1;

    while (l < r) {
        if(!isLetter(arr[l]) && !isLetter(arr[r])) {
            [arr[l], arr[r]] = [arr[r], arr[l]]
            l++
            r--
        }
        else if (!isLetter(arr[l])) {
            r--;
        }
        else if (isLetter(arr[r])) {
            l++
        }
        else {
            l++
            r--
        }
    }

    return arr.join("");
}

function isLetter(char: string): boolean {
    const code = char.charCodeAt(0);
    return (code >= 65 && code <= 90) || (code >= 97 && code <= 122);
}