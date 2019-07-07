class A(object):
    def __init__(self, val):
        self.val = val
        print(val)

    @staticmethod
    def tm():
        return 1


def get_class(label):
    if label == "a":
        print("getting label class")
        return A

cl = get_class("a")
cl(10)