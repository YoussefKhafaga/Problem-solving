public class Solution {
    public int MaximumWealth(int[][] accounts) {
        int maxx = 0;
        int summ = 0;
        for(int i = 0; i < accounts.Length; i++){
            if(accounts[i] is null)
                continue;
            summ = accounts[i].Sum();
            if (summ > maxx)
                maxx = summ;
        }
        return maxx;
    }
}