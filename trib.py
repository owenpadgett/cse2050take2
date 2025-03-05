def trib(k):
    """Returns k-th number of the tribonacci sequence"""
    return _trib(k, {1:0, 2:0, 3:1})

def _trib(k, dict):
    """Helper function: Return k-th number of the tribonacci sequence"""
    if k in dict:
        return dict[k]
    else:
        dict[k] = _trib(k-1, dict)+_trib(k-2, dict)+_trib(k-3, dict)
        return dict[k]