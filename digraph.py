import graphviz # graphviz-0.20.1
from graphviz import Digraph
from functions import autolinebreak

# dictionary of nodes:
n_dict = {

    'type 1 node': [    
                    'A A A', # 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.', # 0
                    'B B B', # 'Non diam phasellus vestibulum lorem sed.', # 1
                    'C C C', # 'Faucibus scelerisque eleifend donec pretium.', # 2
                    ],
    
    'type 2 node': [    
                    'X X X', # 'Lobortis elementum nibh tellus molestie nunc non blandit massa.', # 0
                    'Y Y Y', # 'Nec sagittis aliquam malesuada bibendum.', # 1
                    'Z Z Z', # 'Posuere morbi leo urna molestie at.', # 2
                    ],

    'type 3 node': [    
                    'Q Q Q', # 'Aliquet eget sit amet tellus cras.', # 0
                    ],

    'type 4 node': [    
                    'Enim sit amet venenatis urna cursus eget nunc.', # 0
                    'Viverra aliquet eget sit amet tellus cras adipiscing.', # 1
                    '', # 'Lacus sed viverra tellus in.', # 2
                    'Ornare lectus sit amet est placerat in egestas erat imperdiet.', # 3
                    'Condimentum id venenatis a condimentum vitae.', # 4
                    'Scelerisque eleifend donec pretium vulputate sapien nec sagittis.', # 5
                    'Ac felis donec et odio pellentesque diam volutpat commodo sed.', # 6
                    'Dui accumsan sit amet nulla facilisi morbi tempus iaculis.', # 7
                    'Pellentesque elit ullamcorper dignissim cras tincidunt lobortis feugiat.', # 8
                    'In eu mi bibendum neque egestas.', # 9
                    ],

    'type 5 node': [    
                    'Erat pellentesque adipiscing commodo elit.', # 0
                    'Posuere urna nec tincidunt praesent semper feugiat nibh.', # 1
                    'Porta lorem mollis aliquam ut porttitor.', # 2
                    'Eget duis at tellus at urna condimentum mattis pellentesque.', # 3
                    '', # 'Leo urna molestie at elementum.', # 4
                    'Adipiscing diam donec adipiscing tristique risus nec feugiat.', # 5
                    'Pretium vulputate sapien nec sagittis aliquam malesuada bibendum arcu.', # 6
                    ],

}

# applying until_x() to the dictionary:
max_char = 22
outer_list = []
for a in range(len(n_dict.keys())):
    inner_list = []
    for b in range(len([[i for i in n_dict[k]] for k in n_dict.keys()][a])):
        inner_list.append(autolinebreak([[i for i in n_dict[k]] for k in n_dict.keys()][a][b], max_char))
    outer_list.append(inner_list)

for (i, j) in zip(n_dict.keys(), range(len(n_dict.keys()))):
    n_dict[i] = outer_list[j]

# graph type:
digraph = Digraph('G', filename='digraph.gv')

# nodes that are no longer needed are made invisible: 
digraph.attr('node', shape='plaintext')
digraph.node(n_dict['type 4 node'][2])
digraph.node(n_dict['type 5 node'][4])

# type 1 node style:
digraph.attr('node', shape='doublecircle', style='filled', color='green4', fontcolor='gold')
for x in n_dict['type 1 node']:
  digraph.node(x)

# type 2 node style:
digraph.attr('node', shape='doublecircle', style='filled', color='red3', fontcolor='gold')
for x in n_dict['type 2 node']:
  digraph.node(x)

# type 3 node style:
digraph.attr('node', shape='doublecircle', style='filled', color='gold', fontcolor='black')
for x in n_dict['type 3 node']:
  digraph.node(x)

# type 4 node style:
digraph.attr('node', shape='box', style='filled', color='lightblue2', fontcolor='black')
for x in n_dict['type 4 node']:
  digraph.node(x)

# type 5 node style:
digraph.attr('node', shape='box', style='filled', color='gray', fontcolor='black')
for x in n_dict['type 5 node']:
  digraph.node(x)

# single-to-single edge:
digraph.edge(n_dict['type 1 node'][0], n_dict['type 1 node'][1])

# single-to-single-node edge:
digraph.edge(n_dict['type 1 node'][2], n_dict['type 1 node'][1])

# single-to-multiple-node edges:
l = [
    n_dict['type 2 node'][0],
    n_dict['type 2 node'][2]
    ]
for x in l:
    digraph.edge(n_dict['type 2 node'][1], x)

# multiple-to-single-node edges:
l = [
    n_dict['type 2 node'][0],
    # n_dict['type 2 node'][1],
    n_dict['type 2 node'][2]
    ]
for x in l:
    digraph.edge(x, n_dict['type 3 node'][0])

# multiple-to-multiple-node edges:
l = [
    n_dict['type 4 node'][0],
    n_dict['type 4 node'][1],
    n_dict['type 4 node'][3]]
for x in l:
    digraph.edges([(x, n_dict['type 4 node'][5]), (x, n_dict['type 4 node'][6])])
    digraph.edge(n_dict['type 1 node'][1], x)

# multiple-to-single-node edges:
l = [
    n_dict['type 4 node'][5],
    n_dict['type 4 node'][6]
    ]
for x in l:
    digraph.edge(x, n_dict['type 2 node'][1])

# single-to-single-node edge:
digraph.edge(n_dict['type 5 node'][0], n_dict['type 4 node'][7])

# multiple-to-multiple-node edges:
l = [
    n_dict['type 4 node'][7],
    n_dict['type 4 node'][8]
    ]
for x in l:
    digraph.edge(n_dict['type 5 node'][1], x)
    digraph.edge(n_dict['type 2 node'][1], x)
    digraph.edge(x, n_dict['type 3 node'][0])

# single-to-single edges:
digraph.edges([
    (n_dict['type 5 node'][2], n_dict['type 4 node'][9]), 
    (n_dict['type 1 node'][2], n_dict['type 4 node'][9]), 
    (n_dict['type 4 node'][9], n_dict['type 2 node'][1]),
    (n_dict['type 5 node'][3], n_dict['type 2 node'][1])])

# single-to-single edge:
digraph.edge(n_dict['type 5 node'][5], n_dict['type 2 node'][2])

# single-to-single edge:
digraph.edge(n_dict['type 5 node'][6], n_dict['type 1 node'][0])

# single-to-single edge:
digraph.edges([
    (n_dict['type 1 node'][0], n_dict['type 4 node'][4]),
    (n_dict['type 4 node'][4], n_dict['type 2 node'][0])])

# single-to-single edges:
digraph.edges([
    (n_dict['type 1 node'][0], n_dict['type 1 node'][0]), 
    (n_dict['type 2 node'][2], n_dict['type 2 node'][2]),
    (n_dict['type 4 node'][5], n_dict['type 4 node'][5]),
    (n_dict['type 5 node'][5], n_dict['type 5 node'][5])])

# clustered:
with digraph.subgraph(name='cluster_0') as cluster:
    cluster.attr(shape='box', style='bold', color='lightblue2')
    cluster.node(n_dict['type 4 node'][1])
    cluster.node(n_dict['type 4 node'][5])
    cluster.node(n_dict['type 4 node'][9])
    cluster.node(n_dict['type 5 node'][2])

digraph.view()
