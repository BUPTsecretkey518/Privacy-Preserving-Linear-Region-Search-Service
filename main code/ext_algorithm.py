import hashlib
import random
import copy
import numpy as np
from intersection import transform


def setUp1(iden, m, side, key):

    temp = key + str(iden)

    md5_obj = hashlib.md5(temp.encode())
    sum_val = int(md5_obj.hexdigest(), 16)

    alpha = [random.randint(-10, 10) for i in range(m - 1)]
    alpha.append(int(sum_val/1e36) - sum(alpha))

    sumdj = np.array([side.p1.x, side.p1.y]) @ np.array([side.p2.x, side.p2.y])

    beta = [random.randint(-10, 10) for i in range(m - 1)]
    tail = sumdj - sum(beta)

    beta.append(tail)

    return alpha, beta


def ext1ForTree(side, pos1, pos2, alpha):

    ext1_p1 = copy.deepcopy(alpha)
    ext1_p2 = copy.deepcopy(alpha)

    ext1_p1.insert(pos1, side.p1.x)
    ext1_p1.insert(pos2, side.p1.y)
    ext1_p2.insert(pos1, side.p2.x)
    ext1_p2.insert(pos2, side.p2.y)

    ext1_p1.append(1)
    ext1_p2.append(1)

    return ext1_p1, ext1_p2


def ext2ForTree(side, pos1, pos2, alpha):

    ext2_p1 = copy.deepcopy(alpha)
    ext2_p2 = copy.deepcopy(alpha)

    ext2_p1.insert(pos1, side.p1.x)
    ext2_p1.insert(pos2, side.p1.y)
    ext2_p2.insert(pos1, side.p2.x)
    ext2_p2.insert(pos2, side.p2.y)

    ext2_p1.append(0)
    ext2_p2.append(np.array([side.p1.x, side.p1.y]) @ transform(np.array([side.p2.x, side.p2.y])))

    return ext2_p1, ext2_p2


def ext3ForTree(side, pos1, pos2, beta, m):

    ext3_base = [1 for i in range(m)]

    ext3_p1 = copy.deepcopy(ext3_base)
    ext3_p2 = copy.deepcopy(ext3_base)

    ext3_p1.insert(pos1, -side.p1.x)
    ext3_p1.insert(pos2, -side.p1.y)

    ext3_p2.insert(pos1, -side.p2.x)
    ext3_p2.insert(pos2, -side.p2.y)

    ext3_p1.append(np.array([side.p1.x, side.p1.y]) @ np.array([side.p1.x, side.p1.y]))
    ext3_p2.append(np.array([side.p2.x, side.p2.y]) @ np.array([side.p2.x, side.p2.y]))

    Ds = (side.p1.x + side.p2.x, side.p1.y + side.p2.y)

    beta.insert(pos1, Ds[0])
    beta.insert(pos2, Ds[1])

    ext3_Ds = beta
    ext3_Ds.append(1)

    return ext3_p1, ext3_p2, ext3_Ds


def setUp2(query, m):

    sumkj = np.array([query.p1.x, query.p1.y]) @ np.array([query.p2.x, query.p2.y])

    beta_q = [random.randint(-10, 10) for i in range(m - 1)]
    tail = sumkj - sum(beta_q)

    beta_q.append(tail)

    return beta_q


def ext1ForQuery(query, pos1, pos2, m):

    base1 = [1 for i in range(m + 1)]
    ext1_q1 = copy.deepcopy(base1)
    ext1_q2 = copy.deepcopy(base1)

    ext1_q1.insert(pos1, query.p1.y)
    ext1_q1.insert(pos2, -query.p1.x)

    ext1_q2.insert(pos1, query.p2.y)
    ext1_q2.insert(pos2, -query.p2.x)

    return ext1_q1, ext1_q2


def ext2ForQuery(query, pos1, pos2, m):

    base2 = [1 for i in range(m)]
    ext2_q1 = copy.deepcopy(base2)
    ext2_q2 = copy.deepcopy(base2)

    ext2_q1.insert(pos1, query.p1.y)
    ext2_q1.insert(pos2, -query.p1.x)

    ext2_q1.append(np.array([query.p1.x, query.p1.y]) @ transform(np.array([query.p2.x, query.p2.y])))

    ext2_q2.insert(pos1, query.p2.y)
    ext2_q2.insert(pos2, -query.p2.x)

    ext2_q2.append(0)

    return ext2_q1, ext2_q2


def ext3ForQuery(query, pos1, pos2, beta_q, m):

    base3 = [-1 for i in range(m)]

    ext3_q1 = copy.deepcopy(base3)
    ext3_q2 = copy.deepcopy(base3)

    ext3_q1.insert(pos1, -query.p1.x)
    ext3_q1.insert(pos2, -query.p1.y)
    ext3_q1.append(np.array([query.p1.x, query.p1.y]) @ np.array([query.p1.x, query.p1.y]))

    ext3_q2.insert(pos1, -query.p2.x)
    ext3_q2.insert(pos2, -query.p2.y)
    ext3_q2.append(np.array([query.p2.x, query.p2.y]) @ np.array([query.p2.x, query.p2.y]))

    Du = (query.p1.x + query.p2.x, query.p1.y + query.p2.y)

    ext3_Du = beta_q
    ext3_Du.insert(pos1, query.p1.x)
    ext3_Du.insert(pos2, query.p2.y)
    ext3_Du.append(1)

    return ext3_q1, ext3_q2, ext3_Du


def extendTreeNode(root, m, sk):

    sides = [root.region.s1, root.region.s2, root.region.s3, root.region.s4]

    results = []

    pos1, pos2 = sk[3], sk[4]
    key = "diuwehf283e9nedi2837e"

    for side in sides:

        initVal = setUp1(root.id, m, side, key)
        alpha, beta = initVal[0], initVal[1]

        serverExt1 = ext1ForTree(side, pos1, pos2, alpha)
        ext1_p1, ext1_p2 = serverExt1[0], serverExt1[1]

        serverExt2 = ext2ForTree(side, pos1, pos2, alpha)
        ext2_p1, ext2_p2 = serverExt2[0], serverExt2[1]

        serverExt3 = ext3ForTree(side, pos1, pos2, beta, m)
        ext3_p1, ext3_p2, ext3_Ds = serverExt3[0], serverExt3[1], serverExt3[2]

        results.append((ext1_p1, ext1_p2, ext2_p1, ext2_p2, ext3_p1, ext3_p2, ext3_Ds))

    return results


def extendQuery(query, m, sk):

    pos1, pos2 = sk[3], sk[4]

    beta_q = setUp2(query, m)

    uesrExt1 = ext1ForQuery(query, pos1, pos2, m)
    ext1_q1, ext1_q2 = uesrExt1[0], uesrExt1[1]

    uesrExt2 = ext2ForQuery(query, pos1, pos2, m)
    ext2_q1, ext2_q2 = uesrExt2[0], uesrExt2[1]

    uesrExt2 = ext3ForQuery(query, pos1, pos2, beta_q, m)
    ext3_q1, ext3_q2, ext3_Du = uesrExt2[0], uesrExt2[1], uesrExt2[2]

    return ext1_q1, ext1_q2, ext2_q1, ext2_q2, ext3_q1, ext3_q2, ext3_Du




























