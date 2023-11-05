
# 💻📱 Sistema de Gestão Empresarial (ERP)

Neste curso mergulhamos a fundo na construção de um Sistema de Gestão Empresarial completo utilizando tecnologias de última geração: ReactJS e Django Rest Framework.


## ⛏️ Instalação

Execute o projeto com Python

```bash
  py manage.py runserver
```
    
## 💎 Stacks utilizadas

**Front-end:** ReactJS, TypeScript, React-Router, Redux, Material UI, Axios

**Back-end:** Django, Django Rest Framework, Simple JWT


## 📋 Documentação da API - Authentication

#### Autenticação - Criar Um Conta

```http
  POST /api/v1/auth/signup
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `name` | `string` | **Obrigatório** |
| `email` | `string` | **Obrigatório** |
| `password` | `string` | **Obrigatório** |

#### Autenticação - Fazer Login

```http
  POST /api/v1/auth/signin
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `email` | `string` | **Obrigatório** |
| `password` | `string` | **Obrigatório** |

#### Autenticação - Obter Um Usuário - (_Necessário Autenticação_)

```http
  GET /api/v1/auth/user
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `Authorization` | `string` | **Obrigatório**. Access Token |


## 📋 Documentação da API - Companies - Employees

#### Funcionários - Listar Funcionários De  Uma Empresa - (_Necessário Autenticação_)

```http
  GET /api/v1/companies/employees
```

#### Funcionários - Criar Um Funcionário - (_Necessário Autenticação_)

```http
  POST /api/v1/companies/employees
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `name` | `string` | **Obrigatório** |
| `email` | `string` | **Obrigatório** |
| `password` | `string` | **Obrigatório** |

#### Funcionários - Obter Um Funcionário - (_Necessário Autenticação_)

```http
  GET /api/v1/companies/employees/${id}
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `id` | `number` | **Obrigatório**. ID de um funcionário |

#### Funcionários - Editar Um Funcionário - (_Necessário Autenticação_)

```http
  PUT /api/v1/companies/employees/${id}
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `id` | `number` | **Obrigatório**. ID de um funcionário |
| `groups` | `string` | **Opcional**. String com uma lista de ids de diversos grupos |
| `name` | `string` | **Opcional** |
| `email` | `string` | **Opcional** |

#### Funcionários - Deletar Um Funcionário - (_Necessário Autenticação_)

```http
  DELETE /api/v1/companies/employees/${id}
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `id` | `number` | **Obrigatório**. ID de um funcionário |

## 📋 Documentação da API - Companies - Groups / Permissions

#### Grupos / Cargos - Gupos De Uma Empresa - (_Necessário Autenticação_)

```http
  GET /api/v1/companies/groups
```

#### Grupos / Cargos - Criar Um Grupo - (_Necessário Autenticação_)

```http
  POST /api/v1/companies/groups
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- | 
| `name` | `string` | **Obrigatório** | 
| `permissions` | `string` | **Obrigatório**. String com uma lista de ids de diversas permissões |

#### Grupos / Cargos -  Obter Um Grupo - (_Necessário Autenticação_)

```http
  GET /api/v1/companies/groups/${id}
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- | 
| `id` | `number` | **Obrigatório**. ID de um grupo |

#### Grupos / Cargos - Editar Um Grupo - (_Necessário Autenticação_)

```http
  PUT /api/v1/companies/groups/${id}
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `id` | `number` | **Obrigatório**. ID de um grupo |
| `name` | `string` | **Opcional** | 
| `permissions` | `string` | **Opcional**. String com uma lista de ids de diversas permissões |

#### Grupos / Cargos - Deletar Um Grupo - (_Necessário Autenticação_)

```http
  DELETE /api/v1/companies/groups/${id}
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `id` | `number` | **Obrigatório**. ID de um grupo |

#### Permissões - Permissões Disponíveis - (_Necessário Autenticação_)

```http
  GET /api/v1/companies/permissions
```

## 📋 Documentação da API - Companies - Tasks

#### Tarefas - Tarefas De Uma Empresa - (_Necessário Autenticação_)

```http
  GET /api/v1/companies/tasks
```

#### Tarefas - Criar Um Tarefa - (_Necessário Autenticação_)

```http
  POST /api/v1/companies/tasks
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- | 
| `employee_id` | `number` | **Obrigatório**. ID de um funcionário | 
| `status_id` | `number` | **Obrigatório**. ID de um status de tarefa |
| `title` | `string` | **Obrigatório** |
| `description` | `string` | **Opcional** |
| `due_date` | `date` | **Opcional**. Data no formato: d/m/Y H:M |

#### Tarefas - Obter Uma Tarefa - (_Necessário Autenticação_)

```http
  GET /api/v1/companies/tasks/${id}
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `id` | `number` | **Obrigatório**. ID de uma tarefa |

#### Tarefas - Editar Um Tarefa - (_Necessário Autenticação_)

```http
  PUT /api/v1/companies/tasks/${id}
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `id` | `number` | **Obrigatório**. ID de uma tarefa |
| `employee_id` | `number` | **Opcional**. ID de um funcionário | 
| `status_id` | `number` | **Opcional**. ID de um status de tarefa |
| `title` | `string` | **Opcional** |
| `description` | `string` | **Opcional** |
| `due_date` | `date` | **Opcional**. Data no formato: d/m/Y H:M |

#### Tarefas - Deletar Uma Tarefa - (_Necessário Autenticação_)

```http
  DELETE /api/v1/companies/tasks/${id}
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `id` | `number` | **Obrigatório**. ID de uma tarefa |