from graphviz import Digraph

# Create a new directed graph
dot = Digraph(comment='GitHub Assignment Flow with Icons', format='png')

# Set graph-wide attributes
dot.attr(
    bgcolor='white',
    rankdir='LR',       # Left to Right layout
    fontname='Helvetica',
    fontsize='24',      # Bigger font for graph text (like edge labels)
    size='12,8'         # Larger canvas size: 12x8 inches
)

# Common node style with bigger font and thicker borders
common_node_attrs = {
    'style': 'filled,rounded',   # Rounded corners for better look
    'shape': 'box',
    'fontname': 'Helvetica',
    'fontsize': '20',            # Font size inside nodes
    'fontweight': 'bold',
    'color': 'black',
    'penwidth': '2',             # Thicker borders
    'width': '3',                # Increased min width (inches)
    'height': '1.8',             # Increased min height (inches)
    'margin': '0.4,0.3'          # More padding inside nodes
    # Note: 'fixedsize' removed so nodes auto-scale larger if needed
}

# Define nodes with emoji-enhanced labels and colors
nodes = {
    'A': ('🔱 Fork Repo', 'lightblue'),
    'B': ('💻 Clone Repo', 'orange'),
    'C': ('🌿 Create Branch', 'lightgreen'),
    'D': ('📄 Add Assignment', 'lightpink'),
    'E': ('💾 Commit Changes', 'skyblue'),
    'F': ('📤 Push to GitHub', 'plum'),
    'G': ('📬 Create Pull Request', 'gold'),
    'H': ('🔄 Sync Fork (Regular)', 'lightgrey')
}

# Add nodes to graph
for node_id, (label, color) in nodes.items():
    dot.node(node_id, label=label, fillcolor=color, **common_node_attrs)

# Add edges with style and width
dot.edge('A', 'B', color='black', penwidth='2')
dot.edge('B', 'C', color='black', penwidth='2')
dot.edge('C', 'D', color='black', penwidth='2')
dot.edge('D', 'E', color='black', penwidth='2')
dot.edge('E', 'F', color='black', penwidth='2')
dot.edge('F', 'G', color='black', penwidth='2')
dot.edge('C', 'H', style='dashed', color='gray', label='Regular Sync', fontsize='16', fontcolor='gray', penwidth='1.5')

# Render and open the flowchart image
dot.render(r'docs/Git_GitHub/images/github_assignment_flowchart', view=True)
