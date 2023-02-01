public class Solution {

    int GCD(int x, int y)
    {
        if (y == 0)
        {
            return x;
        }
        else
        {
            return GCD(y, x % y);
        }
    }

    public string GcdOfStrings(string str1, string str2) 
    {
        if (str1 + str2 != str2 + str1)
        {
            return "";
        }

        int gcdLength = GCD(str1.Length, str2.Length);

        return str1.Substring(0, gcdLength);
    }
}