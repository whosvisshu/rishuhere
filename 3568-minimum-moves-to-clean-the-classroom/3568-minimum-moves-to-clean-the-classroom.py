from collections import deque
from typing import List

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        
        litter_pos = {}
        sr, sc = -1, -1
        
        # 1. Find the starting position and map each litter to a unique bit index
        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    sr, sc = r, c
                elif classroom[r][c] == 'L':
                    litter_pos[(r, c)] = len(litter_pos)
                    
        num_litter = len(litter_pos)
        target_mask = (1 << num_litter) - 1  # e.g., if 3 litter, target is 111 in binary (7)
        
        # 3D visited array: visited[r][c][mask] stores the maximum energy seen so far
        visited = [[[-1] * (target_mask + 1) for _ in range(n)] for _ in range(m)]
        visited[sr][sc][0] = energy
        
        # Queue stores: (moves, current_row, current_col, current_energy, current_mask)
        q = deque([(0, sr, sc, energy, 0)])
        
        while q:
            moves, r, c, cur_e, mask = q.popleft()
            
            # If all litter is collected, return the number of moves
            if mask == target_mask:
                return moves
            
            # If we are out of energy (and we weren't saved by an 'R' cell on arrival), we can't move
            if cur_e == 0:
                continue
                
            # Explore all 4 adjacent directions
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                
                # Check bounds and obstacles
                if 0 <= nr < m and 0 <= nc < n and classroom[nr][nc] != 'X':
                    next_e = cur_e - 1
                    next_mask = mask
                    
                    # If it's litter, update our bitmask
                    if classroom[nr][nc] == 'L':
                        next_mask |= (1 << litter_pos[(nr, nc)])
                        
                    # If it's a reset point, refill energy back to maximum capacity
                    if classroom[nr][nc] == 'R':
                        next_e = energy
                        
                    # If we found a strictly better path to this state (more energy remaining)
                    if next_e > visited[nr][nc][next_mask]:
                        visited[nr][nc][next_mask] = next_e
                        q.append((moves + 1, nr, nc, next_e, next_mask))
                        
        return -1
        