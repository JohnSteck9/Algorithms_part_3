import unittest
from ijones import *

FILE_IN_1 = 'data/ijones1.in'
FILE_IN_2 = 'data/ijones2.in'
FILE_IN_3 = 'data/ijones3.in'


graph1 = {'a1': {'a3', 'a5', 'a2'}, 'c4': {'a5'}, 'd7': {'e8'}, 'a2': {'a3'}, 'a5': {'a3', 'b6'}, 'e8': {'f9'}, 'a3': {}, 'b6': {}, 'f9': {}}
graph2 = {'a1': {'a7', 'b2'}, 'b2': {'c3'}, 'c3': {'d4'}, 'd4': {'e5'}, 'e5': {'f6'}, 'f6': {'a7'}, 'a7': {'g8'}, 'g8': {'h9'}, 'h9': {'i10'}, 'i10': {}}
graph3 = {'a1': {'a5', 'a20', 'a19', 'a2', 'a7', 'a12', 'a26', 'a23', 'a33', 'a3', 'a31', 'a42', 'a6', 'a21', 'a35', 'a13', 'a41', 'a17', 'a25', 'a38', 'a32', 'a11', 'a27', 'a14', 'a16', 'a30', 'a4', 'a10', 'a34', 'a28', 'a9', 'a24', 'a37', 'a39', 'a18', 'a40'}, 'a8': {'a5', 'a20', 'a19', 'a2', 'a7', 'a12', 'a26', 'a23', 'a33', 'a3', 'a31', 'a42', 'a6', 'a21', 'a35', 'a13', 'a41', 'a17', 'a25', 'a38', 'a32', 'a11', 'a27', 'a14', 'a16', 'a30', 'a4', 'a10', 'a34', 'a28', 'a9', 'a24', 'a37', 'a39', 'a18', 'a40'}, 'a15': {'a5', 'a20', 'a19', 'a2', 'a7', 'a12', 'a26', 'a23', 'a33', 'a3', 'a31', 'a42', 'a6', 'a21', 'a35', 'a13', 'a41', 'a17', 'a25', 'a38', 'a32', 'a11', 'a27', 'a14', 'a16', 'a30', 'a4', 'a10', 'a34', 'a28', 'a9', 'a24', 'a37', 'a39', 'a18', 'a40'}, 'a22': {'a5', 'a20', 'a19', 'a2', 'a7', 'a12', 'a26', 'a23', 'a33', 'a3', 'a31', 'a42', 'a6', 'a21', 'a35', 'a13', 'a41', 'a17', 'a25', 'a38', 'a32', 'a11', 'a27', 'a14', 'a16', 'a30', 'a4', 'a10', 'a34', 'a28', 'a9', 'a24', 'a37', 'a39', 'a18', 'a40'}, 'a29': {'a5', 'a20', 'a19', 'a2', 'a7', 'a12', 'a26', 'a23', 'a33', 'a3', 'a31', 'a42', 'a6', 'a21', 'a35', 'a13', 'a41', 'a17', 'a25', 'a38', 'a32', 'a11', 'a27', 'a14', 'a30', 'a16', 'a4', 'a10', 'a34', 'a28', 'a9', 'a24', 'a37', 'a39', 'a18', 'a40'}, 'a36': {'a5', 'a20', 'a19', 'a2', 'a7', 'a12', 'a26', 'a23', 'a33', 'a3', 'a31', 'a42', 'a6', 'a21', 'a35', 'a13', 'a41', 'a17', 'a25', 'a38', 'a32', 'a11', 'a27', 'a14', 'a16', 'a30', 'a4', 'a10', 'a34', 'a28', 'a9', 'a24', 'a37', 'a39', 'a18', 'a40'}, 'a2': {'a5', 'a20', 'a19', 'a7', 'a12', 'a26', 'a33', 'a3', 'a31', 'a42', 'a6', 'a21', 'a35', 'a13', 'a41', 'a17', 'a25', 'a38', 'a32', 'a11', 'a27', 'a14', 'a4', 'a10', 'a34', 'a28', 'a24', 'a39', 'a18', 'a40'}, 'a9': {'a5', 'a20', 'a19', 'a7', 'a12', 'a26', 'a33', 'a3', 'a31', 'a42', 'a6', 'a21', 'a35', 'a13', 'a41', 'a17', 'a25', 'a38', 'a32', 'a11', 'a27', 'a14', 'a4', 'a10', 'a34', 'a28', 'a24', 'a39', 'a18', 'a40'}, 'a16': {'a5', 'a20', 'a19', 'a7', 'a12', 'a26', 'a33', 'a3', 'a31', 'a42', 'a6', 'a21', 'a35', 'a13', 'a41', 'a17', 'a25', 'a38', 'a32', 'a11', 'a27', 'a14', 'a4', 'a10', 'a34', 'a28', 'a24', 'a39', 'a18', 'a40'}, 'a23': {'a5', 'a20', 'a19', 'a7', 'a12', 'a26', 'a33', 'a3', 'a31', 'a42', 'a6', 'a21', 'a35', 'a13', 'a41', 'a17', 'a25', 'a38', 'a32', 'a11', 'a27', 'a14', 'a4', 'a10', 'a34', 'a28', 'a24', 'a39', 'a18', 'a40'}, 'a30': {'a5', 'a20', 'a19', 'a7', 'a12', 'a26', 'a33', 'a3', 'a31', 'a42', 'a6', 'a21', 'a35', 'a13', 'a41', 'a17', 'a25', 'a38', 'a32', 'a11', 'a27', 'a14', 'a4', 'a10', 'a34', 'a28', 'a24', 'a39', 'a18', 'a40'}, 'a37': {'a5', 'a20', 'a19', 'a7', 'a12', 'a26', 'a33', 'a3', 'a31', 'a42', 'a6', 'a21', 'a35', 'a13', 'a41', 'a17', 'a25', 'a38', 'a32', 'a11', 'a27', 'a14', 'a4', 'a10', 'a34', 'a28', 'a24', 'a39', 'a18', 'a40'}, 'a3': {'a5', 'a20', 'a19', 'a7', 'a12', 'a26', 'a33', 'a42', 'a6', 'a21', 'a35', 'a13', 'a41', 'a25', 'a32', 'a11', 'a27', 'a14', 'a4', 'a34', 'a28', 'a39', 'a18', 'a40'}, 'a10': {'a5', 'a20', 'a19', 'a7', 'a12', 'a26', 'a33', 'a42', 'a6', 'a21', 'a35', 'a13', 'a41', 'a25', 'a32', 'a11', 'a27', 'a14', 'a4', 'a34', 'a28', 'a39', 'a18', 'a40'}, 'a17': {'a5', 'a20', 'a19', 'a7', 'a12', 'a26', 'a33', 'a42', 'a6', 'a21', 'a35', 'a13', 'a41', 'a25', 'a32', 'a11', 'a27', 'a14', 'a4', 'a34', 'a28', 'a39', 'a18', 'a40'}, 'a24': {'a5', 'a20', 'a19', 'a7', 'a12', 'a26', 'a33', 'a42', 'a6', 'a21', 'a35', 'a13', 'a41', 'a25', 'a32', 'a11', 'a27', 'a14', 'a4', 'a34', 'a28', 'a39', 'a18', 'a40'}, 'a31': {'a5', 'a20', 'a19', 'a7', 'a12', 'a26', 'a33', 'a42', 'a6', 'a21', 'a35', 'a13', 'a41', 'a25', 'a32', 'a11', 'a27', 'a14', 'a4', 'a34', 'a28', 'a39', 'a18', 'a40'}, 'a38': {'a5', 'a20', 'a19', 'a7', 'a12', 'a26', 'a33', 'a42', 'a6', 'a21', 'a35', 'a13', 'a41', 'a25', 'a32', 'a11', 'a27', 'a14', 'a4', 'a34', 'a28', 'a39', 'a18', 'a40'}, 'a4': {'a27', 'a14', 'a5', 'a20', 'a19', 'a42', 'a6', 'a21', 'a7', 'a35', 'a12', 'a13', 'a34', 'a26', 'a41', 'a28', 'a40', 'a33'}, 'a11': {'a27', 'a14', 'a5', 'a20', 'a19', 'a42', 'a6', 'a21', 'a7', 'a35', 'a12', 'a13', 'a34', 'a26', 'a41', 'a28', 'a40', 'a33'}, 'a18': {'a27', 'a14', 'a5', 'a20', 'a19', 'a42', 'a6', 'a21', 'a7', 'a35', 'a12', 'a13', 'a34', 'a26', 'a41', 'a28', 'a40', 'a33'}, 'a25': {'a27', 'a14', 'a5', 'a20', 'a19', 'a42', 'a6', 'a21', 'a7', 'a35', 'a12', 'a13', 'a34', 'a26', 'a41', 'a28', 'a40', 'a33'}, 'a32': {'a27', 'a14', 'a5', 'a20', 'a19', 'a42', 'a6', 'a21', 'a7', 'a35', 'a12', 'a13', 'a34', 'a26', 'a41', 'a28', 'a40', 'a33'}, 'a39': {'a27', 'a14', 'a5', 'a20', 'a19', 'a42', 'a6', 'a21', 'a7', 'a35', 'a12', 'a13', 'a34', 'a26', 'a41', 'a28', 'a40', 'a33'}, 'a5': {'a27', 'a14', 'a20', 'a42', 'a6', 'a21', 'a7', 'a35', 'a13', 'a34', 'a41', 'a28'}, 'a12': {'a27', 'a14', 'a20', 'a42', 'a6', 'a21', 'a7', 'a35', 'a13', 'a34', 'a41', 'a28'}, 'a19': {'a27', 'a14', 'a20', 'a42', 'a6', 'a21', 'a7', 'a35', 'a13', 'a34', 'a41', 'a28'}, 'a26': {'a27', 'a14', 'a20', 'a42', 'a6', 'a21', 'a7', 'a35', 'a13', 'a34', 'a41', 'a28'}, 'a33': {'a27', 'a14', 'a20', 'a42', 'a6', 'a21', 'a7', 'a35', 'a13', 'a34', 'a41', 'a28'}, 'a40': {'a27', 'a14', 'a20', 'a42', 'a6', 'a21', 'a7', 'a35', 'a13', 'a34', 'a41', 'a28'}, 'a6': {'a14', 'a42', 'a21', 'a7', 'a35', 'a28'}, 'a13': {'a14', 'a42', 'a21', 'a7', 'a35', 'a28'}, 'a20': {'a14', 'a42', 'a21', 'a7', 'a35', 'a28'}, 'a27': {'a14', 'a42', 'a21', 'a7', 'a35', 'a28'}, 'a34': {'a14', 'a42', 'a21', 'a7', 'a35', 'a28'}, 'a41': {'a14', 'a42', 'a21', 'a7', 'a35', 'a28'}, 'a7': {}, 'a14': {}, 'a21': {}, 'a28': {}, 'a35': {}, 'a42': {}}


class TestCareer(unittest.TestCase):
    def test_find_max_experience1(self):
        self.assertEqual(main(FILE_IN_1), 5)
        self.assertEqual(main(FILE_IN_2), 2)
        self.assertEqual(main(FILE_IN_3), 201684)


if __name__ == "__main__":
    unittest.main()
