from typing import List

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Merges nums2 into nums1 in-place, assuming nums1 has enough space at the end.
    """
    i = m + n - 1  # Last index of nums1
    j = m - 1  # Last valid index in nums1 before merge
    k = n - 1  # Last index in nums2

    while k >= 0:
        if j >= 0 and nums1[j] > nums2[k]:
            nums1[i] = nums1[j]
            j -= 1
        else:
            nums1[i] = nums2[k]
            k -= 1
        i -= 1

if __name__ == "__main__":
    # Test case
    nums1 = [1, 2, 3, 0, 0, 0]  # nums1 has extra space for merging
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    
    print("Before merging:", nums1)
    merge(nums1, m, nums2, n)
    print("After merging:", nums1)