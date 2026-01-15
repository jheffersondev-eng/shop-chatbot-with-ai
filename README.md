# Shop Chatbot with AI 🤖

Um chatbot inteligente especializado em desenvolvimento de software, APIs REST, Laravel, PHP e boas práticas de programação. Utilizando tecnologias de IA avançadas para fornecer respostas contextualizadas e úteis.

**📚 Documentação Interativa:** [Swagger/OpenAPI](https://shop-chatbot-with-ai.onrender.com/docs)

## 📋 Sobre o Projeto

Este projeto é uma API REST que fornece um endpoint de chat alimentado por inteligência artificial. O chatbot foi treinado para ser um assistente especialista em:

- Desenvolvimento de software
- APIs REST
- Laravel e PHP
- Arquitetura MVC
- Clean Code
- Boas práticas de desenvolvimento

A API utiliza autenticação por chave interna (`x-api-key`) para garantir segurança nas requisições.

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Descrição |
|------------|-----------|
| **FastAPI** | Framework web moderno e rápido para construir APIs em Python |
| **Uvicorn** | Servidor ASGI de alto desempenho |
| **Pydantic** | Validação de dados e serialização |
| **FreeFlow LLM** | Cliente para integração com modelos de linguagem |
| **Python 3.8+** | Linguagem de programação |
| **dotenv** | Gerenciamento de variáveis de ambiente |

## 🚀 Como Rodar o Projeto

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Instalação

1. **Clone ou navegue para o diretório do projeto:**
```bash
cd shop-chatbot-with-ai
```

2. **Crie um ambiente virtual (recomendado):**
```bash
python -m venv venv
```

3. **Ative o ambiente virtual:**

- **Windows:**
```bash
venv\Scripts\activate
```

- **macOS/Linux:**
```bash
source venv/bin/activate
```

4. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

5. **Configure as variáveis de ambiente:**

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```env
GEMINI_API_KEY=sua_chave_gemini
GEMINI_MODEL=gemini-1.5-flash
GROQ_API_KEY=sua_chave_groq
INTERNAL_API_KEY=shop-internal-key
```

6. **Inicie o servidor:**
```bash
uvicorn main:app --reload
```

O servidor estará disponível em `http://localhost:8000`

## 📡 Como Usar

### Endpoint: POST /chat

Envie mensagens para o chatbot e receba respostas inteligentes.

**URL:** `https://shop-chatbot-with-ai.onrender.com/chat`

**Headers:**
- `accept: application/json`
- `x-api-key: shop-internal-key` (autenticação)
- `Content-Type: application/json`

**Body:**
```json
{
    "message": "Sua pergunta aqui"
}
```

### Exemplo com cURL

```bash
curl --location 'https://shop-chatbot-with-ai.onrender.com/chat' \
--header 'accept: application/json' \
--header 'x-api-key: shop-internal-key' \
--header 'Content-Type: application/json' \
--data '{
    "message": "Como criar uma API em Laravel?"
}'
```

**Resposta Esperada:**
```json
{
    "reply": "Para criar uma API em Laravel, você pode seguir esses passos..."
}
```

### Exemplo com Python

```python
import requests
import json

url = "https://shop-chatbot-with-ai.onrender.com/chat"

headers = {
    "accept": "application/json",
    "x-api-key": "shop-internal-key",
    "Content-Type": "application/json"
}

data = {
    "message": "Como criar uma API em Laravel?"
}

response = requests.post(url, headers=headers, json=data)
print(response.json())
```

### Exemplo com JavaScript/Fetch

```javascript
const url = 'https://shop-chatbot-with-ai.onrender.com/chat';

const options = {
    method: 'POST',
    headers: {
        'accept': 'application/json',
        'x-api-key': 'shop-internal-key',
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        message: 'Como criar uma API em Laravel?'
    })
};

fetch(url, options)
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('Erro:', error));
```

## 📝 Estrutura do Projeto

```
shop-chatbot-with-ai/
├── main.py              # Arquivo principal da aplicação FastAPI
├── requirements.txt     # Dependências do projeto
├── .env                 # Variáveis de ambiente (não incluir no git)
├── .gitignore          # Arquivos a ignorar no git
├── README.md           # Este arquivo
└── __pycache__/        # Arquivos compilados Python
```

## 🔐 Segurança

- A API requer uma chave de autenticação (`x-api-key`) para cada requisição
- As variáveis sensíveis (chaves de API) devem estar no arquivo `.env`
- Nunca faça commit do arquivo `.env` no repositório
- Certifique-se de adicionar `.env` ao `.gitignore`

## 📚 Documentação Interativa

Quando o servidor estiver rodando localmente, você pode acessar a documentação interativa:

- **Swagger UI:** `http://localhost:8000/docs`
- **ReDoc:** `http://localhost:8000/redoc`

## 🚢 Deploy

Este projeto está deployado em [Render](https://render.com/) e está disponível em:

```
https://shop-chatbot-with-ai.onrender.com
```

## 📄 Licença

Este projeto está sob licença aberta. Sinta-se livre para usar e modificar conforme necessário.

## 👨‍💻 Contribuições

Contribuições são bem-vindas! Se encontrar algum problema ou tiver sugestões, abra uma issue ou pull request.

---

**Desenvolvido com ❤️**