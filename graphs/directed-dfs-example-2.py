connections = [
    ("A", "B"),
    ("C", "B"),
    ("D", "C"),
    ("D", "E"),
    ("F", "E"),
    ("G", "F"),
    ("H", "G"),
    ("A", "H"),
    ("G", "A"),
    ("G", "B"),
    ("B", "F"),
    ("F", "C"),
    ("F", "D"),
]


G = engine.DiGraph(connections)


# Preparation
STATE_DEFAULT = 0
STATE_OPENED = 1
STATE_CLOSED = 2

for v in G.nodes:
    G.nodes[v]["state"] = STATE_DEFAULT
    G.nodes[v]["pred"] = None

# Style
G.color_nodes_by(prop="state", colors=["default", "blue", "yellow"])


# Algorithm
def dfs_step(u):
    G.nodes[u]["state"] = STATE_OPENED

    for v in G.adj[u]:
        if G.nodes[v]["state"] == STATE_DEFAULT:
            G.nodes[v]["pred"] = u
            dfs_step(v)
        elif G.nodes[u]["pred"] != v:
            G.edges[u, v]["back"] = True

    G.nodes[u]["state"] = STATE_CLOSED


for u in G.nodes:
    if G.nodes[u]["state"] == STATE_DEFAULT:
        print(f"Starting in {u}")
        dfs_step(u)
