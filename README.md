# 🤖 CefasBot

O **CefasBot** é um chatbot interativo desenvolvido em Python que responde perguntas com base em conteúdos fornecidos pelo usuário, conteúdos de:

* 🌐 Sites
* 📄 Arquivos PDF
* 🎥 Vídeos do YouTube (via transcrição)

Ele utiliza modelos de linguagem (LLMs) para interpretar e gerar respostas inteligentes com base no conteúdo carregado.

---

## 🚀 Tecnologias utilizadas

* Python
* LangChain
* Groq API
* YouTube Transcript API

---

## 📦 Funcionalidades

* Carregar conteúdo de um site via URL
* Ler e interpretar arquivos PDF
* Extrair e usar transcrição de vídeos do YouTube
* Chat interativo com histórico de conversa
* Comando para visualizar histórico
* Sistema de menu no terminal

---

## 🛠️ Como usar

### 1. Clone o repositório

```bash
git clone https://github.com/PedroCordeiro-dev/cefas-bot.git
cd cefasbot
```

---

### 2. Crie o arquivo `.env`

Crie um arquivo chamado `.env` na raiz do projeto e adicione:

```env
GROQ_API_KEY=sua_chave_aqui
```

---

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

---

### 4. Execute o projeto

```bash
python chatbot.py
```

---

## 💬 Comandos disponíveis no chat

Durante a conversa com o bot:

* `historico` → mostra o histórico da conversa
* `sair` → encerra o chat atual

---

## 👨‍💻 Autor

Desenvolvido por **Pedro Cordeiro** 👾
Projeto para aprendizado e portfólio.
