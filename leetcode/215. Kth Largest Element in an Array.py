class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr=[]
        for i in range(k):
            arr.append(nums[i])
        heapq.heapify(arr)
        for i in range(k,len(nums)):
            if nums[i]>arr[0]:
                heapq.heappop(arr)
                heapq.heappush(arr,nums[i])
        return arr[0]
