import numpy as np
import pandas as pd

# originally until_x() from here: https://stackoverflow.com/questions/68905829/creating-a-newline-in-a-string-after-20-characters-at-the-end-of-a-word-python
def autolinebreak(string: str, x: int = 20) -> str:

     lst = string.split()
     line = ''
     str_final = ''
     for word in lst:
         if len(line + ' ' + word) <= x:
             str_final += word + ' '
             line += word + ' '
         else:
             str_final += '\n' +  word + ' '
             line = word + ' '
     return str_final


def get_indices(n_dict_subs):
    
    no_nest_ids = list(np.where(pd.DataFrame(n_dict_subs).duplicated(keep=False))[0])
    nest_ids = []
    for idx in n_dict_subs:
        if idx != None:
            nest_ids.append(n_dict_subs.index(idx))
    return no_nest_ids, nest_ids


def no_nest_cluster(keyidx, cluster_args):

    graph = cluster_args[0]
    n_dict = cluster_args[1]
    colorscheme = cluster_args[2]
    margin = cluster_args[3]
    style = cluster_args[4]
    darkmodecontrast = cluster_args[5]
    labelloc = cluster_args[6]

    with graph.subgraph(name=f'cluster{keyidx}') as c:
        c.attr(label=list(n_dict.keys())[keyidx], fillcolor=colorscheme[keyidx], margin=margin, style=style, fontcolor=darkmodecontrast, pencolor=darkmodecontrast, labelloc=labelloc)
        for x in n_dict[list(n_dict.keys())[keyidx]]:
            c.node(x, color=darkmodecontrast, fontcolor=darkmodecontrast)


def nested_cluster(keyidx, cluster_args, n_dict_subs):

    graph = cluster_args[0]
    n_dict = cluster_args[1]
    colorscheme = cluster_args[2]
    margin = cluster_args[3]
    style = cluster_args[4]
    darkmodecontrast = cluster_args[5]
    labelloc = cluster_args[6]
    n_dict_sub = n_dict_subs[keyidx]

    keyidx_of_subdicts = list(n_dict.keys())[keyidx]
    respective_subdict_length = len(list(n_dict[keyidx_of_subdicts]))

    if respective_subdict_length == 1:
        with graph.subgraph(name=f'cluster{keyidx}') as c:
            c.attr(label=list(n_dict.keys())[keyidx], fillcolor=colorscheme[keyidx], margin=margin, style=style, fontcolor=darkmodecontrast, pencolor=darkmodecontrast, labelloc=labelloc)

            keyidxsub=0
            with c.subgraph(name=f'cluster{keyidx}{keyidxsub}') as c_0:
                c_0.attr(label=list(n_dict_sub.keys())[keyidxsub], fillcolor=colorscheme[keyidx], margin=margin, style=style, fontcolor=darkmodecontrast, pencolor=darkmodecontrast, labelloc=labelloc)
                for x in n_dict_sub[list(n_dict_sub.keys())[keyidxsub]]:
                    c_0.node(x, color=darkmodecontrast, fontcolor=darkmodecontrast)
    
    elif respective_subdict_length == 2:
        with graph.subgraph(name=f'cluster{keyidx}') as c:
            c.attr(label=list(n_dict.keys())[keyidx], fillcolor=colorscheme[keyidx], margin=margin, style=style, fontcolor=darkmodecontrast, pencolor=darkmodecontrast, labelloc=labelloc)

            keyidxsub=0
            with c.subgraph(name=f'cluster{keyidx}{keyidxsub}') as c_0:
                c_0.attr(label=list(n_dict_sub.keys())[keyidxsub], fillcolor=colorscheme[keyidx], margin=margin, style=style, fontcolor=darkmodecontrast, pencolor=darkmodecontrast, labelloc=labelloc)
                for x in n_dict_sub[list(n_dict_sub.keys())[keyidxsub]]:
                    c_0.node(x, color=darkmodecontrast, fontcolor=darkmodecontrast)

            keyidxsub=1
            with c.subgraph(name=f'cluster{keyidx}{keyidxsub}') as c_1:
                c_1.attr(label=list(n_dict_sub.keys())[keyidxsub], fillcolor=colorscheme[keyidx], margin=margin, style=style, fontcolor=darkmodecontrast, pencolor=darkmodecontrast, labelloc=labelloc)
                for x in n_dict_sub[list(n_dict_sub.keys())[keyidxsub]]:
                    c_1.node(x, color=darkmodecontrast, fontcolor=darkmodecontrast)

    elif respective_subdict_length == 3:
        with graph.subgraph(name=f'cluster{keyidx}') as c:
            c.attr(label=list(n_dict.keys())[keyidx], fillcolor=colorscheme[keyidx], margin=margin, style=style, fontcolor=darkmodecontrast, pencolor=darkmodecontrast, labelloc=labelloc)

            keyidxsub=0
            with c.subgraph(name=f'cluster{keyidx}{keyidxsub}') as c_0:
                c_0.attr(label=list(n_dict_sub.keys())[keyidxsub], fillcolor=colorscheme[keyidx], margin=margin, style=style, fontcolor=darkmodecontrast, pencolor=darkmodecontrast, labelloc=labelloc)
                for x in n_dict_sub[list(n_dict_sub.keys())[keyidxsub]]:
                    c_0.node(x, color=darkmodecontrast, fontcolor=darkmodecontrast)

            keyidxsub=1
            with c.subgraph(name=f'cluster{keyidx}{keyidxsub}') as c_1:
                c_1.attr(label=list(n_dict_sub.keys())[keyidxsub], fillcolor=colorscheme[keyidx], margin=margin, style=style, fontcolor=darkmodecontrast, pencolor=darkmodecontrast, labelloc=labelloc)
                for x in n_dict_sub[list(n_dict_sub.keys())[keyidxsub]]:
                    c_1.node(x, color=darkmodecontrast, fontcolor=darkmodecontrast)

            keyidxsub=2
            with c.subgraph(name=f'cluster{keyidx}{keyidxsub}') as c_2:
                c_2.attr(label=list(n_dict_sub.keys())[keyidxsub], fillcolor=colorscheme[keyidx], margin=margin, style=style, fontcolor=darkmodecontrast, pencolor=darkmodecontrast, labelloc=labelloc)
                for x in n_dict_sub[list(n_dict_sub.keys())[keyidxsub]]:
                    c_2.node(x, color=darkmodecontrast, fontcolor=darkmodecontrast)

    elif respective_subdict_length == 4:
        with graph.subgraph(name=f'cluster{keyidx}') as c:
            c.attr(label=list(n_dict.keys())[keyidx], fillcolor=colorscheme[keyidx], margin=margin, style=style, fontcolor=darkmodecontrast, pencolor=darkmodecontrast, labelloc=labelloc)

            keyidxsub=0
            with c.subgraph(name=f'cluster{keyidx}{keyidxsub}') as c_0:
                c_0.attr(label=list(n_dict_sub.keys())[keyidxsub], fillcolor=colorscheme[keyidx], margin=margin, style=style, fontcolor=darkmodecontrast, pencolor=darkmodecontrast, labelloc=labelloc)
                for x in n_dict_sub[list(n_dict_sub.keys())[keyidxsub]]:
                    c_0.node(x, color=darkmodecontrast, fontcolor=darkmodecontrast)

            keyidxsub=1
            with c.subgraph(name=f'cluster{keyidx}{keyidxsub}') as c_1:
                c_1.attr(label=list(n_dict_sub.keys())[keyidxsub], fillcolor=colorscheme[keyidx], margin=margin, style=style, fontcolor=darkmodecontrast, pencolor=darkmodecontrast, labelloc=labelloc)
                for x in n_dict_sub[list(n_dict_sub.keys())[keyidxsub]]:
                    c_1.node(x, color=darkmodecontrast, fontcolor=darkmodecontrast)

            keyidxsub=2
            with c.subgraph(name=f'cluster{keyidx}{keyidxsub}') as c_2:
                c_2.attr(label=list(n_dict_sub.keys())[keyidxsub], fillcolor=colorscheme[keyidx], margin=margin, style=style, fontcolor=darkmodecontrast, pencolor=darkmodecontrast, labelloc=labelloc)
                for x in n_dict_sub[list(n_dict_sub.keys())[keyidxsub]]:
                    c_2.node(x, color=darkmodecontrast, fontcolor=darkmodecontrast)

            keyidxsub=3
            with c.subgraph(name=f'cluster{keyidx}{keyidxsub}') as c_3:
                c_3.attr(label=list(n_dict_sub.keys())[keyidxsub], fillcolor=colorscheme[keyidx], margin=margin, style=style, fontcolor=darkmodecontrast, pencolor=darkmodecontrast, labelloc=labelloc)
                for x in n_dict_sub[list(n_dict_sub.keys())[keyidxsub]]:
                    c_3.node(x, color=darkmodecontrast, fontcolor=darkmodecontrast)

    else:
        print(f'extend the nested_cluster() function to accommodate {keyidx} nested clusters')

