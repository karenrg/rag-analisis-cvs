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
    - [LangChain](https://www.langchain.com/)
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

    2. Crear y configurar el archivo .env
    Debés crear un archivo .env con base en el archivo de ejemplo incluido:
    ```bash
    cp .env.example .env

    Las variables GITHUB_USER, GITHUB_REPO y GITHUB_FOLDER ya apuntan a una base de datos funcional para pruebas. Podés reemplazarlas si querés analizar otro repositorio.

    3. Instalar dependencias
    ```bash
    pip install -r requirements.txt

    4. Para probar las consultas, en el archivo rag_notebook.ipynb agregar celdas como:
    ```python
    response = retrieval_chain.invoke(
        {"input": "¿Fabio Diaz tiebe experiencia laboral en AGRO Futurista-Coopetrol?"})
    print(response["answer"])
    
    en donde en el imput se escribe la consulta acerca del corpus en cuestión

    ##Informe y resultados
    Podés el informe técnico y los resultados de prueba se encuentran en:
    [documents/Articulo_AnalisisPerfilesTI.pdf](documents/Articulo_AnalisisPerfilesTI.pdf): Informe detallado del proyecto.
    [documents/NotebookResultados.pdf](documents/NotebookResultados.pdf): evidencia de resultados generados por el sistema.