from abc import ABC
from inspect import ismethod, getmro, isfunction
from collections import namedtuple, defaultdict

class G(object):
    w = 'w'
    x = 'x'
    y = 'y'
    z = 'z'

parser_production = namedtuple('parser_production', ['left', 'right'])
parsers = defaultdict(lambda:list())
parsers_cls = {}

def get_class_that_defined(method):
    for cls in getmro(method.__self__.__class__)[1:]:
        if cls.__dict__.get(method.__name__):
            return cls

def register(p):
    print('Register', p.__name__)
    parsers_cls[p.__name__] = p
    return p
        
def docstring_production(*args):
    def __decorate(method):
        print('Deco', method)
        method.__doc__ = method.__doc__.format(*args)
        method_cls_name = method.__qualname__.split('.')[-2]
        parsers[method_cls_name].append(parser_production(args[0], args[1:]))
        return method

    return __decorate

# class docstring_production(object):
#     """A decorator"""
#     def __init__(self, *args, **kwargs):
#         self.args = args
#         self.kwargs = kwargs

#     def __call__(self, method, *args, **kwargs):
#         print('class deco call', method, ismethod(method), isfunction(method))
#         print('dir', dir(method))
#         method_cls_name = method.__qualname__.split('.')[-2]
#         print(parsers)
#         parsers[method_cls_name].append((parser_production(self.args[0], self.args[1:])))
#         method.__doc__ = method.__doc__.format(*self.args, **self.kwargs)
        
#         return method

class AbstractParserMixin(ABC):
    """Mixin"""

class BaseParser(AbstractParserMixin):
    def __init__(self):
        self.data = []

@register
class Mix1(AbstractParserMixin):

    @docstring_production(G.y, G.z)
    def p_y_z(self):
        """{0} : {1}"""
        self.data.append(1)
        print('func_1')

@register
class Mix2(AbstractParserMixin):

    @docstring_production(G.x, G.y)
    def p_x_y(self):
        """{0} : {1}
               | {0} {1}"""
        print('func_base')

    @docstring_production(G.y, G.w)
    def p_y_w(self):
        """{0} : {1}"""
        self.data.append(2)
        print('func_2')

mro = [BaseParser, Mix1, Mix2]

class Parser(*mro):
    def __init__(self):
        print('init')
        for x in mro:
            print(x)
            x.__init__(self)

class A(object):
    def f(self):
        pass

p = Parser()

for name in dir(p):
    if name != '__init__':
        method = getattr(p,name)
        if ismethod(method):
            print('\nfrom %s.%s' % (get_class_that_defined(method), method.__name__))
            print(method.__doc__)

print(p.data)
p.p_y_w()
p.p_y_z()
print(p.data)

print('\nParsers')
for k, v in parsers.items():
    print(k,v)

print(parsers_cls)
