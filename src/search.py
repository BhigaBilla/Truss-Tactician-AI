import heapq

def a_star(env, start, goal):
    pq = [(0, start)]
    came_from = {start: None}
    cost_so_far = {start: 0}
    nodes_expanded = 0

    while pq:
        _, current = heapq.heappop(pq)
        nodes_expanded += 1
        if current == goal: break
        
        for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
            nxt = (current[0]+dx, current[1]+dy)
            if env.is_valid(nxt):
                new_cost = cost_so_far[current] + 1
                if nxt not in cost_so_far or new_cost < cost_so_far[nxt]:
                    cost_so_far[nxt] = new_cost
                    # Manhattan Distance Heuristic
                    priority = new_cost + abs(nxt[0]-goal[0]) + abs(nxt[1]-goal[1])
                    heapq.heappush(pq, (priority, nxt))
                    came_from[nxt] = current
    return came_from, nodes_expanded
