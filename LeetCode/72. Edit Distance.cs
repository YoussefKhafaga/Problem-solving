public class Solution {
    public int MinDistance(string word1, string word2) {
        int[ , ] x = new int [word1.Length + 1, word2.Length + 1];
        for(int i = 0; i < word2.Length + 1; i++){
            x[word1.Length, i] = word2.Length - i; 
        }
        for(int i = 0; i < word1.Length + 1; i++){
            x[i, word2.Length] = word1.Length - i; 
        }
        for (int i = word1.Length - 1; i >= 0; i--){
            for(int j = word2.Length - 1; j >= 0; j--){
                if(word1[i] == word2[j])
                    x[i, j] = x[i + 1, j + 1];
                else
                    x[i, j] = 1 + Math.Min(x[i+1, j], Math.Min(x[i, j+1], x[i+1, j+1]));
            }
        }
        return x[0, 0];
        
    }
}