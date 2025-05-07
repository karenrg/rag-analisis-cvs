# Análisis de perfiles TI con IA

Este proyecto implementa un sistema de análisis inteligente de currículums vitae (CVs) para puestos en el área de Tecnologías de la Información (TI), utilizando una arquitectura RAG (Retrieval-Augmented Generation). El objetivo es asistir a reclutadores sugiriendo candidatos adecuados a partir de una base de datos de CVs y una descripción del puesto.

---

## Integrantes

- Karen Riveros  
- Jorge Benítez  
- Amanda Sosa

---

## Tecnologías utilizadas

- Python 3.10+
- LangChain
- OpenAI (vía `langchain-openai`)
- FAISS (para recuperación semántica)
- PyPDF (extracción de texto)
- dotenv (gestión de variables de entorno)
---

## Implementación

1. Cloná el repositorio:

```bash
git clone https://github.com/tu-usuario/rag-analisis-cvs.git
cd rag-talent-selection
```

2. Crear y configurar el archivo .env
Debés crear un archivo .env con base en el archivo de ejemplo incluido:
[.env.example](.env.example)

Las variables GITHUB_USER, GITHUB_REPO y GITHUB_FOLDER ya apuntan a una base de datos funcional para pruebas. Podés reemplazarlas si querés analizar otro repositorio.

3. Instalar dependencias
```bash
pip install -r requirements.txt
```
4. Para probar las consultas, en el archivo [rag_notebook.ipynb](rag_notebook.ipynb) agregar celdas como:
```python
response = retrieval_chain.invoke(
{"input": "Lístame el nombre de personas con formación académica de maestría en ciencia de datos"})
print(response["answer"])
```    
en donde en el campo **input** se escribe la consulta acerca del corpus en cuestión. Al ejecutar la celda, se imprime la respuesta.

## Informe y resultados
El informe técnico y los resultados de prueba se encuentran en:
- [documents/Articulo_AnalisisPerfilesTI.pdf](documents/Articulo_AnalisisPerfilesTI.pdf): Informe detallado del proyecto.
- [documents/NotebookResultados.pdf](documents/NotebookResultados.pdf): Documentación de resultados generados por el sistema.
