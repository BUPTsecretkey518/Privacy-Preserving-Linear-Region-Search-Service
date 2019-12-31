from readdata import *
import random
import copy


def genRoot(fileName):
    """

    generate the quadtree root
    :param fileName:
    :return: quadtree root
    """

    data = readData(fileName)

    # initializing the root rectangle
    ll = Point(12100, 3100)
    ur = Point(12197, 3141)
    ul = Point(ll.x, ur.y)
    lr = Point(ur.x, ll.y)

    root = QuadtreeNode(Rectangle(ll, lr, ur, ul), data)

    return root


def partition(region):
    """

    partition the rectangle region into 4 equal sub rectangle regions
    :param region: Rectangle object
    :return: a list contained by 4 Rectangle objects
    """
    center = Point((region.ll.x + region.ur.x) / 2, (region.ll.y + region.ur.y) / 2)

    subReg1 = Rectangle(region.ll, Point(center.x, region.ll.y), center, Point(region.ll.x, center.y))
    subReg2 = Rectangle(Point(center.x, region.ll.y), region.lr, Point(region.lr.x, center.y), center)
    subReg3 = Rectangle(center, Point(region.lr.x, center.y), region.ur, Point(center.x, region.ur.y))
    subReg4 = Rectangle(Point(region.ul.x, center.y), center, Point(center.x, region.ul.y), region.ul)

    return [subReg1, subReg2, subReg3, subReg4]


def pointInRec(point, rectangle):
    """

    determine whether the point in the rectangle
    :param point:
    :param rectangle:
    :return: True or False
    """
    return rectangle.ur.x >= point.x >= rectangle.ll.x and rectangle.ur.y >= point.y >= rectangle.ll.y


def buildQuadtree(root, d):
    """

    build quadtree
    :param root:
    :param d:
    :return: quadtree root
    """
    if root is None:
        return

    elif root.getNum() > d:

        root.isleaf = False
        subRegs = partition(root.region)

        # generate 4 children
        for i in range(4):
            # QuadtreeNode(rectangle, poi)
            child = QuadtreeNode(subRegs[i], [])

            # height + 1
            child.height = root.height + 1

            # append child to root pointers
            root.pointers.append(child)

        # distributing poi objects to 4 children
        while root.getNum() > 0:
            obj = root.poi[0]
            for i in range(4):
                if pointInRec(obj.loc, root.pointers[i].region):
                    root.pointers[i].poi.append(obj)
                    root.poi.remove(obj)
                    break

        for child in root.pointers:
            buildQuadtree(child, d)


def getMaxHeight(root):

    # get the maximum height of quadtree
    if root is None:
        return 0
    elif root.isleaf:
        return 1
    else:
        return max([getMaxHeight(root.pointers[i]) for i in range(4)]) + 1


def enhanceTree(root, d, maxHeight):

    if not root.isleaf:
        for child in root.pointers:
            enhanceTree(child, d, maxHeight)

    # case1: black nodes, leaf nodes in ordinary tree without height requirement
    elif root.isleaf and root.height < maxHeight:
        subRegs = partition(root.region)
        # generate 4 children
        for i in range(4):
            # QuadtreeNode(rectangle, poi)
            child = QuadtreeNode(subRegs[i], [])

            # height + 1
            child.height = root.height + 1

            child.poi = copy.deepcopy(root.poi)

            # append child to root pointers
            root.pointers.append(child)
            root.poi.clear()
            root.isleaf = False

        for child in root.pointers:
            enhanceTree(child, d, maxHeight)

    # leaf nodes in enhanced tree but without poi requirement
    elif root.height == maxHeight and root.getNum() < d:

        diff = d - root.getNum()
        dummies = [POI(None, "dummy") for i in range(diff)]
        root.poi.extend(dummies)

    else:
        return
