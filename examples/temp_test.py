__author__ = 'machiry'

import sys
from pycparser import c_parser, c_ast, parse_file


# A simple visitor for FuncDef nodes that prints the names and
# locations of function definitions.
class FuncDefVisitor(c_ast.NodeVisitor):
    def visit_FuncDef(self, node):
        print('%s at %s' % (node.decl.name, node.decl.coord))

    def visit_FileAST(self, node):
        print 'Visited File'


def show_func_defs(filename):
    # Note that cpp is used. Provide a path to your own cpp or
    # make sure one exists in PATH.
    ast = parse_file(filename, use_cpp=True)

    v = FuncDefVisitor()
    v.visit(ast)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename  = sys.argv[1]
    else:
        filename = '/home/machiry/projects/pycparser/examples/c_files/temp_test.c'

    show_func_defs(filename)
