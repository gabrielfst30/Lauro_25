# Workshop Lauro de Freitas

Bem-vindos ao Workshop de Desenvolvimento! Este guia irá orientá-los através da configuração do ambiente de desenvolvimento e das tarefas práticas do workshop.

## Pré-requisitos e Configuração do Ambiente

### 1. Download e Instalação do VS Code

1. Acesse o site oficial da Microsoft: [https://code.visualstudio.com/](https://code.visualstudio.com/)
2. Clique em "Download" e selecione a versão apropriada para seu sistema operacional
3. Execute o instalador baixado e siga as instruções de instalação (use todas respostas em default)
4. Após a instalação, abra o VS Code

### 2. Download e Instalação do Git

1. Acesse o site oficial do Git: [https://git-scm.com/](https://git-scm.com/)
2. Clique em "Download" e baixe a versão para seu sistema operacional
3. Execute o instalador e siga as instruções de instalação
4. Durante a instalação, mantenha as configurações padrão recomendadas

### 3. Abrir Terminal no VS Code

1. Com o VS Code aberto, acesse o menu superior
2. Vá em **Terminal** → **Novo Terminal** (ou use o atalho `Ctrl + '`)
3. O terminal será aberto na parte inferior da janela do VS Code

### 4. Instalar Python

1. No terminal do VS Code que você acabou de abrir, digite:
   ```bash
   python3
   ```
2. Se o Python não estiver instalado, o Windows irá automaticamente abrir a Microsoft Store
3. Clique em "Instalar" para instalar o Python através da Microsoft Store
4. Após a instalação, feche e reabra o terminal do VS Code
5. Teste a instalação digitando `python --version`

### 5. Instalar Dependências das Bibliotecas

1. No terminal do VS Code que você acabou de abrir, digite:
   ```bash
   pip install -r requirements.txt
   ```

## Tarefas do Workshop

Agora que seu ambiente está configurado, você deve completar as seguintes tarefas:

### Tarefa 1: Escolher o Modelo Apropriado a partir do AI Studio

- Acesse o AI Studio
- Navegue pelos modelos disponíveis
- Selecione o modelo mais adequado para o projeto
- Anote as configurações e parâmetros do modelo escolhido
- Use Google Search como ferramenta do modelo
- Adicione a função em `gemini_chat.py` e configure o retorno de output

### Tarefa 2: Ajustar model_response em app.py

- Abra o arquivo `app.py` no VS Code
- Localize a função ou variável `model_response`
- Ajuste os parâmetros conforme o modelo selecionado na Tarefa 1
- Certifique-se de que a configuração está correta para o modelo escolhido

### Tarefa 3: Ajustar endpoint em index.html

- Abra o arquivo `index.html` no VS Code
- Localize a seção onde o endpoint está definido
- Atualize o endpoint para corresponder às configurações do seu modelo
- Verifique se a URL e os parâmetros estão corretos

## Dicas Importantes

- Sempre salve seus arquivos após fazer alterações (`Ctrl + S`)
- Use o terminal integrado do VS Code para executar comandos
- Se encontrar erros, verifique se todas as dependências foram instaladas corretamente
- Mantenha todos os arquivos organizados no mesmo diretório do projeto

## Suporte

Se você encontrar algum problema durante a configuração ou execução das tarefas, não hesite em pedir ajuda aos instrutores do workshop.

Boa sorte e bom desenvolvimento! 🚀