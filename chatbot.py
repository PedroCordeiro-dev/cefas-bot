import os
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import PyPDFLoader
from youtube_transcript_api import YouTubeTranscriptApi
from dotenv import load_dotenv


load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("Defina a variável de ambiente GROQ_API_KEY.")


chat = ChatGroq(model='openai/gpt-oss-20b')


def resposta_bot(mensagens, documento):

    max_doc = 8000
    prompt = ChatPromptTemplate.from_messages([
        ("system",
         "Seu nome é CefasBot. Você é um assistente virtual amigável. "
         "Use as informações a seguir para formular suas respostas:\n\n{informacoes}"),
        *mensagens
    ])

    chain = prompt | chat
    
    return chain.invoke({'informacoes': documento[:max_doc]}).content

def carrega_site():
    url_site = input('URL do site: ')
    try:
        loader = WebBaseLoader(
            web_path=url_site,
            header_template={"User-Agent": "Mozilla/5.0"})
        lista_documento = loader.load()
    except Exception as e:
        print(f'Erro ao carregar site. {e}')
        return ''

    documento = " ".join(doc.page_content for doc in lista_documento)

    return documento

def carrega_pdf():
    caminho = input('Caminho do PDF: ')
    try:
        loader = PyPDFLoader(caminho)
        lista_documento = loader.load()
    except Exception as e:
        print(f'Erro ao carregar PDF. {e}')
        return ''

    documento = " ".join(doc.page_content for doc in lista_documento)

    return documento

def extract_video_id(url):
    import re
    match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11})", url)
    if match:
        return match.group(1)
    raise ValueError("ID do vídeo não encontrado na URL.")

def carrega_youtube():
    url_youtube = input('URL do vídeo: ')
    documento = ''
    try:
        video_id = extract_video_id(url_youtube)
        yt = YouTubeTranscriptApi()                   # --- Cria instância
        print('Transcrição carregada com sucesso!')

        try:
            transcript_data = yt.fetch(video_id, languages=['pt'])
        except:
            transcript_data = yt.fetch(video_id)
        documento = " ".join([item.text for item in transcript_data])

        if not documento:
            print("Não foi possível obter a transcrição do vídeo (não possui legenda pública disponível).")

    except Exception as e:
        print(f"Erro ao carregar transcrição: {e}")
        documento = ''
    return documento


print('Bem-Vindo(a) ao CefasBot!')

def menu():
    print('==== MENU ====')
    print('1 - Carregar conteúdo de site')
    print('2 - Carregar conteúdo de PDF')
    print('3 - Carregar transcrição de vídeo do YouTube')
    print('0 - Sair')

    opcao = input('Digite sua opção: ')

    if opcao == '0':
        print('Encerrando...')
        return False
    
    if opcao == '1':
        doc = carrega_site()
    elif opcao == '2':
        doc = carrega_pdf()
    elif opcao == '3':
        doc = carrega_youtube()
    else:
        print('Opção inválida.')
        return True
    
    if not doc:
        print("Nenhum conteúdo foi carregado.")
        return True
    
    perguntas = []
    
    while True:
        pergunta = input('CefasBot > (digite "sair" ou "historico"): ').lower()

        if pergunta == 'sair':
            break

        elif pergunta in ['historico', 'histórico']:
            print('\n=== HISTÓRICO ===')
            for tipo, msg in perguntas:
                if tipo == 'user':
                    print(f'Você: {msg}')
                else:
                    print(f'CefasBot: {msg}')
            print('=================\n')
            continue

        perguntas.append(('user', pergunta))

        max_historico = 6
        perguntas = perguntas[-max_historico:]

        print('CefasBot está pensando...')
        resposta = resposta_bot(perguntas, doc)
        perguntas.append(('assistant', resposta))

        print('\nCefasBot:', resposta, '\n')

while True:
    continuar = menu()
    if continuar is False:
        break
