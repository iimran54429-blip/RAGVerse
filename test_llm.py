from ragverse.llm.openai_llm import OpenAILLM


llm = OpenAILLM()

response = llm.generate(
    "What is RAG in one simple sentence?"
)

print("LLM Response:")
print(response)