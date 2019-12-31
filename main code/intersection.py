from definations import *
import numpy as np


def transform(nd_val):
    """

    transform function
    :param nd_val: transformed from a 2-dimensional point
    :return: (y, -x)
    """
    return np.array([nd_val[1], -nd_val[0]])


def segmentsIntersect(s1, s2):
    """

    determine whether 2 segments s1, s2 intersect with each other
    :param s1: a segment
    :param s2: a segment
    :return: True or False
    """

    p1 = np.array([s1.p1.x, s1.p1.y])
    p2 = np.array([s1.p2.x, s1.p2.y])
    q1 = np.array([s2.p1.x, s2.p1.y])
    q2 = np.array([s2.p2.x, s2.p2.y])

    my_lambda_1 = np.inner(p1, transform(q2)) - np.inner(p1, transform(q1)) - np.inner(q1, transform(q2))
    my_lambda_2 = np.inner(p2, transform(q2)) - np.inner(p2, transform(q1)) - np.inner(q1, transform(q2))
    my_lambda_3 = np.inner(p1, transform(q1)) - np.inner(p2, transform(q1)) - np.inner(p1, transform(p2))
    my_lambda_4 = np.inner(p1, transform(q2)) - np.inner(p2, transform(q2)) - np.inner(p1, transform(p2))

    if my_lambda_1 * my_lambda_2 < 0 and my_lambda_3 * my_lambda_4 < 0:
        return True
    elif abs(my_lambda_1) < 1e-9:
        return p1 @ p1 + q1 @ q2 - (q1 + q2) @ p1 <= 1e-9
    elif abs(my_lambda_2) < 1e-9:
        return p2 @ p2 + q1 @ q2 - (q1 + q2) @ p2 <= 1e-9
    elif abs(my_lambda_3) < 1e-9:
        return q1 @ q1 + p1 @ p2 - (p1 + p2) @ q1 <= 1e-9
    elif abs(my_lambda_4) < 1e-9:
        return q2 @ q2 + p1 @ p2 - (p1 + p2) @ q2 <= 1e-9
    else:
        return False


def segIntRec(querySeg, rec):
    """
    determine whether the segment seg intersect with the rectangle rec.
    :param querySeg: with two endpoints p1 and p2
    :param rec: with four endpoints p1, p2, p3, p4
    :return: True or False
    """

    s1 = Segment(rec.ul, rec.ll)
    s2 = Segment(rec.ll, rec.lr)
    s3 = Segment(rec.ur, rec.lr)
    s4 = Segment(rec.ul, rec.ur)

    segments = [s1, s2, s3, s4]

    for i in segments:
        if segmentsIntersect(i, querySeg):
            return True

    gamma1 = gammaHelper(segments[0], querySeg)
    gamma2 = gammaHelper(segments[2], querySeg)
    gamma3 = gammaHelper(segments[3], querySeg)
    gamma4 = gammaHelper(segments[1], querySeg)

    return gamma1 * gamma2 < -1e-9 and gamma3 * gamma4 < -1e-9


def gammaHelper(s, querySeg):

    nd_q1 = np.array([querySeg.p1.x, querySeg.p1.y])

    nd_s_p1 = np.array([s.p1.x, s.p1.y])
    nd_s_p2 = np.array([s.p2.x, s.p2.y])

    gamma_i = nd_s_p2 @ transform(nd_q1) - nd_s_p2 @ transform(nd_s_p1) - nd_s_p1 @ transform(nd_q1)

    return gamma_i



