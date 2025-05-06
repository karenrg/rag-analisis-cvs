from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain_community.vectorstores import FAISS
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain


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
    plantilla = """Responda la siguiente pregunta como un experto en Recursos Humanos especializado en reclutamiento de perfiles IT, basándose en el contexto proporcionado, exponga el mayor detalle posible

<context>
{context}
</context>

Pregunta: {input}"""
    return PromptTemplate.from_template(plantilla)

# Generación de cadena de recuperación (RAG) con embeddings y FAISS
def generar_embeddings(pages, embeddings, chat, prompt):
  ## Transformar a vector los segmentos de documentos
  vector = FAISS.from_documents(pages,
                              embeddings)
  document_chain = create_stuff_documents_chain(chat, prompt) #asociar el LLM con el prompt
  #Crear el objetos que recupera los documentos a partir de una consulta
  retriever = vector.as_retriever(search_kwargs={"k": 15}) #cantidad de documentos similares a recuperar
  retrieval_chain = create_retrieval_chain(retriever, document_chain) #Asociar el objeto consultador con el LLM y el prompt
  return retrieval_chain