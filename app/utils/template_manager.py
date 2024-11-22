from langchain_core.prompts import PromptTemplate


class TemplateManager:
    def __init__(self):
        self.base_template = """Te voy a dar informacion sobre algunas peliculas, me tienes que dar la informacion en (español)
        del titulo, fecha de estreno y resumen de las 3 primeras peliculas que aparezcan de forma estructurada
        (si aparecen menos, me das las que aparezcan).
        {results}"""

    def get_prompt_template(self):
        return PromptTemplate(
            input_variables=["results"],
            template=self.base_template
        )
