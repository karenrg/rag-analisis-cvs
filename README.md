# Análisis de perfiles TI con IA

Este proyecto implementa un sistema de análisis inteligente de currículums vitae (CVs) para puestos en el área de Tecnologías de la Información (TI), utilizando una arquitectura RAG (Retrieval-Augmented Generation). El objetivo es asistir a reclutadores sugiriendo candidatos adecuados a partir de una base de datos de CVs y una descripción del puesto.

---

## Integrantes

- Karen Riveros  
- Jorge Benítez  
- Amanda Sosa

---

## Objetivo del proyecto

Reducir el tiempo y esfuerzo en la selección de talento en TI mediante un prototipo funcional que:
- Indexa CVs de profesionales del área.
- Permite recuperar candidatos relevantes usando FAISS y LangChain.
- Genera recomendaciones basadas en un prompt con requisitos del puesto.

---

## Tecnologías utilizadas

- Python 3.10+
- [LangChain](https://www.langchain.com/)
- OpenAI (vía `langchain-openai`)
- FAISS (para recuperación semántica)
- PyPDF (extracción de texto)
- dotenv (gestión de variables de entorno)

---

## Instalación

1. Cloná el repositorio:

```bash
git clone https://github.com/tu-usuario/rag-analisis-cvs.git
cd rag-talent-selection
