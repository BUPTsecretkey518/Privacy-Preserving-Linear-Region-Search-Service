from ext_algorithm import *


def genSK(m):

    s = np.random.randint(0, 2, size=m + 3)
    M1, M2 = np.random.randint(0, 5, size=(m + 3, m + 3)), np.random.randint(0, 5, size=(m + 3, m + 3))

    pos1, pos2 = random.randint(0, m), random.randint(0, m)

    return s, M1, M2, pos1, pos2


def splitForServer(ndVal, s):

    n = len(s)
    res1, res2 = np.zeros(n), np.zeros(n)

    for index in range(n):
        if s[index] == 0:
            res1[index], res2[index] = ndVal[index], ndVal[index]
        else:
            res2[index] = random.randint(-10, 10)
            res1[index] = ndVal[index] - res2[index]

    return res1, res2


def encNode(node, m, sk):

    s = sk[0]

    M1, M2 = sk[1], sk[2]

    # serverExt: four tuples contained seven elements
    serverExt = extendTreeNode(node, m, sk)

    # encInfo: consist of 4 dictionaries, each of them represented a side of the rectangle
    # each dictionary contained 7 pairs, name:element;
    node.encInfo = []

    for seven_tuple in serverExt:

        temp = {}
        names = ["ext1_p1*", "ext1_p2*", "ext2_p1*", "ext2_p2*", "ext3_p1*", "ext3_p2*", "ext3_Ds*"]

        for index in range(7):

            splitRes = splitForServer(np.array(seven_tuple[index]), s)
            item1, item2 = np.transpose(M1) @ splitRes[0], np.transpose(M2) @ splitRes[1]
            temp[names[index]] = (item1, item2)

        node.encInfo.append(temp)


def encQuadTree(root, sk):

    Next = True
    curNodeList = [root]
    m = len(sk[0]) - 3

    while Next:

        tempNodeList = []
        Next = False

        for node in curNodeList:

            # in fact, assign the attribute encInfo of node
            encNode(node, m, sk)

            # append all children of the node into tempNodeList
            if not node.isleaf:
                Next = True
                for child in node.pointers:
                    tempNodeList.append(child)

        curNodeList = tempNodeList


def splitForUser(ndVal, s):

    n = len(s)
    res1, res2 = np.zeros(n), np.zeros(n)

    for index in range(n):
        if s[index] == 0:
            res2[index] = random.randint(-10, 10)
            res1[index] = ndVal[index] - res2[index]
        else:
            res1[index], res2[index] = ndVal[index], ndVal[index]
    return res1, res2


def encQuery(query, sk):

    s = sk[0]
    m = len(s) - 3

    M1, M2 = sk[1], sk[2]
    M3, M4 = np.linalg.inv(M1), np.linalg.inv(M2)

    trapdoor = {}
    names = ["ext1_q1*", "ext1_q2*", "ext2_q1*", "ext2_q2*", "ext3_q1*", "ext3_q2*", "ext3_Du*"]

    userExt = extendQuery(query, m, sk)

    for index in range(7):

        splitRes = splitForUser(np.array(userExt[index]), s)
        item1, item2 = M3 @ splitRes[0], M4 @ splitRes[1]
        trapdoor[names[index]] = (item1, item2)

    return trapdoor
