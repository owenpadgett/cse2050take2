def trib(k):
    return _trib(k, {1:0, 2:0, 3:1})

def _trib(k, dict):
    if k in dict:
        return dict[k]
    else:
        dict[k] = _trib(k-1, dict)+_trib(k-2, dict)+_trib(k-3, dict)
        return dict[k]