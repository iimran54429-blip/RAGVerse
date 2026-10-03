from langgraph.graph import END, START, StateGraph

from ragverse.agents.agent_state import AgentState
from ragverse.agents.nodes import (
    route_node,
    memory_node,
    retrieve_node,
    graph_node,
    context_node,
    generate_answer_node,
)


def route_after_classification(state: AgentState) -> str:
    return state.get("route", "simple")


def build_agent_graph():
    graph = StateGraph(AgentState)

    graph.add_node("route", route_node)
    graph.add_node("memory", memory_node)

    # Simple query path
    graph.add_node("simple_retrieve", retrieve_node)

    # Complex query path
    graph.add_node("complex_retrieve", retrieve_node)

    graph.add_node("graph", graph_node)
    graph.add_node("context", context_node)
    graph.add_node("generate_answer", generate_answer_node)

    graph.add_edge(START, "route")

    graph.add_conditional_edges(
        "route",
        route_after_classification,
        {
            "simple": "memory",
            "complex": "memory",
        },
    )

    graph.add_conditional_edges(
        "memory",
        route_after_classification,
        {
            "simple": "simple_retrieve",
            "complex": "complex_retrieve",
        },
    )

    graph.add_edge("simple_retrieve", "graph")
    graph.add_edge("complex_retrieve", "graph")

    graph.add_edge("graph", "context")
    graph.add_edge("context", "generate_answer")
    graph.add_edge("generate_answer", END)

    return graph.compile()