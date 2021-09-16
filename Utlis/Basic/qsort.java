class Solution {
    private int[] arr;

    public int[] sortArray(int[] nums) {
        arr = nums;
        quickSort(arr);
        return arr;
    }

    private void quickSort(int[] nums) {
        int n = nums.length;
        qSort(nums, 0, n - 1);
    }

    private void qSort (int[] nums, int lo, int hi) {
        if (lo < hi) {
            int p = partition(nums, lo, hi);
            qSort(nums, lo, p -1);
            qSort(nums, p + 1, hi);
        }
    }

    private int partition(int[] nums, int lo, int hi) {
        int pivot = nums[hi];
        int i = lo;
        for (int j = lo; j < hi; ++j) {
            if (nums[j] < pivot) {
                int tmp = nums[i];
                nums[i] = nums[j];
                nums[j] = tmp;
                i++;
            }
        }
        int tmp = nums[i];
        nums[i] = nums[hi];
        nums[hi] = tmp;
        return i;
    }
}