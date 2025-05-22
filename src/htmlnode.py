import functools

class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if self.props is not None:
            props = self.props.items()
            html = "".join(list(map(lambda x : f" {x[0]}=\"{x[1]}\"", props)))
            return html
        pass
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
    def __eq__(self, other):
        if (
                self.tag == other.tag and
                self.value == other.value and
                self.children == other.children and
                self.props == other.props
            ):
            return True
        return False
    
class LeafNode(HTMLNode):
    def __init__(self, tag = None, value = None, props = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value")
        output = f"<{self.tag}"
        if self.tag is not None:
            if self.props is not None:
                output += self.props_to_html()
            output += f">{self.value}</{self.tag}>"
        return output

    def __eq__(self, other):
        if (
                self.tag == other.tag and
                self.value == other.value and
                self.props == other.props
            ):
            return True
        return False

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    
    def __str__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag = None, children = None, props = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")
        if self.children is None:
            raise ValueError("ParentNode must have children")
        output = f"<{self.tag}{self.props_to_html()}"
        if self.props is not None:
            output += self.props_to_html()
        output += ">"
        output += "".join(list(map(lambda x: x.to_html(), self.children)))
        output += f"</{self.tag}>"
        return output

    def __eq__(self, other):
        if (
                self.tag == other.tag and
                self.value == other.children and
                self.props == other.props
            ):
            return True
        return False

    def __repr__(self):
        return f"ParentNode({self.tag}, {self.value}, {self.props})"
    
    def __str__(self):
        return f"ParentNode({self.tag}, {self.value}, {self.props})"