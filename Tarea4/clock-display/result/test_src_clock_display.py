# Test cases automatically generated by Pynguin (https://github.com/se2p/pynguin).
# Please check them before you use them.
import pytest
import src.clock_display as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xe9\x18"
    clock_display_0 = module_0.ClockDisplay(bytes_0)
    var_0 = clock_display_0.invariant()
    var_1 = clock_display_0.str()
    assert var_1 == "00:00"
    var_2 = clock_display_0.increment()
    var_2.invariant()


def test_case_1():
    bytes_0 = b"\xe9\xdf~\x18"
    clock_display_0 = module_0.ClockDisplay(bytes_0)
    var_0 = clock_display_0.increment()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\x8cZ\xdd\x14\x9b\x92\x0e\xac\x14<z\xe1\x18T\xe6u\xd2"
    clock_display_0 = module_0.ClockDisplay(bytes_0)
    var_0 = clock_display_0.clone()
    module_0.ClockDisplay(clock_display_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    dict_0 = {}
    clock_display_0 = module_0.ClockDisplay(dict_0)
    var_0 = clock_display_0.increment()
    var_0.increment()


def test_case_4():
    bool_0 = True
    list_0 = [bool_0, bool_0]
    clock_display_0 = module_0.ClockDisplay(list_0)
    var_0 = clock_display_0.increment()


@pytest.mark.xfail(strict=True)
def test_case_5():
    bytes_0 = b"\xd5\x8a\x99\xb4\x83\x94B\xcdP\x01"
    clock_display_0 = module_0.ClockDisplay(bytes_0)
    var_0 = clock_display_0.clone()
    var_1 = var_0.increment()
    var_2 = var_0.str()
    assert var_2 == "00:00:00:00:00:00:00:00:01:00"
    var_2.str()