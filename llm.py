from langchain_ollama import ChatOllama


llm = ChatOllama(
    model="deepseek-r1:8b",
    temperature=0,
)


prompt = "If i give you a newsportal link, can you give me a desctiption on it in 100 word. the newsporal link is https://www.prothomalo.com/"

print(llm.invoke(prompt).content)
