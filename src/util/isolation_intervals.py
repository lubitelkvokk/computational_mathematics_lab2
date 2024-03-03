def get_isolation_intervals(a: float, b: float, step: float, func):
    pointer = a
    intervals = []
    while pointer <= b:
        if func(pointer + step) * func(pointer) <= 0:
            intervals.append([pointer, pointer + step])
        pointer += step
    return intervals
