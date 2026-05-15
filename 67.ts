function addBinary(a: string, b: string): string {
    var p;
    let binaryCount: number[] = [];
    var temp = 0;

    if (a.length > b.length) {
        p = a.length;
    } else {
        p = b.length;
    }

    while (p != 0) {
        let indexA = a.length - 1 - binaryCount.length;
        let indexB = b.length - 1 - binaryCount.length;
        let digitA = indexA >= 0 ? a[indexA] : "0";
        let digitB = indexB >= 0 ? b[indexB] : "0";
        let result = soma(digitA, digitB) + temp;

        if (result == 0) {
            binaryCount.push(0);
            temp = 0;
        } else if (result == 1) {
            binaryCount.push(1);
            temp = 0;
        } else if (result == 2) {
            binaryCount.push(0);
            temp = 1;
        } else if (result == 3) {
            binaryCount.push(1);
            temp = 1;
        }

        p--;
    }

    if (temp == 1) {
        binaryCount.push(1);
    }

    return binaryCount.reverse().join("");
}

function soma(a: string, b: string): number {
    return Number(a) + Number(b);
}