
def get_max_triples(n):
    """
    You are given a positive integer n. You have to create an integer array a of length n.
        For each i (1 ≤ i ≤ n), the value of a[i] = i * i - i + 1.
        Return the number of triples (a[i], a[j], a[k]) of a where i < j < k, 
    and a[i] + a[j] + a[k] is a multiple of 3.

    Example :
        Input: n = 5
        Output: 1
        Explanation: 
        a = [1, 3, 7, 13, 21]
        The only valid triple is (1, 7, 13).
    """
    # Your code here
    # 1 3 7 13 21
    # 1 4 9 16 25
    # 1 5 10 17 26
    # 1 6 11 18 27
    # 1 7 12 19 28
    # 1 8 13 20 29
    # 1 9 14 21 30
    # 1 10 15 22 31
    # 1 11 16 23 32
    # 1 12 17 24 33
    # 1 13 18 25 34
    # 1 14 19 26 35
    # 1 15 20 27 36
    # 1 16 21 28 37
    # 1 17 22 29 38
    # 1 18 23 30 39
    # 1 19 24 31 40
    # 1 20 25 32 41
    # 1 21 26 33 42
