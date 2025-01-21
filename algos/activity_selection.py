# Greedy Algorithm: Activity Selection

def activity_selection(activities):
    """
    Given a list of (start, finish) times, select the maximum number of
    non-overlapping activities using a greedy strategy.
    """
    # Sort by finishing times
    activities.sort(key=lambda x: x[1])
    
    selected = []          # To store chosen activities
    last_finish_time = -1  # Track the finish time of last selected activity
    
    for activity in activities:
        start, finish = activity
        # If this activity starts after or at the finish time of the last one we picked
        if start >= last_finish_time:
            selected.append(activity)
            last_finish_time = finish  # Update finish time to this activity's finish
    
    return selected


# Example usage:
if __name__ == "__main__":
    acts = [(1, 4), (3, 5), (0, 6), (5, 7), (8, 9), (5, 9)]
    optimal = activity_selection(acts)
    print("Activities (start, finish):", acts)
    print("Selected (greedy):", optimal)
