class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def level_order_traversal(root):
    if not root:
        return
    
    queue = [root]
    
    while queue:
        current = queue.pop(0)
        print(current.key, end=" ")
        
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    print("Level-order Traversal:")
    level_order_traversal(root)

if __name__ == "__main__":
    main()
