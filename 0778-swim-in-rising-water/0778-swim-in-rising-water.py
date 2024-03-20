class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = [[float('inf')]*n for _ in range(n)]
        heap = [(grid[0][0], 0, 0)]
        visited[0][0] = grid[0][0]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while heap:
            t, x, y = heapq.heappop(heap)
            if (x, y) == (n-1, n-1):
                return t
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] > max(t, grid[nx][ny]):
                    visited[nx][ny] = max(t, grid[nx][ny])
                    heapq.heappush(heap, (visited[nx][ny], nx, ny))

        return visited[n-1][n-1]