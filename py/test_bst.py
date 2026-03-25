from binary_search_tree import binary_search_tree, PRE_ORDER, POST_ORDER


def test_insert():
    bst = binary_search_tree()
    bst.insert_node(1)
    bst.insert_node(2)
    bst.insert_node(3)
    expected = "1->2->3"
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
    expected = "1->2->3"
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
