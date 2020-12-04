import unittest
from src.list_remove import Node, remove
class TestListMove(unittest.TestCase):
    """
    在jianzhi目录运行
    python3 -m unittest -v test.list_remove_test.TestListMove
    执行这个测试类
    """
    def generate_list(self, n: int):
        head = None
        for i in range(1, n+1):
            a = Node(i)
            a.next = head
            head = a
    
    def test_list_move(self):
        a = Node(1)
        b = Node(2)
        c = Node(3)
        a.next = b
        b.next = c
        a.show() # 1->2->3
        a= remove(a, b)
        a.show() # 1->3
        a = remove(a, c)
        a.show() #1
        a= remove(a, a)




if __name__ == "__main__":
    unittest.main()
    
