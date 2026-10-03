from ragverse.graph_rag.knowledge_graph import KnowledgeGraph, GraphNode


class GraphRetriever:
    def __init__(self, graph: KnowledgeGraph | None = None):
        self.graph = graph or KnowledgeGraph()

    def add_document_relationship(
        self,
        document_id: str,
        document_name: str,
        chunk_id: str,
    ) -> None:
        self.graph.add_node(
            node_id=document_id,
            node_type="document",
            name=document_name,
        )

        self.graph.add_node(
            node_id=chunk_id,
            node_type="chunk",
            name=chunk_id,
        )

        self.graph.add_edge(
            source=document_id,
            relation="contains",
            target=chunk_id,
        )

    def get_related_nodes(self, node_id: str) -> list[GraphNode]:
        return self.graph.get_neighbors(node_id)

    def retrieve_neighbors(
        self,
        node_id: str,
        max_hops: int = 1,
    ) -> list[GraphNode]:
        if not node_id or max_hops <= 0:
            return []

        visited = {node_id}
        current_nodes = [node_id]
        results = []

        for _ in range(max_hops):
            next_nodes = []

            for current_node in current_nodes:
                neighbors = self.graph.get_neighbors(current_node)

                for neighbor in neighbors:
                    if neighbor.node_id not in visited:
                        visited.add(neighbor.node_id)
                        results.append(neighbor)
                        next_nodes.append(neighbor.node_id)

            current_nodes = next_nodes

            if not current_nodes:
                break

        return results