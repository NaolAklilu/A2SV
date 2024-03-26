/**
 * @param {number} n
 * @return {number[]}
 */
var lexicalOrder = function(n) {
 class TrieNode {
 constructor(val) {
     this.val = val;
     this.children = {};
     this.isEnd = false;
     this.number = "";
 }
 }

 class Solution {
 constructor() {
     this.root = new TrieNode(".");
 }

 insert(num) {
     let cur = this.root;
     let digits = num.split("");

     for (let digit of digits) {
         if (!(digit in cur.children)) {
             cur.children[digit] = new TrieNode(digit);
         }

         cur = cur.children[digit];
     }

     cur.isEnd = true;
     cur.number = num;
 }

 dfs(curNode, result) {
     if (curNode.isEnd) {
         result.push(curNode.number);
     }

     for (let i = 0; i <= 9; i++) {
         let strI = String(i);
         if (strI in curNode.children) {
             this.dfs(curNode.children[strI], result);
         }
     }
 }

 lexicalOrder(n) {
     for (let num = 1; num <= n; num++) {
         this.insert(String(num));
     }

     let cur = this.root;
     let result = [];
     this.dfs(cur, result);

     let intResult = [];
     for (let num of result) {
         intResult.push(parseInt(num));
     }

     return intResult;
 }
 }

 let solution = new Solution();
 return solution.lexicalOrder(n);

};

