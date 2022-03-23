"""
Modifique a gramática abaixo e/ou a classe de transformer para que as árvores
sintáticas dos exemplos abaixo obedeçam à estrutura desejada.

Você pode criar novas regras, reescrever as regras apresentadas, incluir operadores 
como ?, _, etc. 
"""
from lark import Lark, Transformer, Tree, v_args


grammar = Lark(
    r"""
start  : cmd+

cmd    : expr ";"
       | NAME "=" expr ";"
       | "if" expr "{" cmd+ "}" "else" "{" cmd+ "}" -> ifelse

expr   : NAME
       | NAME "(" [ args ] ")"

args   : expr [ "," args ]

NAME   : /(?!\d)\w+/

%ignore /\s+/
"""
)


@v_args(inline=True)
class IR(Transformer):
    NAME = str
    var = str

    def funcall(self, fn, args):
        return [fn, *args]

    def args(self, *args):
        return [...]

    def assign(self, lhs, rhs):
        return ["def", lhs, rhs]

    def cond(self, cond, then, other):
        return ["if", cond, then, other]

    def __default__(self, data, children, meta):
        print(f"nó não processado: {data}")
        return super().__default__(data, children, meta)


def parse(src: str) -> Tree:
    ast = grammar.parse(src)
    return IR().transform(ast)
