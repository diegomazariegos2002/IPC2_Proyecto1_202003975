# from graphviz import Source
# temp = """ 
# digraph G{
# Edge [dir=forward]
# node [shape=plaintext]

# 0 [label="0 (None)"]
# 0 -> 5 [label="root"]
# 1 [label="1 (Hello)"]
# 2 [label="2 (how)"]
# 2 -> 1 [label="advmod"]
# 3 [label="3 (are)"]
# 4 [label="4 (you)"]
# 5 [label="5 (doing)"]
# 5 -> 3 [label="aux"]
# 5 -> 2 [label="advmod"]
# 5 -> 4 [label="nsubj"]
# }
# """
# s = Source(temp, filename="test.gv", format="png")
# s.view()

from graphviz import Graph

dot = Graph(comment='The Round Table')

dot.attr('node', shape = "underline")

dot.node('titulo',label='terreno1',)

dot.attr('node', shape = "rectangle")

matriz = [[1,2],[3,4]]

contaFila = 0
contaCol = 0
for i in matriz:
    contaFila += 1
    for j in i:
        contaCol += 1
        dot.node(f'{contaFila}{contaCol}', f'{contaFila},{contaCol}')
    contaCol = 0


dot.edge('11', '21', constraint='true')

print(dot.source)  


# Guarde la fuente en el archivo y proporcione el motor Graphviz
dot.render('test-table.gv', view=True)