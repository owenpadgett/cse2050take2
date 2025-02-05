import time

def time_function(func, args, n_trials=10) -> float:
    """Tests function runtime in n trials"""
    best_trial = float('inf')
    for i in range(n_trials):
        time_offset = time.time()
        func(args)
        best_trial = min(time.time()-time_offset, best_trial)
    return best_trial
    
def time_function_flexible(func, args, n_trials=10):
    """returns best runtime of the function over n_trials, arguments must be packed in a tuple"""
    best_trial = float('inf')
    for i in range(n_trials):
        time_offset = time.time()
        func(*args)
        best_trial = min(time.time()-time_offset, best_trial)
    return best_trial

if __name__ == '__main__':
    # Some tests to see if time_function works
    def test_func(L):
        for item in L:
            item *= 2

    L1 = [i for i in range(10**5)]
    t1 = time_function_flexible(test_func, tuple(L1))

    L2 = [i for i in range(10**6)] # should be 10x slower to operate on every item
    t2 = time_function_flexible(test_func, tuple(L2))

    print("t(L1) = {:.3g} ms".format(t1*1000))
    print("t(L2) = {:.3g} ms".format(t2*1000))