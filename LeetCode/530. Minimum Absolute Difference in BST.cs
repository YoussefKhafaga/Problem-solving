public class Solution {
    int minimum = int.MaxValue;
    TreeNode prev = null;
    public void inordertraversal(TreeNode root){
        if(root == null)
            return;
        inordertraversal(root.left);
        if(prev != null)
            minimum = Math.Min(minimum, Math.Abs( root.val - prev.val ));
        prev = root;
        inordertraversal(root.right);


    }
    public int MinDiffInBST(TreeNode root) {
        inordertraversal(root);
        return minimum;
    }
}