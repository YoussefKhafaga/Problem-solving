public class Solution {
    public int CountTriples(int n) {
    int result = 0;
     for(int i = 1; i <= n; i++)
    {
        for(int j = i+1; j <= n; j++)
        {
            if ( Math.Sqrt(Math.Pow(i, 2) + Math.Pow(j, 2)) % 1 == 0)
                if( Math.Sqrt(Math.Pow(i, 2) + Math.Pow(j, 2)) <= n )
                    result ++;
                
        }
    }   
    return result*2;
    }
}