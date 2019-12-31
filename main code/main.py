from schemes import *
import random


# def element1(m=80):
#     """
#     for different d:(50, 100), different number of POI objects, obtain traffic and enc time
#     time for poi number
#     :return:
#     """
#     # generating query segment
#     x_lim = [11568.63, 11711.90]
#     y_lim = [3941.38, 4042.60]
#     q1 = Point(round(random.uniform(x_lim[0] - 1, x_lim[1] + 1), 2),
#                round(random.uniform(y_lim[0] - 1, y_lim[1] + 1), 2))
#     q2 = Point(round(random.uniform(x_lim[0] - 1, x_lim[1] + 1), 2),
#                round(random.uniform(y_lim[0] - 1, y_lim[1] + 1), 2))
#     query = Segment(q1, q2)
#     sk = genSK(m)
#     TR = encQuery(query, sk)
#
#     for d in [50, 100]:
#         for index in [4000, 8000, 12000, 16000]:
#             fileName = "data" + str(index) + ".csv"
#             # constructing quadtree
#             root1 = genRoot(fileName)
#             root2 = genRoot(fileName)
#             buildQuadtree(root1, d)
#             buildQuadtree(root2, d)
#
#             # search
#             result_1 = lrs_1(root1, sk, TR)
#             result_2 = lrs_2(root2, sk, TR, d)
#
#             print("when number = " + str(index) + ", communication for lrs_1 is: ", len(result_1))
#             print("when number = " + str(index) + ", communication for lrs_2 is: ", len(result_2))
#
#
# def element2(fileName):
#     """
#     time for m
#     :param fileName:
#     :return:
#     """
#     x_lim = [11568.63, 11711.90]
#     y_lim = [3941.38, 4042.60]
#     q1 = Point(round(random.uniform(x_lim[0] - 1, x_lim[1] + 1), 2),
#                round(random.uniform(y_lim[0] - 1, y_lim[1] + 1), 2))
#     q2 = Point(round(random.uniform(x_lim[0] - 1, x_lim[1] + 1), 2),
#                round(random.uniform(y_lim[0] - 1, y_lim[1] + 1), 2))
#     query = Segment(q1, q2)
#
#     for d in [50, 100]:
#
#         # constructing quadtree
#         root1 = genRoot(fileName)
#         root2 = genRoot(fileName)
#         buildQuadtree(root1, d)
#         buildQuadtree(root2, d)
#
#         for index in [80, 160, 240, 320]:
#
#             sk = genSK(index)
#
#             startForTrapdoor = time.time()
#             TR = encQuery(query, sk)
#             endForTrapdoor = time.time()
#
#             print("When m = " + str(index) + ", time of trapdoor is: ", endForTrapdoor - startForTrapdoor)
#
#             # print("when m = " + str(index) + " :")
#             result_1 = lrs_1(root1, sk, TR)
#             result_2 = lrs_2(root2, sk, TR, d)


def genQuery():

    x_lim = [12100, 12197]
    y_lim = [3100, 3141]
    q1 = Point(round(random.uniform(x_lim[0] - 1, x_lim[1] + 1), 2),
               round(random.uniform(y_lim[0] - 1, y_lim[1] + 1), 2))
    q2 = Point(round(random.uniform(x_lim[0] - 1, x_lim[1] + 1), 2),
               round(random.uniform(y_lim[0] - 1, y_lim[1] + 1), 2))
    return Segment(q1, q2)


def element3(m):
    sk = genSK(m)
    queries = [genQuery() for i in range(10)]
    TRs = [encQuery(query, sk) for query in queries]

    for d in [100, 200]:
        for index in [4000, 8000, 12000, 16000]:
            fileName = "shData" + str(index) + ".csv"

            # constructing quadtree
            root1 = genRoot(fileName)
            root2 = genRoot(fileName)
            buildQuadtree(root1, d)
            buildQuadtree(root2, d)
            lrs_11(root1, sk, TRs)
            lrs_22(root2, sk, TRs, d)


# def element4(fileName):
#
#     queries = [genQuery() for i in range(10)]
#
#     for d in [50, 100]:
#
#         root1 = genRoot(fileName)
#         root2 = genRoot(fileName)
#         buildQuadtree(root1, d)
#         buildQuadtree(root2, d)
#
#         for m in [80, 160, 240, 320]:
#
#             sk = genSK(m)
#             TRs = [encQuery(query, sk) for query in queries]
#             print("m = " + str(m) + ": ")
#
#             lrs_11(root1, sk, TRs)
#             lrs_22(root2, sk, TRs, d)

if __name__ == "__main__":

    element3(80)
