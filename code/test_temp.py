import nose
import temp
'''cwtest_nose hello wrold....'''
def test_to_celsius():
    '''test celsius....'''
    assert temp.to_celsius(31) < 0,'负'
    assert temp.to_celsius(32) == 0,'边缘'
    assert temp.to_celsius(33) > 0,'正'
    assert temp.to_celsius(-33) < 0,'负'
    assert temp.to_celsius(0) < 0,'边缘'
    assert temp.to_celsius(1) < 0,'正'
def test_above_freezing():
    '''test freeze....'''
    pass #good

if __name__ == '__main__':
    nose.runmodule()