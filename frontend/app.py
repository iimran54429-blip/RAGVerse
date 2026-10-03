import requests
import streamlit as st


API_URL = "http://127.0.0.1:8000"


st.set_page_config(
    page_title="RAGVerse",
    page_icon="🤖",
    layout="wide",
)


# -----------------------------
# Session State
# -----------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []


# -----------------------------
# Header
# -----------------------------

st.title("🤖 RAGVerse")
st.caption("Advanced AI Knowledge Assistant")
st.markdown(
    "Upload your documents and ask questions using "
    "retrieval-augmented generation."
)


# -----------------------------
# Sidebar
# -----------------------------

with st.sidebar:
    st.header("RAGVerse")

    st.markdown("### System")
    
    try:
        health = requests.get(
            f"{API_URL}/health",
            timeout=5,
        )

        if health.ok:
            st.success("API Online")
        else:
            st.error("API Unhealthy")

    except requests.exceptions.RequestException:
        st.error("API Offline")

    st.divider()

    st.markdown("### Capabilities")
    st.write("✓ PDF / TXT / DOCX")
    st.write("✓ Vector Search")
    st.write("✓ Hybrid Retrieval")
    st.write("✓ Reranking")
    st.write("✓ Adaptive RAG")
    st.write("✓ LangGraph")
    st.write("✓ Citations")
    st.write("✓ Conversation Memory")

    st.divider()

    if st.button(
        "Clear Chat",
        use_container_width=True,
    ):
        st.session_state.messages = []
        st.rerun()


# -----------------------------
# Main Tabs
# -----------------------------

tab_chat, tab_upload = st.tabs(
    [
        "💬 Chat",
        "📄 Documents",
    ]
)


# ============================================================
# CHAT
# ============================================================

with tab_chat:

    # Previous messages
    for message in st.session_state.messages:

        with st.chat_message(
            message["role"]
        ):
            st.markdown(
                message["content"]
            )

            if (
                message["role"] == "assistant"
                and message.get("citations")
            ):
                with st.expander(
                    "📚 Sources"
                ):
                    for citation in message["citations"]:
                        st.write(
                            f"{citation.get('citation_id', '')} "
                            f"— "
                            f"{citation.get('document_name', '')} "
                            f"(chunk "
                            f"{citation.get('chunk_index', '')})"
                        )


    # Chat input
    question = st.chat_input(
        "Ask something about your documents..."
    )


    if question:

        # User message
        st.session_state.messages.append(
            {
                "role": "user",
                "content": question,
            }
        )

        with st.chat_message("user"):
            st.markdown(question)


        # Assistant response
        with st.chat_message("assistant"):

            with st.spinner(
                "RAGVerse is thinking..."
            ):
                try:

                    response = requests.post(
                        f"{API_URL}/query",
                        json={
                            "question": question
                        },
                        timeout=180,
                    )

                    response.raise_for_status()

                    data = response.json()

                    answer = data.get(
                        "answer",
                        "No answer generated.",
                    )

                    citations = data.get(
                        "citations",
                        [],
                    )

                    route = data.get(
                        "route",
                        "unknown",
                    )

                    st.markdown(answer)

                    # Metadata
                    col1, col2 = st.columns(2)

                    with col1:
                        st.caption(
                            f"Route: `{route}`"
                        )

                    with col2:
                        st.caption(
                            f"Sources: `{len(citations)}`"
                        )


                    # Sources
                    if citations:

                        with st.expander(
                            "📚 View Sources"
                        ):

                            for citation in citations:

                                st.write(
                                    f"{citation.get('citation_id', '')} "
                                    f"— "
                                    f"{citation.get('document_name', '')}"
                                )

                                st.caption(
                                    f"Chunk: "
                                    f"{citation.get('chunk_index', '')}"
                                )


                    # Save assistant message
                    st.session_state.messages.append(
                        {
                            "role": "assistant",
                            "content": answer,
                            "citations": citations,
                        }
                    )


                except requests.exceptions.RequestException as exc:

                    error_message = (
                        f"Could not connect to RAGVerse API: {exc}"
                    )

                    st.error(error_message)

                    st.session_state.messages.append(
                        {
                            "role": "assistant",
                            "content": error_message,
                            "citations": [],
                        }
                    )


                except Exception as exc:

                    error_message = (
                        f"Unexpected error: {exc}"
                    )

                    st.error(error_message)

                    st.session_state.messages.append(
                        {
                            "role": "assistant",
                            "content": error_message,
                            "citations": [],
                        }
                    )


# ============================================================
# DOCUMENT UPLOAD
# ============================================================

with tab_upload:

    st.subheader("📄 Upload & Index Document")

    st.write(
        "Supported formats: PDF, TXT, DOCX"
    )


    uploaded_file = st.file_uploader(
        "Choose a document",
        type=[
            "pdf",
            "txt",
            "docx",
        ],
    )


    if uploaded_file:

        st.info(
            f"Selected: **{uploaded_file.name}**"
        )


    if st.button(
        "🚀 Upload & Index",
        type="primary",
        use_container_width=True,
    ):

        if uploaded_file is None:

            st.warning(
                "Please select a document first."
            )

        else:

            with st.spinner(
                "Processing and indexing document..."
            ):

                try:

                    response = requests.post(
                        f"{API_URL}/upload",
                        files={
                            "file": (
                                uploaded_file.name,
                                uploaded_file.getvalue(),
                                uploaded_file.type,
                            )
                        },
                        timeout=300,
                    )

                    response.raise_for_status()

                    data = response.json()

                    st.success(
                        data.get(
                            "message",
                            "Document indexed successfully.",
                        )
                    )

                    with st.expander(
                        "View indexing details"
                    ):
                        st.json(data)

                except requests.exceptions.RequestException as exc:

                    st.error(
                        f"Upload failed: {exc}"
                    )

                except Exception as exc:

                    st.error(
                        f"Unexpected error: {exc}"
                    )