from graphviz import Digraph
from DecisionTree import Node  # Importa a classe Node do seu código

def export_tree_to_graphviz(tree, feature_names=None, class_names=None):
    # Exporta a árvore para formato Graphviz
    dot = Digraph(comment="Decision Tree")
    
    def _add_nodes(node, parent=None, decision=None):
        if node.is_leaf_node():
            # Nó folha
            if class_names is not None:
                label = f"Classe: {class_names[node.value]}"
            else:
                label = f"Classe {node.value}"
            node_id = f"leaf_{id(node)}"
            dot.node(node_id, label=label, shape="box", fillcolor="lightblue")
            if parent:
                dot.edge(parent, node_id, label=decision)
        else:
            # Nó de decisão
            if feature_names is not None:
                feature_name = feature_names[node.feature]
            else:
                feature_name = f"Feature {node.feature}"
            label = f"{feature_name} ≤ {node.threshold:.2f}"
            node_id = f"node_{id(node)}"
            dot.node(node_id, label=label)
            
            if parent:
                dot.edge(parent, node_id, label=decision)
            
            # Recursão para filhos
            _add_nodes(node.left, node_id, "Sim")
            _add_nodes(node.right, node_id, "Não")
    
    _add_nodes(tree.root)
    return dot