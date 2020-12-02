"""
实现 avl树
"""
class Node:
    def __init__(self):
        self.root =None

    def get_height(self):
        """
        获取树高度
        """
        pass

    def insert(self, value):
        """
        插入值
        """
        pass
    
    def del_node(self, node):
        """
        删除节点
        """
        pass
   
    def __str__(self):
        """
        打印树
        """

def display(tree):
    if tree:
        display(tree.left)
        print(tree.data)
        display(tree.right)