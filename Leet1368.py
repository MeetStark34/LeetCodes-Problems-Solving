#1368. Minimum Cost to Make at Least One Valid Path in a Grid

from collections import deque

class Solution:
    def minCost(self, grid):
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Directions: right, left, down, up
        queue = deque([(0, 0, 0)])  # (row, col, cost)
        visited = [[False] * n for _ in range(m)]

        while queue:
            x, y, cost = queue.popleft()

            # Skip if already visited
            if visited[x][y]:
                continue
            visited[x][y] = True

            # If we've reached the bottom-right corner
            if x == m - 1 and y == n - 1:
                return cost

            # Explore all directions
            for i, (dx, dy) in enumerate(directions):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    # If the direction matches, no cost; otherwise, cost is +1
                    if i + 1 == grid[x][y]:
                        queue.appendleft((nx, ny, cost))  # Priority to no-cost paths
                    else:
                        queue.append((nx, ny, cost + 1))  # Higher cost paths later
        return -1