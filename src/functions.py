from textnode import TextType, TextNode
from htmlnode import LeafNode
import re

def text_node_to_html_node(text_node):

    if text_node.text_type == TextType.TEXT:
        return LeafNode(tag = None,value=text_node.text)
    if text_node.text_type == TextType.BOLD:
        return LeafNode("b",value=text_node.text)
    if text_node.text_type == TextType.ITALIC:
        return LeafNode("i",value=text_node.text)
    if text_node.text_type == TextType.CODE:
        return LeafNode("code", value=text_node.text)
    if text_node.text_type == TextType.LINK:
        return LeafNode("a",value=text_node.text, props= {"href" : text_node.url})
    if text_node.text_type == TextType.IMAGE:
        return LeafNode("img", value="", props = {"src" : text_node.url, "alt" : text_node.text})
    
    raise Exception("No proper TextType")

def split_nodes_delimeter(old_nodes, delimeter, text_type):
    
    
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimeter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes
            
def extract_markdown_images(text):
    image_text =  re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)",text)
    return image_text

def extract_markdown_links(text):
    link_text  =  re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    
    return (link_text)
            
        
    
