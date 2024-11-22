# MovieOverview App

## Descripción

MovieOverview es una aplicación diseñada para interactuar con la API de [The Movie Database (TMDB)](https://www.themoviedb.org/) y proporcionar información estructurada en español sobre las **películas** encontradas en una búsqueda. La aplicación utiliza un modelo de lenguaje natural (LLM) a través del framework **LangChain** para generar respuestas claras y concisas con detalles como título, fecha de estreno y descripción.

Este proyecto incorpora principios de diseño **SOLID** para asegurar una arquitectura limpia y escalable. Además, está configurado para ejecutarse en un entorno **Docker y Docker Compose**, facilitando su despliegue en cualquier máquina o entorno de desarrollo.

---

## Características

- **Consulta de películas**: Integra la API de TMDB para buscar información sobre películas.
- **Procesamiento de lenguaje natural**: Utiliza cualquier modelo LLM compatible con LangChain para generar respuestas estructuradas en español.
- **Plantillas personalizadas**: Configura prompts dinámicos para interactuar eficientemente con el modelo de lenguaje.
- **Diseño modular**: Implementación basada en principios SOLID para alta cohesión y bajo acoplamiento.
- **Contenerización**: Configuración lista para Docker, permitiendo un despliegue ágil y consistente.

---

## Requisitos

- **Python** 3.8 o superior
- **Docker** y **Docker Compose**
- Clave de API de [The Movie Database](https://www.themoviedb.org/settings/api)

---

## Instalación

1. **Clonar el repositorio**
   ```bash
   git clone repo
   cd movie-overview
   docker compose build
   docker compose up
