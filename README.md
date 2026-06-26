# 🏦 Banking System L.I.M.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![POO](https://img.shields.io/badge/POO-1E293B?style=for-the-badge&logo=python&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)
![GitLabFlow](https://img.shields.io/badge/Flow-GitLabFlow-orange?style=for-the-badge)
![Console](https://img.shields.io/badge/Interface-Console-4CAF50?style=for-the-badge)
![Pytest](https://img.shields.io/badge/Tests-Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)

Projeto acadêmico desenvolvido em Python com o objetivo de simular um sistema bancário, permitindo operações essenciais como cadastro de conta, consulta de saldo, crédito, débito, transferência e rendimento. O sistema foi planejado com separação em camadas, buscando melhor organização do código e reaproveitamento de componentes, além de contar com uma API REST e testes unitários.


---

## ✨ Funcionalidades

- **Cadastrar Conta** - Criação de contas dos tipos: normal, bônus e poupança
- **Consultar Saldo** - Exibição do saldo atual da conta
- **Consultar Dados** - Exibição de dados completos da conta (tipo, saldo, pontuação)
- **Crédito** - Adição de valores à conta (com bonificação para conta bônus)
- **Débito** - Retirada de valores da conta
- **Transferência** - Transferência de valores entre contas (com bonificação para conta bônus destino)
- **Render Juros** - Aplicação de taxa de juros em todas as contas poupança

---

## 🛠️ Linguagem e Stack de Desenvolvimento

- **Python** - Linguagem principal do projeto
- **Programação Orientada a Objetos (POO)** - Modelagem das entidades e regras de negócio
- **Arquitetura em Camadas** - Separação entre interface e camada de negócio
- **FastAPI** - Framework para construção da API REST
- **Pytest** - Framework para testes unitários
- **Git e GitHub** - Versionamento e gerenciamento do repositório
- **Console / API** - Interação via terminal ou requisições HTTP

---

## 📁 Estrutura do Projeto

```
banking-system-lim-dim0517/
├── api/                    # Camada REST (FastAPI)
│   └── app.py
├── controller/             # Camada de interface (console)
│   └── conta_controller.py
├── models/                 # Entidades do domínio
│   ├── conta.py
│   ├── conta_bonus.py
│   └── conta_poupanca.py
├── repositories/           # Camada de armazenamento
│   └── conta_repository.py
├── services/               # Regras de negócio
│   ├── conta_service.py
│   └── conta_poupanca_service.py
├── tests/                  # Testes unitários
│   └── test_services.py
├── main.py                 # Entrypoint do console
├── requirements.txt
└── README.md
```

---

## ▶️ Como Executar o Sistema

### Pré-requisitos

- Ter o **Python 3** instalado na máquina
- Ter o **Git** instalado, caso deseje clonar o repositório

### Passo a passo

1. Clone o repositório:

```bash
git clone https://github.com/luan-sampaio/banking-system-lim-dim0517.git
```

2. Acesse a pasta do projeto:

```bash
cd banking-system-lim-dim0517
```

3. Crie e ative um ambiente virtual:

```bash
python3 -m venv venv
source venv/bin/activate
```

4. Instale as dependências:

```bash
pip install -r requirements.txt
```

### Executar via Console

```bash
python main.py
```

> Em alguns ambientes, pode ser necessário usar `python3 main.py`.

Após a execução, o sistema exibirá um menu no terminal com as opções disponíveis.

### Executar via API REST

```bash
uvicorn api.app:app --reload --port 8080
```

A API ficará disponível em `http://127.0.0.1:8080`. A documentação interativa (Swagger) pode ser acessada em `http://127.0.0.1:8080/docs`.

### Executar os Testes

```bash
pytest tests/ -v
```

### 🐳 Executar via Docker (Produção)

A imagem oficial do sistema é gerada e publicada automaticamente através da nossa esteira de Entrega Contínua (CD). Para baixar e executar o container, certifique-se de ter o Docker instalado e utilize os comandos abaixo:

```bash
docker pull marcusaurelius33/banking-system-lim-dim0517:latest

docker run -d -p 8080:8080 marcusaurelius33/banking-system-lim-dim0517:latest
```
Após a execução, a API conteinerizada responderá em http://127.0.0.1:8080.

🔗 Link Direto para a Imagem: Acessar o repositório no Docker Hub - marcusaurelius33/banking-system-lim-dim0517

---

## 🌐 Endpoints da API

| Método | Rota | Descrição |
|--------|------|-----------|
| `POST` | `/banco/contas/` | Cadastrar nova conta (normal, bônus ou poupança) |
| `GET`  | `/banco/conta/{id}` | Consultar dados da conta |
| `GET`  | `/banco/conta/{id}/saldo` | Consultar saldo da conta |
| `PUT`  | `/banco/conta/{id}/credito` | Realizar crédito na conta |
| `PUT`  | `/banco/conta/{id}/debito` | Realizar débito na conta |
| `PUT`  | `/banco/conta/transferencia` | Realizar transferência entre contas |
| `PUT`  | `/banco/conta/rendimento` | Aplicar rendimento em contas poupança |


## 🧪 Testes Unitários

O projeto utiliza **Pytest** para testes unitários na camada de serviços, sem dependência da API REST.

### Executar os testes

```bash
# Com ambiente virtual ativado
pytest tests/ -v

# Ou diretamente pelo venv
venv/bin/pytest tests/ -v
```

---

## 👥 Integrantes da Equipe

- **Luan Sampaio** - [@luan-sampaio](https://github.com/luan-sampaio)
- **Iruziky Araújo** - [@iruziky](https://github.com/iruziky)
- **Marcus Aurelius** - [@MarcusAurelius33](https://github.com/MarcusAurelius33)

---

