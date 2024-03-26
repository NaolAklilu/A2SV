/**
 * @param {number[][]} bombs
 * @return {number}
 */

function detonate(bomb, graph, visited) {
    visited.add(bomb);
    let count = 1;

    if (bomb in graph) {
        for (let neighbor of graph[bomb]) {
            if (!visited.has(neighbor)) {
                count += detonate(neighbor, graph, visited);
            }
        }
    }

    return count;
}

var maximumDetonation = function(bombs) {
    let graph = {};
    let bombDic = {};

    for (let i = 0; i < bombs.length; i++) {
        bombDic[i + 1] = bombs[i];
    }

    for (let i = 1; i <= bombs.length; i++) {
        for (let j = 1; j <= bombs.length; j++) {
            if (i != j) {
                let diff = Math.sqrt(Math.pow(bombDic[i][0] - bombDic[j][0], 2) + Math.pow(bombDic[i][1] - bombDic[j][1], 2));
                if (diff <= bombDic[i][2]) {
                    if (!graph[i]) {
                        graph[i] = [];
                    }
                    graph[i].push(j);
                }
            }
        }
    }

    let maxCount = 0;
    for (let i = 1; i <= bombs.length; i++) {
        let visited = new Set();
        let curCount = detonate(i, graph, visited);
        maxCount = Math.max(curCount, maxCount);
    }

    return maxCount;
};