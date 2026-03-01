def clock_helper(total_seconds):
    """Helper function for a clock

    Args:
        total_seconds (integer): seconds to convert to minute
    """
    seconds_in_minute = total_seconds % 60

print(clock_helper(90)) # Returns None since there is not return for seconds_in_minute in clock_helper
