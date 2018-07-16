class Stack(object):

    def __init__(self, value):
        self.size = None
        self.l = []

        for i in range(value):
            self.l.append(i)

    def length(self):

        return len(self.l)

    def pop(self):
        self.size = len(self.l)
        if self.size > 0:
            self.l.pop()

            return self.l

    def append(self, params):
        self.l.append(params)
        return self.l


def main():
    stack = Stack(5)
    print(stack.append('shan'))


if __name__ == '__main__':
    main()










