from collections import deque

class TreeOps:
    
    class TreeNode:
        def __init__(self, val : str):
            self.val = val
            self.left = None
            self.right = None

        def leftIns(self, node: 'TreeOps.TreeNode'):
            self.left = node

        def rightIns(self, node: 'TreeOps.TreeNode'):
            self.right = node  


    def depth(self, node: TreeNode):
        if node == None:
            return 0
        
        return 1 + max(self.depth(node.left), self.depth(node.right))
        

    def dfs(self, node: TreeNode):
        if node == None:
            return 0    
        stack = [node]
        level = 0
        while stack:
            level = level+1
            n = stack.pop()
            if n == None:
                continue
            print(n.val+"\n")
            stack.append(n.left)
            stack.append(n.right)
        return level 



        
    def bfs(self, node: TreeNode):
        if node == None:
            return 0   
        
        queue = deque()
        queue.append(node)
        level = 0
        while queue:
            level = level + 1
            node = queue.popleft()
            if node is None:
                continue
            
            print(node.val+"\n")
            queue.append(node.left)
            queue.append(node.right)

        return level            

root = TreeOps.TreeNode(1)
l = TreeOps.TreeNode(2)
r = TreeOps.TreeNode(3)
l.leftIns(TreeOps.TreeNode(4))
l.rightIns(TreeOps.TreeNode(5))
r.leftIns(TreeOps.TreeNode(6))
r.rightIns(TreeOps.TreeNode(7))
root.leftIns(l)
root.rightIns(r)

ops = TreeOps()
print(ops.depth(root))
print(ops.dfs(root))