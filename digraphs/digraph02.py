from graphviz import Digraph
from digraphfunctions import autolinebreak

n_dict = {
    'Monday': [
        'Task 1',
        'Task 2',
        'Task 3',
        'Task 4',
        'Task 5',
    ],
    'Tuesday': [
        'Task 6',
        'Task 7',
        'Task 8',
        'Task 9',
        'Task 10',
    ],
    'Wednesday': [
        'Task 11',
        'Task 12',
        'Task 13',
        'Task 14',
        'Task 15',
    ],
    'Thursday': [
        'Task 16',
        'Task 17',
        'Task 18',
        'Task 19',
        'Task 20',
    ],
    'Friday': [
        'Task 21',
        'Task 22',
        'Task 23',
        'Task 24',
        'Task 25',
    ],
}

# applying automatic linebreak to the dictionary:
max_char = 28
outer_list = []
for a in range(len(n_dict.keys())):
    inner_list = []
    for b in range(len([[i for i in n_dict[k]] for k in n_dict.keys()][a])):
        inner_list.append(autolinebreak([[i for i in n_dict[k]] for k in n_dict.keys()][a][b], max_char))
    outer_list.append(inner_list)

for (i, j) in zip(n_dict.keys(), range(len(n_dict.keys()))):
    n_dict[i] = outer_list[j]

# colors:
backgroundcolor = 'gray20'
boxcolor = '#1A2530'
fontcolor_main = 'white'
fontcolor_clustertitle = '#D08057'
linecolor_cluster = '#D08057'

# graph type:
digraph = Digraph(
    'G',
    format='pdf',
    # format='png',
    filename='digraphs/digraph02.gv'
    )
digraph.attr(
    bgcolor=backgroundcolor, 
    margin='0'
    )

# node style:
digraph.attr('node', shape='box', style='filled', color=boxcolor, fontcolor=fontcolor_main)
for k in list(n_dict.keys()):
    for x in n_dict[k]:
      digraph.node(x)

# single edges:
for n in n_dict.keys():
    for a, b in zip(range(len(n_dict[n])-1), range(1, len(n_dict[n]))):
        digraph.edge(n_dict[n][a], n_dict[n][b])

# clustered:
labelslist = list(n_dict.keys())
dayslist = []
for day in labelslist:
    dayslist.append('cluster_'+day)
for (n, days, labels) in zip(n_dict.keys(), dayslist, labelslist):
    for x in range(len(n_dict[n])):
        with digraph.subgraph(name=days) as cluster:
            cluster.attr(label=labels, shape='box', style='bold', color=linecolor_cluster, fontcolor=fontcolor_clustertitle)
            cluster.node(n_dict[n][x])

digraph.view()
