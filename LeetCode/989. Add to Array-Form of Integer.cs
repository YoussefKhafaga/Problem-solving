public class Solution {
    public IList<int> AddToArrayForm(int[] num, int k) {
        int carry = 0;
        int knum = 0;
        int i = num.Length-1;
        while(k > 0 && i >= 0){
            knum = k % 10;
            k = k / 10;
            num[i] = num[i] + knum;
            if(carry > 0){
                num[i] = num[i] + carry;
                carry = 0;
            }
            if(num[i] > 9){
                num[i] = num[i] % 10;
                carry = 1;
            }
            i--;
        }
        while(i >= 0){
            if(carry == 0)
                break;
            num[i] = num[i] + 1;
            carry = 0;
            if(num[i] > 9){
                num[i] = num[i] % 10;
                carry = 1;}
            
            i--;
        }
        var numlist = new List<int>(num);
        while(k > 0)
        {   
            Console.WriteLine(k);
            knum = k % 10;
            k = k / 10;
            if(carry == 1){
                if(1+knum > 9){
                    carry = 1;
                    numlist.Insert(0, (1+knum)%10);
                }
                else{
                    numlist.Insert(0, 1+knum);
                    carry = 0;
                }
                continue;
            }
            
            numlist.Insert(0, knum);
            
        }
        if(carry > 0){
            numlist.Insert(0, 1);
        }
        return numlist;
    }
}