import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_url(self):
        node    = TextNode("This is a text node", TextType.BOLD, "ludi")
        node2   = TextNode("This is a text node", TextType.BOLD, None)
        self.assertNotEqual(node,node2)
    
    def test_texttype(self):
        node    = TextNode("This is a text node", TextType.LINK, "ludi")
        node2   = TextNode("This is a text node", TextType.TEXT, "ludi")
        self.assertNotEqual(node,node2)


if __name__ == "__main__":
    unittest.main()