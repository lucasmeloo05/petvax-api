# PetVax API - Sistema de Vacinação de Pets

API REST desenvolvida com Django e Django REST Framework para gerenciamento de pets, vacinas e registros de vacinação, implementando autenticação JWT e controle de acesso baseado em papéis (RBAC).

---

## Visão Geral do Projeto

O sistema foi desenvolvido para clínicas veterinárias que necessitam:

- Cadastrar pets e seus responsáveis
- Cadastrar vacinas disponíveis
- Registrar aplicações de vacinas
- Controlar histórico de vacinação
- Garantir que apenas funcionários possam registrar vacinações
- Permitir que donos visualizem apenas seus próprios pets

A API segue o padrão RESTful e implementa controle de acesso baseado em papéis (CLIENTE e FUNCIONARIO).

---

## Tecnologias Utilizadas

- Python 3.13
- Django
- Django REST Framework
- Simple JWT (autenticação)
- SQLite (banco de dados relacional)
- Django Groups (RBAC)
- Django Admin
- Swagger

---

## Controle de Acesso (RBAC)

O sistema utiliza dois papéis principais:

### CLIENTE
- Pode cadastrar e gerenciar seus próprios pets
- Pode visualizar vacinações dos seus pets
- Não pode registrar vacinações
- Não pode cadastrar vacinas

### FUNCIONARIO
- Pode registrar vacinações
- Pode cadastrar/editar vacinas
- Pode visualizar todos os registros
- Pode gerenciar pets (conforme regra definida)

Superusuários possuem acesso total ao sistema.

---

## Como Executar o Projeto Localmente

### 1- Clone o repositório

```bash
git clone https://github.com/lucasmeloo05/petvax-api.git
cd petvax-api
```

### 2- Crie um ambiente virtual

```bash
python -m venv .venv
```

Windows (Funcional apenas no Prompt de Comando):
```bash
.venv\Scripts\activate
```

Powershell:
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\.venv\Scripts\Activate.ps1
```

Linux/Mac:
```bash
source .venv/bin/activate
```

### 3- Instale as dependencias
```bash
pip install -r requirements.txt
```

### 4- Execute as migrações
```bash
python manage.py migrate
```

### 5- Crie um super usuário

```bash
python manage.py createsuperuser
```

*Caso queira criar um usuário comum, após executar o servidor acesse "http://127.0.0.1:8000/api/accounts/register/"*

### 6- Execute o servidor
```bash
python manage.py runserver
```

Acesse a URL informada no terminal (por padrão, `http://127.0.0.1:8000/`)

---

## Executando com Docker (opcional)

Pré-requisito: Docker Desktop instalado.

```bash
docker compose up --build
```

Acesse:

API: http://127.0.0.1:8000/

Docs (Swagger): http://127.0.0.1:8000/api/docs/


---

# Erros comuns e como resolver

## “Port 8000 is already allocated”
Você já tem o Django rodando local.
- Pare o `runserver` local ou mude no compose para `"8001:8000"`

## “Module not found …” dentro do container
- Seu `requirements.txt` pode estar incompleto/encoding errado (UTF-8)
- Rode `docker compose build --no-cache`

## Migrações não aplicando
- Veja logs: `docker compose logs -f`
- Entre no container:
  ```bash
  docker exec -it petvax_api bash
  python manage.py migrate
   ```
   
## 📖 Documentação da API

A documentação interativa da API está disponível em:

http://127.0.0.1:8000/api/docs/

Após realizar login em `/api/auth/token/`, utilize o botão **Authorize** no Swagger e insira o token JWT no formato:

Bearer <access_token>

Isso permitirá testar endpoints protegidos diretamente pela interface web.


## Endpoints da API

### Autenticação
| Método | Endpoint | Descrição |
|--------|----------|-----------|
| POST | `/api/auth/token/` | Login (gera access e refresh) |
| POST | `/api/auth/token/refresh/` | Atualiza token |

### Usuários
| Método | Endpoint | Descrição |
|--------|----------|-----------|
| POST | `/api/accounts/register/` | Cadastro de usuário |

### Pets
| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/api/pets/` | Lista pets do usuário |
| POST | `/api/pets/` | Cadastra pet |
| GET | `/api/pets/{id}/` | Detalha pet |
| PATCH | `/api/pets/{id}/` | Atualiza parcialmente |
| PUT | `/api/pets/{id}/` | Atualiza completamente |
| DELETE | `/api/pets/{id}/` | Remove pet |

### Vacinas
| Método | Endpoint | Permissão |
|--------|----------|-----------|
| GET | `/api/vaccines/` | Autenticado |
| POST | `/api/vaccines/` | FUNCIONARIO |
| PATCH | `/api/vaccines/{id}/` | FUNCIONARIO |
| DELETE | `/api/vaccines/{id}/` | FUNCIONARIO |

### Vacinações
| Método | Endpoint | Permissão |
|--------|----------|-----------|
| GET | `/api/vaccinations/` | Autenticado |
| POST | `/api/vaccinations/` | FUNCIONARIO |
| PATCH | `/api/vaccinations/{id}/` | FUNCIONARIO |
| DELETE | `/api/vaccinations/{id}/` | FUNCIONARIO |

## Decisões Técnicas Adotadas
1. **Arquitetura Modular**
   - Separação por domínio (pets, vaccines, vaccinations, accounts) para melhor organização e escalabilidade.
2. **Uso de JWT**
   - Autenticação baseada em token para simular cenário real de API consumida por frontend/mobile.
3. **RBAC com Django Groups**
   - Controle de acesso baseado em papéis (CLIENTE e FUNCIONARIO).
4. **SQLite**
   - Escolhido para execução local; facilita migração futura para PostgreSQL.
5. **Serializers com campos relacionados**
   - Retornam nomes relacionados (ex: nome do dono, vacina) para melhorar legibilidade da API.

### Possíveis Melhorias Futuras
- Dockerização do projeto
- Testes automatizados
- Deploy em ambiente cloud
- Implementação de multi-clínicas
- Cálculo automático de próxima vacinação

## Autor 
Lucas Mendes Polonio de Melo
