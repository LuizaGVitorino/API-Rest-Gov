# Trabalho de Projetos -- aula de sexta feira

## Desenvolver uma API rest com um dado aberto do governo
### Dado utilizado: 
[Características dos produtos da saúde suplementar](https://dados.gov.br/dados/conjuntos-dados/caracteristicas-dos-produtos-da-saude-suplementar)

### Testes -- Utilização do Postman
Coleção com testes para todos os endpoints (CRUD e autenticação).
<p>Token de autorização: {{access_token}} -- Isso fará com que todas as requisições desta coleção usem automaticamente um token que será salvo na variável access_token mais tarde</p>

### Access token
{
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTc1ODM5Mjc0MH0.8PljV0Qww-sDqp0tCrl8Gf7jzMj2JqxymJrUbDT_EwQ",
    "token_type": "bearer"
}

# RELATÓRIO
## 1. Introdução

Este relatório técnico detalha o desenvolvimento de uma API RESTful para consulta e gestão de dados públicos, com foco nos dados de "Características dos produtos da saúde suplementar" disponibilizados pelo portal dados.gov.br. O objetivo principal do projeto foi construir uma aplicação robusta e segura, capaz de estruturar, armazenar e expor esses dados de forma programática.

A solução foi implementada utilizando o framework **FastAPI**, escolhido por sua alta performance e facilidade de uso para a criação de APIs modernas em Python. O gerenciamento de dados foi realizado com a biblioteca **SQLAlchemy**, que atua como um Mapeador Objeto-Relacional (ORM), permitindo a interação com o banco de dados **SQLite** através de objetos Python.

Para garantir a segurança dos endpoints que manipulam os dados, a autenticação de usuários foi implementada com o padrão **JSON Web Token (JWT)**. Isso assegura que apenas usuários devidamente autorizados possam realizar operações de criação, atualização e exclusão de informações.

O projeto demonstra a capacidade de consumir dados públicos e transformá-los em um serviço acessível e seguro, seguindo as melhores práticas de desenvolvimento de software.

## 2. Modelagem de Dados

A arquitetura do banco de dados foi projetada para refletir a estrutura dos dados de saúde suplementar, utilizando um modelo relacional que garante a integridade e a organização das informações. A modelagem foi desenvolvida com base nas entidades do dataset e suas interconexões.

O diagrama de Entidade-Relacionamento (ER) a seguir ilustra a estrutura do banco de dados:

![DIAGRAMA ER - API GOV](https://github.com/user-attachments/assets/fa313252-1142-42a4-a975-bcf4a736074e)

### Entidades e Relacionamentos

* **`Operadora`**: Esta entidade representa a empresa de saúde suplementar. Ela possui atributos como `id`, `nome` e `razao_social`. Uma única operadora pode ter múltiplos produtos, estabelecendo uma relação de um-para-muitos (1:N) com a entidade `Produto`.

* **`Segmentacao`**: Reflete o tipo de cobertura do plano (por exemplo, "Ambulatorial"). Possui atributos como `id` e `tipo`. A relação com a entidade `Produto` também é de um-para-muitos (1:N), já que uma segmentação pode ser aplicada a vários produtos.

* **`Produto`**: A entidade central que representa um plano de saúde. Ela contém informações como `nome`, `numero_registro` e `tipo_cobertura`. Para associar um produto a uma operadora e a uma segmentação, ela utiliza as chaves estrangeiras (`operadora_id` e `segmentacao_id`).

* **`User`**: Uma entidade dedicada à autenticação e autorização. Possui atributos como `id`, `username` e `hashed_password`. Embora seja uma entidade do banco de dados, ela não se relaciona diretamente com os dados dos produtos, mas sim com a segurança da API.

Esta modelagem permite que o sistema organize e acesse os dados de forma eficiente, seguindo as melhores práticas de design de banco de dados relacional.

## 3. Endpoints da API

A API foi projetada com endpoints RESTful que permitem a interação completa com as entidades do banco de dados, seguindo os princípios de criação, leitura, atualização e exclusão (CRUD). As rotas são organizadas por tags para facilitar a navegação na documentação interativa do Swagger UI.

### 3.1. Endpoints de Autenticação

Estes endpoints são essenciais para gerenciar o acesso à API.

* **`POST /auth/register`**
    * **Função**: Cria um novo usuário na base de dados.
    * **Acesso**: Público.

* **`POST /auth/token`**
    * **Função**: Autentica um usuário com suas credenciais (username e password) e retorna um JSON Web Token (JWT) para acesso a endpoints protegidos.
    * **Acesso**: Público.

### 3.2. Endpoints de Dados (Protegidos)

As rotas a seguir exigem que o usuário forneça um token JWT válido no cabeçalho da requisição para serem acessadas.

* **`POST /operadoras/`**
    * **Função**: Cria um novo registro de operadora no banco de dados.
    * **Acesso**: Protegido.

* **`POST /segmentacoes/`**
    * **Função**: Cria um novo registro de segmentação no banco de dados.
    * **Acesso**: Protegido.

* **`POST /produtos/`**
    * **Função**: Cria um novo registro de produto, associando-o a uma operadora e a uma segmentação existentes.
    * **Acesso**: Protegido.

### 3.3. Endpoints de Dados (Públicos)

Estas rotas são para consulta de dados e não requerem autenticação.

* **`GET /operadoras/`**
    * **Função**: Retorna uma lista de todas as operadoras cadastradas.
    * **Acesso**: Público.

* **`GET /segmentacoes/`**
    * **Função**: Retorna uma lista de todas as segmentações cadastradas.
    * **Acesso**: Público.

* **`GET /produtos/`**
    * **Função**: Retorna uma lista de todos os produtos cadastrados.
    * **Acesso**: Público.]
      
## 4. Instruções de Execução

Para configurar e executar a API localmente, siga os passos abaixo. É recomendado o uso do **Visual Studio Code** com o terminal integrado.

### 4.1. Pré-requisitos

Certifique-se de ter o **Python 3.8+** e o **Git** instalados na sua máquina.

### 4.2. Clonar o Repositório

Abra o terminal e clone o projeto do GitHub para a sua máquina.

```
git clone [https://github.com/LuizaGVitorino/APIrest_trabalho.git](https://github.com/LuizaGVitorino/API-Rest-Gov/)
cd APIrest_trabalho
```
### 4.3 Configuração do ambiente virtual
Crie e ative um aambiente virtual para que possa instalar as depenências de forma isolada
* No **Windows** copie e cole no terminal:
```
python -m venv .venv
.venv\Scripts\activate
```
* No **Linux  ou MacOS** copie e cole:
```
python3 -m venv .venv
source .venv/bin/activate
```

### 4.4 Instalar as dependências
No ambiente virtual ativado, instale as bibliotecas necessárias para o projeto:
```
pip install -r requirements.txt
```
Abaixo, será instalado as bibliotecas: FastAPI, Uvicorn (para rodar o servidor), SQLAlchemy e Python-jose (para JWT). </p>

```pip install fastapi "uvicorn[standard]" sqlalchemy python-jose[cryptography] passlib[bcrypt]```

### 4.5 Execução da API
Inicie o servidor Uvicorn para que a API seja executada localmente. O modo `--reload` permite que o servidor reinicie automaticamente a cada alteração no código.

```
uvicorn main:app --reload
```
A API estará disponível em http://127.0.0.1:8000

### 4.6. Acessar a Documentação Interativa
Com a API em execução, acesse a documentação interativa para testar os endpoints:
* Swagger UI: http://127.0.0.1:8000/docs
* Redoc: http://127.0.0.1:8000/redoc

## 5. Conclusão

O desenvolvimento desta API RESTful demonstrou a aplicação prática de conceitos de programação e arquitetura de software para resolver um problema real de gestão de dados públicos. O projeto resultou em uma solução completa, que vai desde a modelagem de um banco de dados relacional até a criação de endpoints seguros e documentados.

A utilização do FastAPI, combinada com o SQLAlchemy, provou ser uma escolha eficiente para a criação de uma API performática e com código limpo. A implementação do sistema de autenticação com JWT garantiu que a API não apenas disponibiliza os dados, mas também os protege, permitindo o acesso apenas a usuários autorizados para operações críticas como a inserção de novos registros.

Em suma, este trabalho consolida o entendimento sobre o ciclo de vida de uma API, desde a concepção e modelagem até a implementação e documentação. A API está pronta para ser expandida, podendo servir como a base para futuros desenvolvimentos ou integrações.

