import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(props = {"leck" : "mie", "nasty" : "333"})
        node2 = HTMLNode(props = {"leck" : "mie", "nasty" : "333"})
        self.assertEqual(node, node2)
    
    def test_to_html(self):
        node = ' leck="mie" nasty="333"'
        node2 = HTMLNode(props = {"leck" : "mie", "nasty" : "333"}).props_to_html() 
        self.assertEqual(node, node2)
    
    def test_repr(self):
        node = HTMLNode(props={"style": "color:red"}).props_to_html()
        repr_str = repr(node)
        self.assertIn('style="color:red"', repr_str)
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_props(self):
        node = LeafNode("a", "BuubatzOnBeatz", {"style" : "color:red"})
        self.assertEqual(node.to_html(), '<a style="color:red">BuubatzOnBeatz</a>')
    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    if __name__ == "__main__":
        unittest.main()
        