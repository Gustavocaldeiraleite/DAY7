from DAY7 import sorted_array

def test1():
    assert sorted_array([1,3,4,5,0,], [2,1,3,6,9,9,0,]) == [1, 1, 2, 3, 3, 4, 5, 6, 9, 9]
    
def test2():
    assert sorted_array([1,2,3,0,0,0], [2,5,6]) == [1,2,2,3,5,6]


if __name__ == '__main__':
    test1()
    test2()
    print('all tests passed')

