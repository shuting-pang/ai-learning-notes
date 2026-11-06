"""In-place bubble sort, without an early-exit optimization."""


def Bubbles(nums):
    n = len(nums)
    for i in range(n):
        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


if __name__ == "__main__":
    nums = [int(value.strip()) for value in input().split(",") if value.strip()]
    print(",".join(map(str, Bubbles(nums))))
