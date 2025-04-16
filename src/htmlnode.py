
class HTMLNode():
    
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag 
        self.value = value
        self.children = children
        self.props = props
        
    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        out_string = ''
        if self.props is not None:
            for key in self.props.keys():
                out_string += f' {key}="{self.props[key]}"' 
        return out_string
    
    def __eq__(self, other):
        if not isinstance(other,HTMLNode):
            return False
        return (self.tag == other.tag and 
                self.value == other.value and
                self.children == other.children and
                self.props == other.props)
    
    def __repr__(self):
        return f"HTMLNode(tag='{self.tag}', value='{self.value}', props={self.props})"
    
class LeafNode(HTMLNode):
    
    def __init__(self, tag, value, props = None):
        
        super().__init__(tag,value, props = props)
        
    def to_html(self):
        
        if self.value is None:
            raise ValueError("All LeafNodes must have a value")
        
        if self.tag is None:
            return f"{self.value}"
        
        return  f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    
    def __init__(self, tag, children, props = None):
        
        super().__init__(tag,  children = children , props = props, value = None,)
        
    def to_html(self):
        if self.tag is None:
            raise ValueError("All ParentNodes must have a tag")
        if self.children is None:
            raise ValueError("All ParentNodes must have children")
        props_str = "" if self.props is None else self.props_to_html
        children_str = ""
        for child in self.children:
            children_str += child.to_html()
        return f"<{self.tag}{props_str}>{children_str}</{self.tag}>"
        
        
        
        
        
                 