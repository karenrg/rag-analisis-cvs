from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain_community.vectorstores import FAISS
from langchain.chains import create_retrieval_chain

# Función que crea la instacia del modelo llm
def crear_chat(modelo="gpt-4o-mini", temperatura=0.3):
    return ChatOpenAI(model_name=modelo, temperature=temperatura)


# Función para crear el modelo de embeddings de OpenAI
def crear_embeddings(modelo="text-embedding-3-large"):
    """
    Crea una instancia del modelo de embeddings de OpenAI.

    Parámetros:
    - modelo (str): Nombre del modelo de embeddings a utilizar.

    Retorna:
    - Instancia de OpenAIEmbeddings.
    """
    return OpenAIEmbeddings(model=modelo)

# Función para crear una plantilla de prompt personalizada
def crear_prompt():
    """
    Crea una plantilla de prompt para tareas de RAG (retrieval-augmented generation),
    donde se solicita una respuesta basada en un contexto proporcionado.

    Retorna:
    - Instancia de PromptTemplate.
    """
    plantilla = """Responda la siguiente pregunta basándose en el contexto proporcionado, exponga el mayor detalle posible

<context>
{context}
</context>

Pregunta: {input}"""
    return PromptTemplate.from_template(plantilla)