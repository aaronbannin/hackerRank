/* Node is defined as :
class Node
   int data;
   Node left;
   Node right;

   */

static Node Insert(Node root,int value)
{
   Node newNode = new Node();
   newNode.data = value;

   if(root == null) {
       return newNode;
   }

   Node nextNode = root;
   while(true) {
       if(nextNode.data > newNode.data) {
           if(nextNode.left == null) {
               nextNode.left = newNode;
               return root;
           } else {
               nextNode = nextNode.left
           }
       } else {
           if(nextNode.right == null) {
               nextNode.right = newNode;
               return root;
           } else {
               nextNode = nextNode.right
           }
       }
   }
}





static Node Insert(Node root, int value) {
    /* Create new Node */
    Node newNode = new Node();
    newNode.data = value;

    /* Special case: empty tree */
    if (root == null) {
        return newNode;
    }

    /* Iteratively walk tree and insert new Node */
    Node curr = root;
    while (true) {
        if (value <= curr.data) {
            if (curr.left == null) {
                curr.left = newNode;
                return root;
            } else {
                curr = curr.left;
            }
        } else {
            if (curr.right == null) {
                curr.right = newNode;
                return root;
            } else {
                curr = curr.right;
            }
        }
    }
}
