from dataclasses import dataclass, field


@dataclass
class GraphNode:
    node_id: str
    node_type: str
    name: str


@dataclass
class GraphEdge:
    source: str
    relation: str
    target: str


class KnowledgeGraph:
    """
    Lightweight in-memory knowledge graph foundation.
    """

    def __init__(self):
        self.nodes: dict[str, GraphNode] = {}
        self.edges: list[GraphEdge] = []

    def add_node(
        self,
        node_id: str,
        node_type: str,
        name: str,
    ) -> None:
        self.nodes[node_id] = GraphNode(
            node_id=node_id,
            node_type=node_type,
            name=name,
        )

    def add_edge(
        self,
        source: str,
        relation: str,
        target: str,
    ) -> None:
        self.edges.append(
            GraphEdge(
                source=source,
                relation=relation,
                target=target,
            )
        )

    def get_neighbors(self, node_id: str) -> list[GraphNode]:
        neighbor_ids = []

        for edge in self.edges:
            if edge.source == node_id:
                neighbor_ids.append(edge.target)

            elif edge.target == node_id:
                neighbor_ids.append(edge.source)

        return [
            self.nodes[node_id]
            for node_id in neighbor_ids
            if node_id in self.nodes
        ]