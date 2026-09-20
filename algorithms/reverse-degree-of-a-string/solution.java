class Solution {
    public int reverseDegree(String s) {
        

        int sum = 0;

        for (int i = 0; i < s.length(); i++) {

            char ch = s.charAt(i);

            int reverseValue = 'z' - ch + 1;

            int position = i + 1;

            sum += reverseValue * position;
        }

        return sum;
    
        
    }
}