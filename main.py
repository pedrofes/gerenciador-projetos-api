from fastapi import FastAPI

app = FastAPI(
    title="Gerenciador de Projetos e Tarefas",
    description="API para gerenciamento de projetos e tarefas.",
    version="1.0.0"
    ) # app representa a aplicação FastAPI que está sendo criada. É uma instância da classe FastAPI, que é usada para definir rotas, middlewares e outras funcionalidades da aplicação.

@app.get("/") # O decorador @app.get("/") é usado para definir uma rota HTTP GET na raiz ("/") da aplicação. Quando um cliente faz uma solicitação GET para a URL raiz, a função associada a essa rota será executada.
def inicio():
    return {"mensagem": "Gerenciador de Projetos e Tarefas"}

