class Solution {
    public int[] sortArray(int[] nums) {
        return mergeSort(nums);
    }

    public int[] mergeSort(int[] nums) {
        if (nums.length <= 1) return nums;
        int pivot = nums.length / 2;
        int[] leftArr = mergeSort(Arrays.copyOfRange(nums, 0, pivot));
        int[] rightArr = mergeSort(Arrays.copyOfRange(nums, pivot, nums.length));
        return merge(leftArr, rightArr);
    }

    public int[] merge(int[] arr1, int[] arr2) {
        int[] res = new int[arr1.length + arr2.length];
        int l = 0, r = 0;
        while (l < arr1.length && r < arr2.length) {
            if (arr1[l] <= arr2[r]) {
                res[l + r] = arr1[l];
                l++;
            } else {
                res[l + r] = arr2[r];
                r++;
            }
        }
        
        while (l < arr1.length) {
            res[l + r] = arr1[l];
            l++;
        }
        
        while (r < arr2.length) {
            res[l + r] = arr2[r];
            r++;
        }
        
        return res;
        
    }
}