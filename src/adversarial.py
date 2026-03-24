def evaluation_function(drone_pos, opponent_pos, defects):
    """
    Standard Heuristic: Mechanical Value - My Cost + Opponent Disadvantage.
    Used by Minimax to evaluate leaf nodes.
    """
    scores = {}
    for d_pos, val in defects.items():
        # Manhattan Distances
        dist = abs(drone_pos[0]-d_pos[0]) + abs(drone_pos[1]-d_pos[1])
        opp_dist = abs(opponent_pos[0]-d_pos[0]) + abs(opponent_pos[1]-d_pos[1])
        
        # Scoring Formula: Priority weight adjusted by proximity
        scores[d_pos] = val - (dist * 1.5) + (opp_dist * 0.5)
    
    return scores

def minimax_alpha_beta(drone_pos, opponent_pos, defects, depth, alpha, beta, is_maximizing):
    """
    Minimax with Alpha-Beta Pruning for strategic target selection.
    """
   
    if depth == 0 or not defects:
        scores = evaluation_function(drone_pos, opponent_pos, defects)
        return max(scores.values()) if scores else 0, None

    best_target = None

    if is_maximizing:
        max_eval = -float('inf')
        for target in list(defects.keys()):
            # Simulate picking this target
            remaining = {k: v for k, v in defects.items() if k != target}
            eval_score, _ = minimax_alpha_beta(target, opponent_pos, remaining, depth - 1, alpha, beta, False)
            
            if eval_score > max_eval:
                max_eval = eval_score
                best_target = target
            
            alpha = max(alpha, eval_score)
            if beta <= alpha:
                break # Alpha-Beta Pruning
        return max_eval, best_target

    else:
        min_eval = float('inf')
        for target in list(defects.keys()):
            remaining = {k: v for k, v in defects.items() if k != target}
            eval_score, _ = minimax_alpha_beta(drone_pos, target, remaining, depth - 1, alpha, beta, True)
            
            if eval_score < min_eval:
                min_eval = eval_score
                best_target = target
            
            beta = min(beta, eval_score)
            if beta <= alpha:
                break # Alpha-Beta Pruning
        return min_eval, best_target