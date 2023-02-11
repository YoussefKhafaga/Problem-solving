public class Solution {
    public char NextGreatestLetter(char[] letters, char target) {
        int low = 0, high = letters.Length;
        while(low < high){
            int mid = (low + high)/2;
            if(letters[mid] > target){
                high = mid;
            }
            else{
                low = mid + 1;
            }
        }
        return letters[low % letters.Length];

    }
}