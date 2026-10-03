from ragverse.retrieval.retriever import Retriever
from ragverse.rag.context_builder import build_context
from ragverse.rag.prompt import build_rag_prompt
from ragverse.rag.citations import build_citations
from ragverse.llm.ollama_llm import OllamaLLM


class RAGPipeline:
    def __init__(self):
        self.retriever = Retriever()
        self.llm = OllamaLLM()

    def prepare_prompt(self, question: str) -> dict:
        results = self.retriever.retrieve(
            query=question,
            top_k=3,
        )

        context = build_context(results)

        citations = build_citations(results)

        prompt = build_rag_prompt(
            context=context,
            question=question,
            citations=citations,
        )

        return {
            "prompt": prompt,
            "citations": citations,
        }

    def ask(self, question: str) -> str:
        result = self.prepare_prompt(question)

        answer = self.llm.generate(
            result["prompt"]
        )

        return answer