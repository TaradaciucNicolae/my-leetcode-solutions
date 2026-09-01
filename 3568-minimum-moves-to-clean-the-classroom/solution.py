class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        rows = len(classroom)
        cols = len(classroom[0])
        litters = []

        for row in range(rows):
            for column in range(cols):

                value = classroom[row][column]

                if value == "S": 
                    start = (row,column)
                elif value == "L": 
                    litters.append((row,column))

            
        num_litters = len(litters)
        all_collected = (1 << num_litters) - 1 # e.g. 3 litters: 1 << 3 = 1000, minus 1 = 0111 (all 3 bits set = all collected)
        litter_index = {}
        for i, pos in enumerate(litters):
            litter_index[pos] = i
        
        start_state = (start[0], start[1], energy, 0)

        queue = deque()
        queue.append((start_state, 0)) #current_state and numbers_of_moves

        max_energy_at = {}
        # key: (row, col, collected_bitmask) -> max energy seen at this state
        max_energy_at[(start[0], start[1], 0)] = energy

        while queue:

            (r,c, curr_energy, collected), moves = queue.popleft()

            if collected == all_collected: 
                return moves

            for direction_row, direction_column in [(-1,0), (1,0), (0,-1), (0,1)]:
                new_r, new_c = r + direction_row , c + direction_column

                if not ( 0<= new_r < rows and 0<= new_c < cols ):  
                    continue
                if classroom[new_r][new_c] == "X": 
                    continue
                if curr_energy == 0: 
                    continue

                new_energy = curr_energy - 1
                new_collected = collected

                if classroom[new_r][new_c] == "R": 
                    new_energy = energy # reset to max
                
                if classroom[new_r][new_c] == "L":
                    i = litter_index[(new_r, new_c)]
                    new_collected = collected | (1 << i) # mark the i litter as collected
                
                new_state = (new_r, new_c, new_energy, new_collected)

                key = (new_r, new_c, new_collected)
                if new_energy > max_energy_at.get(key, -1):  # .get(key, -1) returns -1 if key not seen yet
                    max_energy_at[key] = new_energy
                    queue.append((new_state, moves + 1))
                            
        return -1
