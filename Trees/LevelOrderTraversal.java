/*

 class Node
    int data;
    Node left;
    Node right;
*/
void LevelOrder(Node root)
{
    //Node[] queue = {root};
    Queue queue = new LinkedList();
    queue.add(root);
    while(queue.peek() != null) {
        Object obj = queue.remove();
        if(obj instanceof Node) {
            Node node = (Node) obj;
            System.out.print(node.data + " ");
            if(node.left != null) {
                queue.add(node.left);
            }
            if(node.right != null) {
                queue.add(node.right);
            }
        }
    }
}
