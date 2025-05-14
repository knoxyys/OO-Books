class ParentClass:
    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1
        self.attribute2 = attribute2

    def method1(self):
        return "Parent method 1"

class ChildClass(ParentClass):
    def __init__(self, attribute1, attribute2, attribute3):
        super().__init__(attribute1, attribute2)
        self.attribute3 = attribute3
    
    def method2(self):
        return "Child method 2"