function isPalindromee(s: string): boolean {
    let isPar = s.length%2
    let stringPar = [];
    if(isPar != 0){
        for(let i = 0; i < s.length; i++) {
            if(i != Math.trunc(s.length/2)) {
                stringPar.push(s[i]);
            }
        }
    }
    console.log(stringPar)
    return true;
};