public class Solution {
    public int MaxDepth(TreeNode root) {
        
        if(root is null){
            return 0;
        }


        return Math.Max(MaxDepth(root.left), MaxDepth(root.right)) + 1;
    }
}