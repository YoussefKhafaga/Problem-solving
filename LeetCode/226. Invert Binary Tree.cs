public class Solution {
    TreeNode temp;
    public TreeNode InvertTree(TreeNode root) {
        if(root == null)
            return null;
        InvertTree(root.left);
        InvertTree(root.right);
        temp = root.left;
        root.left = root.right;
        root.right = temp;
        return root;
    }
}