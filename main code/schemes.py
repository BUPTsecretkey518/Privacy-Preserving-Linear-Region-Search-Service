from buildtree import *
from linear_region_search import *
from encryption import *
import time


def plaSearch(fileName):

    d = 100

    root = genRoot(fileName)
    x_lim = [root.region.ll.x, root.region.ur.x]
    y_lim = [root.region.ll.y, root.region.ur.y]
    buildQuadtree(root, d)

    # q1 = Point(random.uniform(x_lim[0] - 1, x_lim[1] + 1), random.uniform(y_lim[0] - 1, y_lim[1] + 1))
    # q2 = Point(random.uniform(x_lim[0] - 1, x_lim[1] + 1), random.uniform(y_lim[0] - 1, y_lim[1] + 1))

    q1 = Point(11694.91, 3982.42)
    q2 = Point(11637.99, 4035.39)
    query = Segment(q1, q2)

    result = []

    linearRegionSearch(query, root, result)

    return result


def lrs_1(root, sk, TR):
    """

    :param root:
    :param sk:
    :param TR:
    :return: the results of l1 scheme
    """

    startForEnctree = time.time()
    encQuadTree(root, sk)
    endForEnctree = time.time()

    result = []

    # search
    startForSearch = time.time()
    secureSearch(TR, root, result)
    endForSearch = time.time()

    print("time for enc quadtree for lrs_1: ", endForEnctree - startForEnctree)
    print("time for search for lrs_1: ", endForSearch - startForSearch)

    return result


def lrs_11(root, sk, TRs):
    """

    :param root:
    :param sk:
    :param TRs:
    :return: the results of l1 scheme
    """

    encQuadTree(root, sk)

    count = 0
    times = []
    lens = []

    # search
    for TR in TRs:

        result = []
        startForSearch = time.time()
        secureSearch(TR, root, result)
        endForSearch = time.time()
        temp1 = endForSearch - startForSearch
        temp2 = len(result)
        print(str(count) + ": time for search for lrs_1: ", temp1)
        print(str(count) + ": length for search for lrs_1: ", temp2)
        count += 1
        times.append(temp1)
        lens.append(temp2)

    print("average time: ", sum(times) / len(times))
    print("average com: ", sum(lens) / len(lens))


def lrs_2(root, sk, TR, d):
    maxHeight = getMaxHeight(root)
    enhanceTree(root, d, maxHeight)

    startForEnctree = time.time()
    encQuadTree(root, sk)
    endForEnctree = time.time()

    result = []

    # search
    startForSearch = time.time()
    secureSearch(TR, root, result)
    endForSearch = time.time()

    print("time for enc quadtree for lrs_2: ", endForEnctree - startForEnctree)
    print("time for search for lrs_2: ", endForSearch - startForSearch)

    return result


def lrs_22(root, sk, TRs, d):

    maxHeight = getMaxHeight(root)
    enhanceTree(root, d, maxHeight)

    encQuadTree(root, sk)

    count = 0
    times = []
    lens = []

    for TR in TRs:
        result = []

        startForSearch = time.time()
        secureSearch(TR, root, result)
        endForSearch = time.time()
        temp1 = endForSearch - startForSearch
        temp2 = len(result)
        print(str(count) + ": time for search for lrs_2: ", temp1)
        print(str(count) + ": length for search for lrs_2: ", temp2)
        count += 1
        times.append(temp1)
        lens.append(temp2)

    print("average time: ", sum(times)/len(times))
    print("average com: ", sum(lens) / len(lens))
