import java.util.*;

class TrieNode {
    char val;
    Map<Character, TrieNode> children;
    boolean isEnd;
    String number;

    public TrieNode(char val) {
        this.val = val;
        this.children = new HashMap<>();
        this.isEnd = false;
        this.number = "";
    }
}

public class Solution {
    private TrieNode root;

    public Solution() {
        this.root = new TrieNode('.');
    }

    public void insert(String num) {
        TrieNode cur = this.root;
        char[] digits = num.toCharArray();

        for (char digit : digits) {
            if (!cur.children.containsKey(digit)) {
                cur.children.put(digit, new TrieNode(digit));
            }

            cur = cur.children.get(digit);
        }

        cur.isEnd = true;
        cur.number = num;
    }

    public void dfs(TrieNode curNode, List<String> result) {
        if (curNode.isEnd) {
            result.add(curNode.number);
        }

        for (int i = 0; i < 10; i++) {
            char n = (char) (i + '0');
            if (curNode.children.containsKey(n)) {
                dfs(curNode.children.get(n), result);
            }
        }
    }

    public List<Integer> lexicalOrder(int n) {
        for (int num = 1; num <= n; num++) {
            insert(String.valueOf(num));
        }

        TrieNode cur = this.root;
        List<String> result = new ArrayList<>();
        dfs(cur, result);

        List<Integer> integerResult = new ArrayList<>();
        for (String num : result) {
            integerResult.add(Integer.parseInt(num));
        }

        return integerResult;
    }
}