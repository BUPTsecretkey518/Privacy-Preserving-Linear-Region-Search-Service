class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class POI(object):
    def __init__(self, loc, iden):
        self.loc = loc
        self.id = iden


class Segment(object):
    """the 2 points p1 and p2 are unordered"""

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2


class Rectangle(object):
    """
    ll,lr,ur,ul are 4 points from: lower left, lower right, upper right, upper left
    """
    def __init__(self, ll, lr, ur, ul):
        self.ll, self.lr, self.ur, self.ul = ll, lr, ur, ul
        self.s1, self.s2 = Segment(ul, ll), Segment(ll, lr)
        self.s3, self.s4 = Segment(ur, lr), Segment(ul, ur)


class QuadtreeNode(object):
    """
    id: identification of quadtree node, generated by GenID();
    region: rectangle region;
    pointers: children;
    num: the number of poi objects contained in the tree node;
    """
    def __init__(self, rectangle, poi):

        self.id = self.GenID()
        self.region = rectangle
        self.pointers = []
        self.poi = poi
        self.isleaf = True
        self.encInfo = None
        self.height = 1

    def GenID(self):
        return id(self)

    def getNum(self):
        return len(self.poi)