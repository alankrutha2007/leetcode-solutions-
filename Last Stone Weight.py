

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        def heapifyDown(arr, index, size):
            largest = index
            lchild = 2 * index + 1
            rchild = 2 * index + 2

            if lchild < size and arr[lchild] > arr[largest]:
                largest = lchild
            if rchild < size and arr[rchild] > arr[largest]:
                largest = rchild

            if largest != index:
                arr[index], arr[largest] = arr[largest], arr[index]
                heapifyDown(arr, largest, size)

        def buildMaxHeap(arr):
            size = len(arr)
            for i in range(size // 2 - 1, -1, -1):
                heapifyDown(arr, i, size)

        def extractMax(arr):
            size = len(arr)
            if size == 0:
                return 0
            arr[0], arr[size - 1] = arr[size - 1], arr[0]
            max_val = arr.pop()
            heapifyDown(arr, 0, len(arr))
            return max_val

        # Build heap
        buildMaxHeap(stones)

        # Process stones
        while len(stones) > 1:
            y= extractMax(stones)
            x= extractMax(stones)

            if y!=x:
                stones.append(y-x)
                # Fix heap after insertion
                buildMaxHeap(stones)
        if stones:
            return stones[0]
        else:
            return 0
