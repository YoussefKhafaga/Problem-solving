public class Solution {
    public int RomanToInt(string s) {
        Dictionary<char, int> dict = new Dictionary<char, int>();
        dict.Add('I', 1);
        dict.Add('V', 5);
        dict.Add('X', 10);
        dict.Add('L', 50);
        dict.Add('C', 100);
        dict.Add('D', 500);
        dict.Add('M', 1000);
        int sum = 0;
        for(int i = 0; i < s.Length; i++){
            if( i < s.Length - 1 && dict[s[i]] < dict[s[i+1]])
                sum = sum - dict[s[i]];
            else
                sum = sum + dict[s[i]];
        }
        return sum;
    }
}