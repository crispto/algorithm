class Calculator():
    operators = ["+", "-", "*", "/"]
    def __init__(self):
        self.buffer = ""
        self.show_type = 0

    def show(self):
        """
        打印当前数字
        -- ------------------------
        一百零五十
        -----------------------------
        [n: 数字] [c: 中文] [ac: 清屏][q:退出]
        [0-9] 数字
        [+ - * /]
        """
            
        width, height = 20, 100
        def show_line(v):
            for i in range(width):
                print(v, end="")
            print()
        show_line('+')
        print("+     calculator   +")
        show_line('-')
        b =  "0" if self.buffer == ""  else self.buffer
        print(b)
        show_line('-')
        print("[n: 数字] [c: 中文] \n[ac: 清屏][q:退出][e:=]")
        show_line('-')
        print()
        print()
        print()

    def cal(self):
        """
        计算，如果前面缺操作数，补0， 后面缺操作数，不变
        1 + 2
        """
        b = self.buffer
        i = 0
        while i < len(b):
            if b[i] in self.operators:
                break
            i+=1
        if i == len(b):
            # 不存在
            return b
        if i == 0:
            #缺少操作数
            b = '0'+b
        x = b[:i]
        y = b[i+1:]
        x1 = float(x)
        y1= float(y)
        v = 0
        if b[i] == "+":
            v = x1 +y1
        if b[i] == "-":
            v = x1 - y1
        if b[i] == "*":
            v = x1 * y1
        if b[i] == "/":
            v = x1 / y1
        self.buffer = str(v)

    def control(self, v: str):
        """
        读取当前显示的数字然后更新buffer
        """
        if v == "ac": # clear screen
            self.buffer = "0"
            self.show()
        elif v == "=":
            self.cal()
            self.show()
        elif v in ["+", "-", "*", "/"]:
            self.cal()
            self.buffer += v
            self.show()
        elif v == "n": # 阿拉伯数字
            self.show_type = 0
            self.show()
        elif v == "c": # 中国文字
            self.show_type = 1
            self.show()
        else:
            self.buffer+=v
            self.show()

def main():
    c = Calculator()
    c.show()
    while True:
        v = input()
        print(v)
        if v == "q": # quit
            return
        else:
            c.control(v)
        
        
if __name__ == "__main__":
    main()


