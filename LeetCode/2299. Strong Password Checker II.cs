public class Solution {
    public bool StrongPasswordCheckerII(string password) {
        bool lower = false;
        bool upper = false;
        bool digit = false;
        bool special = false;
        string specialChar = "!@#$%^&*()-+";
        if(password.Length < 8)
            return false;
        for (int i = 1; i <= password.Length; i++){
            if(Char.IsUpper(password[i-1]))
                upper = true;
            if(Char.IsLower(password[i-1]))
                lower = true;
            if(Char.IsDigit(password[i-1]))
                digit = true;
            if (specialChar.Contains(password[i-1]))
                special = true;
            if(i == password.Length)
                continue;
            if(password[i].Equals(password[i-1]))
                return false;
            
        }

        if(lower && upper && digit && special)
            return true;
        return false;
    }
}