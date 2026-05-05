function isPalindrome(s: string): boolean {
    s = normalizarTexto(s);
    let isPar = s.length % 2;
    let stringPar = [];
    let i = 0;

    if (isPar != 0) {
        while (i < s.length) {
            if (i < Math.trunc(s.length / 2) ) {
                stringPar[i] = s[i];
            }
            else if (i > Math.trunc(s.length / 2)) {
                stringPar[i-1] = s[i];
            }
            i++;
        }
    } else {
        stringPar = [...s]
    }
    
    let pl = 0;
    let pr = 0;
    pr = stringPar.length-1;
    let invertedString = [];

    while (pr > pl) {
        invertedString[pl] = stringPar[pr];
        invertedString[pr] = stringPar[pl];
        pr--;
        pl++;
        
    }

    if(invertedString.join("") == stringPar.join(""))
        return true

    return false
};

function normalizarTexto(texto: any) {
  return String(texto)
    .toLowerCase()
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "")
    .replace(/\s+/g, "")
    .replace(/[^a-z0-9]/g, "");
}