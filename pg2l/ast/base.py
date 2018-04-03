"""
This is the ast.base module

For example,

>>> x = Node('A1')
>>> y = Node('B')
>>> z = Module()
>>> z.push(x)
>>> z.push(y)
>>> print(repr(z))
(Module A1B)
>>> print([x for x in z])
[(Module A1B), (Node A1), (Node B)]

"""
        
class String(object):
    pass

class Node(String):
    """AST Node class"""
    repr = '(Node %s)'

    def __init__(self, value):
        """
        >>> x = Node('A3')
        >>> x.value
        'A3'
        """
        
        super().__init__()
        self.__value = value
        self.__parent = None
        pass

    @property
    def value(self):
        """Assessor to the value of the node.

        :return: node value's
        :rtype: string
        """
        return self.__value

    @property
    def parent(self):
        """Node parent's, a module or None if node is orphaned"""
        return self.__parent

    def set_parent(self, parent):
        """Set node parent's to parent
        :return: self
        """
        self.__parent = parent
        return self

    def __repr__(self):
        return self.repr % str(self)

    def __str__(self):
        return str(self.value)

    def __iter__(self):
        yield self
    
    pass

class Module(Node):
    """
    A simple k-ary tree, a tree for pg2l expression where branches are modules and leaves are nodes
    """
    repr = '(Module %s)'

    def __init__(self, value=None):
        super().__init__(value)
        self.__children =  []
        pass

    @property
    def children(self): return tuple(self.__children)

    @property
    def value(self): return ''.join(str(x) for x in self.__children)
    
    def push(self, children):
        """Push children into module by adding them to the end of the children's list.

        :param children: Children to add to the module. The parent of each child must be set to None because the new child must be orphaned, otherwhise an exception is raised.

        :type children: A list of children or a single child, child can be either a node or another module, otherwhise an exception is raised.

        :return: None
        :rtype: NoneType
        """

        # if children is not an iterable, turn it into a list
        if not isinstance(children, (list, tuple)):
            children = [children]

        # check if each child if of the right type
        for child in children:
            if not isinstance(child, (Node, Module)):
                raise Exception('try to push a child %s who is neither a node nor a module in a module %s' %
                                    (repr(children), repr(self)))

        # check if each child is orphaned
        for child in children:
            if child.parent is not None:
                raise Exception('child %s must by orphaned, but he already has a parent %s' %
                                    (repr(child), repr(child.parent)))

        # set new chidren's parent
        [child.set_parent(self) for child in children]

        # and add new children at the end of the list
        self.__children += list(children)
        pass
    
    def __iter__(self):
        """
        Deep first pre order traversal of an expression.

        :return: Return an iterator over the leaves of an expression in the order they appear 
                 when we read the expression from left to right.
        :rtype: generator
        """
        
        yield self
        for child in self.children:
            if child:
                yield from child
    
    pass

def copy(x):
    """Return an orphaned copy of x by creating a new instance of x and his children recursively if he has any. If x is an instance of Leaf, the new instance is initialized with x.value.

    :return: orphaned copy of x
    :rtype: list
    """
    x_copy = not isinstance(x, BaseTree) and type(x)(x.value) or type(x)()
    isinstance(x, BaseTree) and [x_copy.push(__shallow_copy(y)) for y in x.children]
    return x_copy

