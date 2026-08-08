class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = {0}
        queue = [0]

        while queue:
            room = queue.pop(0)

            for key in rooms[room]:
                if key not in visited:
                    visited.add(key)
                    queue.append(key)
            
            if len(visited) == len(rooms):
                return True

        return False
