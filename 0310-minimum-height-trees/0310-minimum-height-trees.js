/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {number[]}
 */
var findMinHeightTrees = function(n, edges) {
    const tree = {};
        const heights = {};
        const indegree = Array(n).fill(0);
        const visited = new Set();

        if (edges.length === 0) {
            return [0];
        }

        for (const [source, des] of edges) {
            if (!tree[source]) {
                tree[source] = [];
            }
            if (!tree[des]) {
                tree[des] = [];
            }
            tree[source].push(des);
            tree[des].push(source);
        }

        const queue = [];
        for (let i = 0; i < n; i++) {
            indegree[i] = tree[i] ? tree[i].length : 0;

            if (indegree[i] === 1) {
                visited.add(i);
                queue.push(i);
            }
        }

        while (queue.length > 0) {
            const length = queue.length;

            if (Math.max(...indegree) === 1) {
                return queue;
            }

            for (let i = 0; i < length; i++) {
                const node = queue.shift();

                for (const neighbor of tree[node]) {
                    indegree[neighbor] -= 1;

                    if (!visited.has(neighbor)) {
                        if (indegree[neighbor] <= 1) {
                            visited.add(neighbor);
                            queue.push(neighbor);
                        }
                    }
                }
            }
        }

        return [];
};