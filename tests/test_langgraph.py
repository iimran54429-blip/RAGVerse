from ragverse.agents.graph import build_agent_graph


def main():
    app = build_agent_graph()

    result = app.invoke(
        {
            "question": "What are my technical skills?"
        }
    )

    print("\n=== LANGGRAPH TEST ===")
    print("Route:", result.get("route"))
    print("Documents:", len(result.get("documents", [])))
    print("Context available:", bool(result.get("context")))
    print("Graph context:", bool(result.get("graph_context")))
    print("Memory available:", bool(result.get("conversation_history")))

    if result.get("answer"):
        print("\nAnswer:")
        print(result["answer"])
    else:
        print("\nAnswer generation was not completed.")


if __name__ == "__main__":
    main()