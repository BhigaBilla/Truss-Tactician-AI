def check_collision_constraint(next_pos, other_drone_pos):
    """
    Implements a simple Forward Checking CSP rule.
    """
    # Safety buffer of 1 grid unit
    if abs(next_pos[0] - other_drone_pos[0]) <= 1 and \
       abs(next_pos[1] - other_drone_pos[1]) <= 1:
        return False # Constraint Violated
    return True
