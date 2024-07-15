from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate

ollama = Ollama(base_url="http://localhost:11434", model="llama3")
print(ollama.invoke('Who is Elon Musk?'))
