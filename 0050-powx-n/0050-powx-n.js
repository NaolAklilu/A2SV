/**
 * @param {number} x
 * @param {number} n
 * @return {number}
 */
var myPow = function(x, n) {
    const power = Math.abs(n);

        const recur = (x, n) => {
            if (n === 0) {
                return 1;
            }

            if (n % 2 === 0) {
                const half = recur(x, n / 2);
                return half * half;
            } else {
                const half = recur(x, Math.floor((n - 1) / 2));
                return half * half * x;
            }
        };

        let result = recur(x, power);
        if (n < 0) {
            return 1 / result;
        }
        return result;
};
