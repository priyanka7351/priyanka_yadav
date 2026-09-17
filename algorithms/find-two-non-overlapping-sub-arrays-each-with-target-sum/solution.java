class Solution {
    public int minSumOfLengths(int[] arr, int target) {
    

        int n = arr.length;
        int INF = Integer.MAX_VALUE / 2;

        // best[i] = minimum length of a valid subarray
        // completely inside arr[0...i]
        int[] best = new int[n];

        Arrays.fill(best, INF);

        int left = 0;
        int sum = 0;
        int answer = INF;

        for (int right = 0; right < n; right++) {

            sum += arr[right];

            // Reduce window if sum becomes greater than target
            while (sum > target && left <= right) {
                sum -= arr[left];
                left++;
            }

            // If current subarray has sum = target
            if (sum == target) {

                int currentLength = right - left + 1;

                // Check if there is a previous non-overlapping subarray
                if (left > 0 && best[left - 1] != INF) {
                    answer = Math.min(
                        answer,
                        currentLength + best[left - 1]
                    );
                }

                // Store minimum valid subarray ending before/right here
                best[right] = currentLength;
            }

            // Carry forward the best previous answer
            if (right > 0) {
                best[right] = Math.min(best[right], best[right - 1]);
            }
        }

        return answer == INF ? -1 : answer;
    }
}
    