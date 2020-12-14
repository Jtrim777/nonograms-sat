from reduction import reduce_board
from solve import *

rowSet1 = [[2], [2], [2, 1], [4], [2]]
colSet1 = [[3], [4], [1], [2], [3]]
sol1 = [1, 2, -3, -4, -5,
        6, 7, -8, -9, -10,
        11, 12, -13, -14, 15,
        -16, 17, 18, 19, 20,
        -21, -22, -23, 24, 25]

rowSet2 = [[4], [4], [2, 1], [1, 1], [2, 2], [1, 4], [3, 4], [8], [6, 1], [3, 3]]
colSet2 = [[5], [1, 1, 1], [3], [2, 3], [2, 3], [3, 4], [2, 4], [5], [4, 1], [3, 3]]
sol2 = [-1, -2, -3, 4, 5, 6, 7, -8, -9, -10,
        -11, -12, -13, 14, 15, 16, 17, -18, -19, -20,
        21, 22, -23, -24, -25, 26, -27, -28, -29, -30,
        31, -32, -33, -34, -35, -36, -37, -38, -39, 40,
        41, 42, -43, -44, -45, -46, -47, -48, 49, 50,
        51, -52, -53, -54, -55, -56, 57, 58, 59, 60,
        61, 62, 63, -64, -65, 66, 67, 68, 69, -70,
        -71, -72, 73, 74, 75, 76, 77, 78, 79, 80,
        -81, -82, 83, 84, 85, 86, 87, 88, -89, 90,
        -91, -92, -93, 94, 95, 96, -97, 98, 99, 100]

rowSet3 = [[8, 1], [8, 2], [1, 1, 5, 3], [1, 4, 3], [10],
           [1, 8], [3, 9], [3, 1, 1, 2], [7], [6],
           [5], [2, 2, 2], [1, 2], [5, 2], [2, 2]]
colSet3 = [[1, 1, 1], [1, 1], [4, 4, 1], [2, 4, 2], [3, 5, 2],
           [5, 4], [5, 7], [7, 3], [11], [2, 3],
           [3], [3], [5], [8, 4], [7, 4]]

sol3 = [-1, -2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, 14, -15,
        -16, -17, 18, 19, 20, 21, 22, 23, 24, 25, -26, -27, -28, 29, 30,
        31, -32, 33, -34, 35, 36, 37, 38, 39, -40, -41, -42, 43, 44, 45,
        -46, -47, 48, -49, -50, 51, 52, 53, 54, -55, -56, -57, 58, 59, 60,
        -61, -62, -63, -64, -65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75,
        -76, -77, 78, -79, -80, -81, -82, 83, 84, 85, 86, 87, 88, 89, 90,
        -91, -92, 93, 94, 95, -96, 97, 98, 99, 100, 101, 102, 103, 104, 105,
        -106, -107, 108, 109, 110, -111, 112, -113, 114, -115, -116, -117, -118, 119, 120,
        -121, -122, 123, 124, 125, 126, 127, 128, 129, -130, -131, -132, -133, -134, -135,
        -136, -137, -138, 139, 140, 141, 142, 143, 144, -145, -146, -147, -148, -149, -150,
        -151, -152, -153, -154, 155, 156, 157, 158, 159, -160, -161, -162, -163, -164, -165,
        166, 167, -168, -169, -170, 171, 172, -173, -174, -175, -176, -177, -178, 179, 180,
        -181, -182, -183, -184, -185, -186, 187, -188, -189, -190, -191, -192, -193, 194, 195,
        196, 197, 198, 199, 200, -201, -202, -203, -204, -205, -206, -207, -208, 209, 210,
        -211, -212, -213, 214, 215, -216, -217, -218, -219, -220, -221, -222, -223, 224, 225]


def test(size, rows, cols, expectedSol):
    form = reduce_board(size, rows, cols)
    testSol = solve(form)
    passed = True
    for i in range(size * size):
        if testSol[1][i] != expectedSol[i]:
            passed = False
    print(passed)


badRowSet1 = [[3, 1], [1, 1], [3, 6], [3], [2, 1, 4], [6], [7], [5], [5], [2, 1]]
badColSet1 = [[1, 1], [1, 1, 1], [3], [1, 3], [1, 2, 1], [7], [7], [7], [3, 5], [1, 3]]

def assert_bad(size, rows, cols):
    form = reduce_board(size, rows, cols)
    testSol = solve(form)
    print(not testSol[1])


def test_all():
    test(5, rowSet1, colSet1, sol1)
    test(10, rowSet2, colSet2, sol2)
    test(15, rowSet3, colSet3, sol3)
    assert_bad(10, badRowSet1, badColSet1)


