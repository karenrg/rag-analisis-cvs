import requests

def construir_url_contenido(user: str, repo: str, carpeta: str = ""):
    base = f"https://api.github.com/repos/{user}/{repo}/contents"
    return f"{base}/{carpeta}" if carpeta else base


# Función para leer los archivos PDF desde la ubicación en Github
def obtener_archivos_github(user, repo, carpeta):
    url = f"https://api.github.com/repos/{user}/{repo}/contents/{carpeta}"
    response = requests.get(url)

    if response.status_code == 200:
        archivos = response.json()
        nombres = [f["name"] for f in archivos if f["type"] == "file"]
        return nombres
    else:
        print("Error al acceder al repositorio:", response.status_code)
        return []