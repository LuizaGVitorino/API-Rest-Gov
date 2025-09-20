# Trabalho de Projetos -- aula de sexta feira

## Desenvolver uma API rest com um dado aberto do governo
### Dado utilizado: 
[Características dos produtos da saúde suplementar](https://dados.gov.br/dados/conjuntos-dados/caracteristicas-dos-produtos-da-saude-suplementar)

### Criação de um ambiente virtual
```python -m venv venv```

### Ativação
```venv\Scripts\activate```

### Instalação das bibliotecas necessárias
<p> Aqui o ambiente virtual está ativado e foi instalado as bibliotecas: FastAPI, Uvicorn (para rodar o servidor), SQLAlchemy e Python-jose (para JWT). </p>

```pip install fastapi "uvicorn[standard]" sqlalchemy python-jose[cryptography] passlib[bcrypt]```

### Pastas
```.
├── app/
│   ├── __init__.py
│   ├── main.py        # Onde o FastAPI será inicializado
│   ├── database.py    # Conexão com o SQLite
│   ├── models/        # Schemas do SQLAlchemy
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── data_models.py
│   ├── schemas/       # Schemas do Pydantic (validação de dados)
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── data_schemas.py
│   ├── services/      # Lógica de negócio
│   │   ├── __init__.py
│   │   └── data_service.py
│   └── routers/       # Endpoints da API
│       ├── __init__.py
│       ├── auth.py
│       └── data_routes.py
├── .gitignore
├── README.md
├── requirements.txt

```

### Execução do servidor
O --reload faz o servidor reiniciar automaticamente ao detectar mudanças.

```
uvicorn app.main:app --reload
```

### Acesso a interface Swagger
Acesse a documentação da sua API em: http://127.0.0.1:8000/docs -- documentação automática.

### Testes -- Utilização do Postman
Coleção com testes para todos os endpoints (CRUD e autenticação).
<p>Token de autorização: {{access_token}} -- Isso fará com que todas as requisições desta coleção usem automaticamente um token que será salvo na variável access_token mais tarde</p>

### Access token
{
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTc1ODM5Mjc0MH0.8PljV0Qww-sDqp0tCrl8Gf7jzMj2JqxymJrUbDT_EwQ",
    "token_type": "bearer"
}

### Diagrama entidade relacionamento
![DIAGRAMA ER - API GOV](https://github.com/user-attachments/assets/fa313252-1142-42a4-a975-bcf4a736074e)

### Fluxograma
![fluxograma fast appi gov](https://github.com/user-attachments/assets/1afefde1-4c39-4d9a-8937-8a763c781d7a)

