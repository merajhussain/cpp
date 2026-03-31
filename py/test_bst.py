from binary_search_tree import binary_search_tree, PRE_ORDER, POST_ORDER
from tree_node import TreeNode


def test_insert():
    bst = binary_search_tree()
    bst.insert_node(1)
    bst.insert_node(2)
    bst.insert_node(3)
    expected = "1->2->3->"
    assert expected == bst.to_string()

def test_search():
    bst = binary_search_tree()
    bst.insert_node(1)
    bst.insert_node(2)
    bst.insert_node(3)
    assert True == bst.search(3)

def test_in_order():
    bst = binary_search_tree()
    bst.insert_node(1)
    bst.insert_node(2)
    bst.insert_node(3)
    expected = "1->2->3->"
    assert expected == bst.to_string()

def test_pre_order():
    bst = binary_search_tree()
    bst.insert_node(1)
    bst.insert_node(2)
    bst.insert_node(3)
    expected = "1->2->3"
    assert expected == bst.to_string(PRE_ORDER)

def test_post_order():
    bst = binary_search_tree()
    bst.insert_node(1)
    bst.insert_node(2)
    bst.insert_node(3)
    expected = "3->2->1"
    assert expected == bst.to_string(POST_ORDER)


def test_is_bst_tree():
    bst = binary_search_tree()
    bst.insert_node(2)
    bst.insert_node(1)
    bst.insert_node(3)
    assert True == bst.is_bst_tree()

def test_is_bst_tree_false():
    bst = binary_search_tree()
    bst.root = TreeNode(2)
    bst.root.left = TreeNode(3)
    bst.root.right = TreeNode(1)
    assert False == bst.is_bst_tree()


def test_bst_bfs():
    bst = binary_search_tree()
    bst.insert_node(5)
    bst.insert_node(2)
    bst.insert_node(3)
    bst.insert_node(1)
    bst.insert_node(7)
    bst.insert_node(6)
    bst.insert_node(8)
    expected = "5|27|1368|"

    assert expected == bst.dfs()

def test_bst_height():
    bst = binary_search_tree()
    bst.insert_node(5)
    bst.insert_node(3)
    bst.insert_node(4)
    bst.insert_node(2)
    bst.insert_node(8)
    bst.insert_node(7)
    bst.insert_node(6)
    expected = 3
    #print(bst.dfs())
    assert expected == bst.height()

def test_bst_size():
    bst = binary_search_tree()
    bst.insert_node(5)
    bst.insert_node(3)
    bst.insert_node(4)
    bst.insert_node(2)
    bst.insert_node(8)
    bst.insert_node(7)
    bst.insert_node(6)
    expected = 7
    assert expected == bst.size()

def test_bst_delete_node_no_children():
    bst = binary_search_tree()
    bst.insert_node(50)
    bst.insert_node(40)
    bst.insert_node(45)
    bst.insert_node(30)
    bst.insert_node(70)
    bst.insert_node(60)
    bst.insert_node(80)
    bst.delete_node(30)
    expected = "50|4070|456080|"
    assert expected == bst.dfs()

def test_bst_delete_node_one_child():
    bst = binary_search_tree()
    bst.insert_node(50)
    bst.insert_node(40)
    bst.insert_node(30)
    bst.insert_node(70)
    bst.insert_node(60)
    bst.insert_node(80)
    bst.delete_node(40)
    expected = "50|3070|6080|"
    assert expected == bst.dfs()

def test_bst_delete_root_node():
    bst = binary_search_tree()
    bst.insert_node(50)
    bst.insert_node(40)
    bst.insert_node(30)
    bst.insert_node(45)
    bst.insert_node(70)
    bst.insert_node(60)
    bst.insert_node(80)
    bst.delete_node(50)
    expected = "30|4070|456080|"
    assert expected == bst.dfs()