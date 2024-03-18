# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def serial(node):
            if node:
                vals.append(str(node.val))
                serial(node.left)
                serial(node.right)
            else:
                vals.append('$')
        vals = []
        serial(root)
        return ' '.join(vals)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def deserial():
            val = next(vals)
            if val == '$':
                return None
            node = TreeNode(int(val))
            node.left = deserial()
            node.right = deserial()
            return node
        
        vals = iter(data.split())
        return deserial()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))