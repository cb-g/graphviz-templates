# Python 3.9.13
import sys # sys.exit()
import graphviz # graphviz-0.20.1
from graphviz import Graph
from graphfunctions import autolinebreak, get_indices, no_nest_cluster, nested_cluster

# automatic linebreak after these many characters:
max_char = 14

n_dict_sub_1 = {

    # 0:
    'Label: Ba': {
        # 0:
        'Nec sagittis aliquam malesuada bibendum.',
        # 1:
        'Posuere morbi leo urna molestie at.',
        # 2:
        'Aliquet eget sit amet tellus cras.',
        # 3:
        'Enim sit amet venenatis urna cursus eget nunc.',
    },

    # 1:
    'Label: Bb': {
        # 0:
        'Viverra aliquet eget sit amet tellus cras adipiscing.',
        # 1:
        'Lacus sed viverra tellus in.',
        # 2:
        'Ornare lectus sit amet est placerat in egestas erat imperdiet.',
    },

    # 2:
    'Label: Bc': {
        # 0:
        'Condimentum id venenatis a condimentum vitae.',
    },

    # 3:
    'Label: Bd': {
        # 0:
        'Scelerisque eleifend donec pretium vulputate sapien nec sagittis.',
    },
}

outer_list = []
for a in range(len(n_dict_sub_1.keys())):
    inner_list = []
    for b in range(len([[i for i in n_dict_sub_1[k]] for k in n_dict_sub_1.keys()][a])):
        inner_list.append(autolinebreak([[i for i in n_dict_sub_1[k]] for k in n_dict_sub_1.keys()][a][b], max_char))
    outer_list.append(inner_list)
for (i, j) in zip(n_dict_sub_1.keys(), range(len(n_dict_sub_1.keys()))):
    n_dict_sub_1[i] = outer_list[j]

n_dict_sub_3 = {

    # 0:
    'Label: Da': {
        # 0:
        'Posuere urna nec tincidunt praesent semper feugiat nibh.',
        # 1:
        'Porta lorem mollis aliquam ut porttitor.',
    },

    # 1:
    'Label: Db': {
        # 0:
        'Eget duis at tellus at urna condimentum mattis pellentesque.',
        # 1:
        'Leo urna molestie at elementum.',
        # 2:
        'Adipiscing diam donec adipiscing tristique risus nec feugiat.',
        # 3:
        'Pretium vulputate sapien nec sagittis aliquam malesuada bibendum arcu.',
    },

}

outer_list = []
for a in range(len(n_dict_sub_3.keys())):
    inner_list = []
    for b in range(len([[i for i in n_dict_sub_3[k]] for k in n_dict_sub_3.keys()][a])):
        inner_list.append(autolinebreak([[i for i in n_dict_sub_3[k]] for k in n_dict_sub_3.keys()][a][b], max_char))
    outer_list.append(inner_list)
for (i, j) in zip(n_dict_sub_3.keys(), range(len(n_dict_sub_3.keys()))):
    n_dict_sub_3[i] = outer_list[j]

n_dict = {

    # 0:
    'Label: A': {
        # 0:
        'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
        # 1:
        'Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
        # 2:
        'Non diam phasellus vestibulum lorem sed.',
        # 3:
        'Faucibus scelerisque eleifend donec pretium.',
        # 4:
        'Lobortis elementum nibh tellus molestie nunc non blandit massa.',
    },

    # 1:
    'Label: B': n_dict_sub_1,

    # 2:
    'Label: C': {
        # 0:
        'Ac felis donec et odio pellentesque diam volutpat commodo sed.',
        # 1:
        'Dui accumsan sit amet nulla facilisi morbi tempus iaculis.',
        # 2:
        'Pellentesque elit ullamcorper dignissim cras tincidunt lobortis feugiat.',
        # 3:
        'In eu mi bibendum neque egestas.',
        # 4:
        'Erat pellentesque adipiscing commodo elit.',
    },

    # 3:
    'Label: D': n_dict_sub_3,

}

outer_list = []
for a in range(len(n_dict.keys())):
    inner_list = []
    for b in range(len([[i for i in n_dict[k]] for k in n_dict.keys()][a])):
        inner_list.append(autolinebreak([[i for i in n_dict[k]] for k in n_dict.keys()][a][b], max_char))
    outer_list.append(inner_list)
for (i, j) in zip(n_dict.keys(), range(len(n_dict.keys()))):
    n_dict[i] = outer_list[j]

graph = Graph(
    'G',
    format='pdf',
    # format='png', 
    filename='graphs/graph00.gv', 
    engine='fdp')
graph.attr(
    bgcolor='gray20', 
    margin='0'
    )

# style doc:
# https://www.yuque.com/liuwenkan/blog/eddb3e#c0d5fc57
# https://graphviz.gitlab.io/doc/info/shapes.html
# https://graphviz.gitlab.io/doc/info/colors.html
# https://graphviz.gitlab.io/doc/info/attrs.html
# https://graphviz.gitlab.io/doc/info/arrows.html

darkmodecontrast='white'
brightmodecontrast='black'
margin='15'
style='filled'
labelloc='c'
darklove=       ['#401F59', '#61265F', '#812D64', '#A2346A', '#C23B6F', '#E34275'] # https://www.schemecolor.com/dark-love.php
oldwest2=       ['#DCB971', '#7A5D41', '#1A2530', '#3C6B6A', '#DBCB9F', '#D08057'] # https://www.schemecolor.com/old-west-2.php
countryhome=    ['#D06F5C', '#6E4546', '#9E695A', '#BE9B68', '#CCC2AE', '#2B4648'] # https://www.schemecolor.com/country-home.php
# colorscheme=darklove
colorscheme=oldwest2
# colorscheme=countryhome
cluster_args=[graph, n_dict, colorscheme, margin, style, darkmodecontrast, labelloc]
cluster_args=[graph, n_dict, colorscheme, margin, style, darkmodecontrast, labelloc]

# set according to the indices structure of n_dict:
n_dict_subs=[None, n_dict_sub_1, None, n_dict_sub_3]

no_nest_ids, nest_ids = get_indices(n_dict_subs)
for id in no_nest_ids:
    no_nest_cluster(id, cluster_args)
for id in nest_ids:
    nested_cluster(id, cluster_args, n_dict_subs)

graph.view()