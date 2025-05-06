import io
import requests
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader



# Función para descargar, cargar y dividir PDFs desde un repositorio GitHub.
def cargar_pdfs_desde_github(files, usuario, repositorio, carpeta, text_splitter):
    """
    Descarga, carga y divide PDFs desde un repositorio GitHub.
    """
    text = []
    for file in files:
        print(f"Procesando: {file}")
        carpeta_path = f"{carpeta}/" if carpeta else ""
        raw_url = f"https://raw.githubusercontent.com/{usuario}/{repositorio}/main/{carpeta_path}{file}"

        try:
            response = requests.get(raw_url)
            response.raise_for_status()

            tmp_path = f"/tmp/{file}"
            with open(tmp_path, "wb") as f:
                f.write(response.content)

            loader = PyPDFLoader(tmp_path)
            pages = loader.load()
            documents = text_splitter.split_documents(pages)
            text.extend(documents)

        except Exception as e:
            print(f"Error al procesar {file}: {e}")

    return text

# Función para dividir los textos - 1000 100  El mejor parámetro de momento  2000 / 200 - Particionar cada documentos en segmentos
def create_text_splitter():
  text_splitter = RecursiveCharacterTextSplitter(
      chunk_size=2000,
      chunk_overlap=200,
      separators=["\n\n", "\n", ". ", " ", ""],
      strip_whitespace=True
  )
  return text_splitter  