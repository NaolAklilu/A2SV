class Solution {
    public int bagOfTokensScore(int[] tokens, int power) {
        Arrays.sort(tokens);
        int score = 0, left = 0, right = tokens.length - 1;
        
        while (left < right) {
            if (power >= tokens[left]) {
                power -= tokens[left];
                left += 1;
                score += 1;
            } else if (score >= 1 && power >= tokens[left] - tokens[right]) {
                power += tokens[right];
                right -= 1;
                score -= 1;
            } else {
                break;
            }
        }
        
        if (left == right && power >= tokens[left]) {
            power -= tokens[left];
            score += 1;
        }
        
        return score;
    }
}