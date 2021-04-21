import sys
sys.path.append("../..")
from doubly_linked_list import DoublyLinkedList as DLL


def test_node_str():
    test_node = DLL.Node(1)
    assert str(test_node) == "1"
    test_node = DLL.Node("test")
    assert str(test_node) == "test"


def test_node_equals():
    test_node = DLL.Node(1)
    assert test_node == 1
    test_node = DLL.Node("test")
    assert test_node == "test"


def test_node_update():
    test_node = DLL.Node(1)
    test_node.update("test")
    assert test_node.data == "test"


def test_dll_add():
    test_dll = DLL()
    test_dll.add(1)
    assert test_dll.head.data == 1
    assert test_dll.tail.data == 1
    test_dll.add(2)
    assert test_dll.head.data == 1
    assert test_dll.tail.data == 2


def test_dll_add_head():
    test_dll = DLL()
    test_dll.add_head(1)
    assert test_dll.head.data == 1
    assert test_dll.tail.data == 1
    test_dll.add_head(2)
    assert test_dll.head.data == 2
    assert test_dll.tail.data == 1
    test_dll.add_head(3)
    assert test_dll.head.data == 3
    assert test_dll.tail.data == 1


def test_ddl_add_tail():
    test_dll = DLL()
    test_dll.add_tail(1)
    assert test_dll.head.data == 1
    assert test_dll.tail.data == 1
    test_dll.add_tail(2)
    assert test_dll.head.data == 1
    assert test_dll.tail.data == 2
    test_dll.add_tail("test")
    assert test_dll.head.data == 1
    assert test_dll.tail.data == "test"


def test_dll_string():
    test_dll = DLL()
    test_dll.add_tail(1)
    test_dll.add_tail(2)
    test_dll.add_tail("test")
    test_string = "[1, 2, test]"
    assert str(test_dll) == test_string


def test_remove_data():
    test_dll = DLL()
    test_dll.add_tail(1)
    test_dll.add_tail(2)
    test_dll.add_tail("test")
    test_dll.remove_data(2)
    assert test_dll.head == 1
    assert test_dll.tail == "test"
    test_dll.remove_data(1)
    assert test_dll.head == "test"
    assert test_dll.tail == "test"
    test_dll.remove_data("test")
    assert test_dll.head is None
    assert test_dll.tail is None


def test_remove_position():
    test_dll = DLL()
    test_dll.add_tail(1)
    test_dll.add_tail(2)
    test_dll.add_tail("test")
    test_dll.remove_position(1)
    assert test_dll.head == 1
    assert test_dll.tail == "test"
    test_dll.remove_position(0)
    assert test_dll.head == "test"
    assert test_dll.tail == "test"
    test_dll.remove_position(0)
    assert test_dll.head is None
    assert test_dll.tail is None


def test_query_position():
    test_dll = DLL()
    test_dll.add_tail(1)
    test_dll.add_tail(2)
    test_dll.add_tail("test")
    assert test_dll.query_position(0) == 1
    assert test_dll.query_position(1) == 2
    assert test_dll.query_position(2) == "test"


def test_find_data():
    test_dll = DLL()
    test_dll.add_tail(1)
    test_dll.add_tail(2)
    test_dll.add_tail("test")
    assert test_dll.query_position(0) == 1
    assert test_dll.query_position(1) == 2
    assert test_dll.query_position(2) == "test"
    assert test_dll.query_position(3) is None


def test_update_position():
    test_dll = DLL()
    test_dll.add_tail(1)
    test_dll.add_tail(2)
    test_dll.add_tail("test")
    test_dll.update_position(0, 3)
    test_dll.update_position(1, 2)
    test_dll.update_position(2, 1)
    assert test_dll.query_position(0) == 3
    assert test_dll.query_position(1) == 2
    assert test_dll.query_position(2) == 1
    assert test_dll.update_position(3, 1) == -1


def test_len():
    test_dll = DLL()
    len_now = test_dll.len()
    assert len_now == 0
    test_dll.add_tail(1)
    len_now = test_dll.len()
    assert len_now == 1
    test_dll.add_tail(2)
    len_now = test_dll.len()
    assert len_now == 2
    test_dll.add_tail("test")
    len_now = test_dll.len()
    assert len_now == 3

