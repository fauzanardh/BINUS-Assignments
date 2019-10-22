class M:
    def __init__(self):
        self.M = "M"
        super(M, self).__init__()


class A(M):
    def __init__(self):
        self.A = "A"
        super(A, self).__init__()


class B(M):
    def __init__(self):
        self.B = "B"
        super(B, self).__init__()


class Z(B, M):
    def __init__(self):
        self.Z = "Z"
        super(Z, self).__init__()


class Y(A, B):
    def __init__(self):
        self.Y = "Y"
        super(Y, self).__init__()


class X(A):
    def __init__(self):
        self.X = "X"
        super(X, self).__init__()


class Object(X, Y, Z):
    def __init__(self):
        self.Object = "Object"
        super(Object, self).__init__()


x = Object()
print(dir(x))
