import pytest


def testCompare():
    assert 1 == 8


if __name__ == '__main__':
    pytest.main(["-s", "-v",
                 "--junit-xml=./framework/test_report/log.xml",
                 "--html=./framework/test_report/result.html",
                 "--self-contained-html",
                 __file__])
