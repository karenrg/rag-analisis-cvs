from collections import Counter
import matplotlib.pyplot as plt
lista_datos = []

# Función para añadir una fila a la lista de respuestas
def agregar_fila(numero, descripcion):
    fila = (numero, descripcion)
    lista_datos.append(fila)

def imprimir_resultados(lista_datos):
  """Función que imprime los resultados obtenidos"""
  for numero, descripcion in lista_datos:
      print(f"{numero}: {descripcion}")


def graficar_pie_respuestas(lista_datos):
    """
    Genera un gráfico de torta con las proporciones de respuestas y leyendas.

    Parámetros:
        lista_datos (list of tuples): Lista con tuplas (numero, descripcion).
    """
    descripciones = [descripcion for _, descripcion in lista_datos]
    conteo = Counter(descripciones)
    labels = list(conteo.keys())
    sizes = list(conteo.values())
    colors = plt.get_cmap('Set2').colors
    fig, ax = plt.subplots(figsize=(6, 6))
    wedges, texts, autotexts = ax.pie(
        sizes,
        autopct='%1.1f%%',
        startangle=90,
        colors=colors[:len(labels)],
        textprops=dict(color="white")
    )

    legend_labels = [f"{label} ({conteo[label]})" for label in labels]
    ax.legend(wedges, legend_labels, title="Respuestas", loc="center left", bbox_to_anchor=(1, 0.5))

    ax.set_title("Distribución de respuestas")
    ax.axis('equal')

    plt.tight_layout()
    plt.show()