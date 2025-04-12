from textnode import TextNode, TextType

def main():
    my_node = TextNode("palabero", TextType.LINK, "no url")
    print(my_node)
    
main()