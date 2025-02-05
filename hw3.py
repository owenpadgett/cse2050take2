import random
import time

def generate_lists(size):
    if size == 0:
        return ([], [])
    return (random.sample(range(2*size), size), random.sample(range(2*size), size))

def find_common(list1, list2):
    if list1 == [] or list2 == []: #+2
        return 0                   #+1
    list1.sort()                   #+nlogn
    list2.sort()                   #+nlogn
    
    len1 = len(list1)              #+2
    len2 = len(list2)              #+2

    common = 0                     #+1
    i = 0                          #+1
    j = 0                          #+1
    while i < len1 and j < len2:   #+2n*(4 + 
        if list1[i] == list2[j]:             #1   
            common += 1                      #+1
            i += 1                           #+1 
            j += 1                           #+1
        elif list1[i] > list2[j]:            #OR 2 (because comparison above)
            j += 1                           #+1
        else:                                # OR 2 (because of above comparisons)
            i += 1                           #+1
                                             #Worst case 2n*(4+4)
    return common                  #+1
    ###### Total : 11 + 16n + 2nlogn = O(nlogn)


def find_common_efficient(list1, list2):
    length = len(list1)         #+1
    s1 = set(list1)             #+n
    s2 = set(list2)             #+n
    omega = s1.union(s2)        #+2n
    return length*2-len(omega)  #+1+1+1+1
    #### Total = 5 + 4n = O(n)

def measure_time():
    l1, l2 = generate_lists(10)
    l3, l4 = generate_lists(100)
    l5, l6 = generate_lists(1000)
    l7, l8 = generate_lists(10000)
    l9, l0 = generate_lists(20000)

    times = []

    times.append(time.time())
    find_common(l1, l2)
    times.append(time.time())
    find_common(l3, l4)
    times.append(time.time())
    find_common(l5, l6)
    times.append(time.time())
    find_common(l7, l8)
    times.append(time.time())
    find_common(l9, l0)
    times.append(time.time())
    find_common_efficient(l1, l2)
    times.append(time.time())
    find_common_efficient(l3, l4)
    times.append(time.time())
    find_common_efficient(l5, l6)
    times.append(time.time())
    find_common_efficient(l7, l8)
    times.append(time.time())
    find_common_efficient(l9, l0)
    times.append(time.time())

    timeList = [times[i+1]-times[i] for i in range(10)]
    lenList = [10, 100, 1000, 10000, 20000]

    for i in range(5):
        print(f"List Length: {str(lenList[i])} | find_common Time (ns): {str(timeList[i]*1e9)} | find_common_efficient Time (ns): {str(timeList[i+5]*1e9)}")



if __name__ == "__main__":
    measure_time()

