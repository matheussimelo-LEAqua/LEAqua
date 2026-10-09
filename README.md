LEAqua

Bem-vindo ao repositório do LEAqua, um projeto desenvolvido utilizando o framework Django para o PIBITI.

💬 Um recado para o(a) próximo(a) dev:

"Olá! Que bom que você vai assumir este projeto. Queria deixar um aviso amigável: construí este site bem no começo da minha jornada na programação e utilizei bastante o apoio de IAs generativas para fazer as coisas funcionarem. Por conta disso, é muito provável que você encontre alguns bugs, trechos de código que poderiam ser mais otimizados ou até algumas 'gambiarras'. Sinta-se totalmente livre para refatorar, apagar e melhorar o que achar necessário. Boa sorte e bom trabalho! 🚀"

Este guia foi feito para ajudar você a configurar o ambiente de desenvolvimento local de forma rápida e sem complicações.

📋 Pré-requisitos

Antes de começar, certifique-se de ter as seguintes ferramentas instaladas na sua máquina:

Python (versão 3.x recomendada)

Git (para clonar o repositório)

🚀 Passo a Passo para Instalação e Configuração

Siga as instruções abaixo para rodar o projeto localmente:

1. Clonar o repositório

Abra o seu terminal (Prompt de Comando, PowerShell ou terminal do Linux/macOS) e rode o comando abaixo para baixar o código para a sua máquina:

git clone https://github.com/matheussimelo-LEAqua/LEAqua.git


Em seguida, entre na pasta do projeto:

cd LEAqua


2. Criar o Ambiente Virtual (venv)

O ambiente virtual isola as bibliotecas deste projeto para que elas não entrem em conflito com outros projetos Python no seu computador. Para criá-lo, digite:

python -m venv venv


(Isso criará uma pasta chamada venv dentro do projeto, que não deve ser enviada para o GitHub).

3. Ativar o Ambiente Virtual

Sempre que for trabalhar no projeto, você precisará ativar o ambiente virtual. O comando varia dependendo do seu sistema operacional:

No Windows (Prompt de Comando / PowerShell):

venv\Scripts\activate


No Linux ou macOS:

source venv/bin/activate


Dica: Você saberá que deu certo quando o nome (venv) aparecer no início da linha de comando do seu terminal.

4. Instalar as Dependências

Com o ambiente virtual ativado, instale todas as bibliotecas que o projeto precisa (como o próprio Django) a partir do arquivo de requisitos:

pip install -r requirements.txt


5. Rodar as Migrações do Banco de Dados

Para criar as tabelas necessárias no banco de dados SQLite padrão do projeto, execute:

python manage.py migrate


6. Iniciar o Servidor de Desenvolvimento

Agora está tudo pronto! Para rodar o site no seu computador, digite:

python manage.py runserver


Abra o seu navegador de internet e acesse: http://127.0.0.1:8000/ ou http://localhost:8000/

🛠️ Dicas Úteis

Se você fechar o terminal e for programar no dia seguinte, não se esqueça de entrar na pasta do projeto e rodar o comando de Ativar o Ambiente Virtual (Passo 3) antes de rodar o servidor.

Se você instalar alguma biblioteca nova enquanto programa, lembre-se de atualizar o arquivo de dependências rodando: pip freeze > requirements.txt.
