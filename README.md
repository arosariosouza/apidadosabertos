# API Dados Abertos

Documentação de instalação e manutenção do projeto.

## Índice
1. [Arquitetura](#1-arquitetura);
2. [Preparação de ambiente de desenvolvimento](#2-preparação-e-manutenção-do-ambiente-de-desenvolvimento);
    - [2.01. Instalação do Ubuntu no WSL2](#201-instalação-do-ubuntu-no-wsl2);
    - [2.02. Instalação do Visual Studio Code](#202-instalação-do-visual-studio-code);
    - [2.03. Instalação do Docker Desktop no Ubuntu WSL2](#203-instalação-do-docker-desktop-no-ubuntu-wsl2);
    - [2.04. Instalação do Docker Compose no Ubuntu WSL2](#204-instalação-do-docker-compose-no-ubuntu-wsl2);
    - [2.05. Instalação do git no Ubuntu WSL2](#205-instalação-do-git-no-ubuntu-wsl2);
    - [2.06. Obtenção do código-fonte](#206-obtenção-do-código-fonte);
    - [2.07. Preparação do ambiente python](#207-preparação-do-ambiente-python);
    - [2.08. Arquivos e diretórios do projeto](#208-arquivos-e-diretórios-do-projeto);
    - [2.09. Criação de views na base de dados](#209-criação-de-views-na-base-de-dados);
    - [2.10. Criação de variáveis de ambiente em desenvolvimento](#210-criação-de-variáveis-de-ambiente-em-desenvolvimento);
    - [2.11. Execução do projeto a partir do código-fonte](#211-execução-do-projeto-a-partir-do-código-fonte);
    - [2.12. Criando imagem Docker do projeto](#212-criando-imagem-docker-do-projeto);
    - [2.13. Criação de variáveis de ambiente para container Docker em desenvolvimento](#213-criação-de-variáveis-de-ambiente-para-container-docker-em-desenvolvimento);
    - [2.14. Execução do projeto a partir de imagem Docker utilizando Docker Compose](#214-execução-do-projeto-a-partir-de-imagem-docker-utilizando-docker-compose);
    - [2.15. Envio de imagem docker do projeto ao Docker Hub](#215-envio-de-imagem-docker-do-projeto-ao-docker-hub);
    - [2.16. Configuração do swagger](#216-configuração-do-swagger);
    - [2.17. Customização de home page do swagger](#217-customização-de-home-page-do-swagger);
3. [Disponilização de nova versão de homologação](#3-disponilização-de-nova-versão-de-homologação);
    - [3.01. Instalação do Docker no servidor de homologação Ubuntu](#);
    - [3.02. Instalação do Docker Compose no servidor de homologação Ubuntu](#);
    - [3.03. Obtenção de imagem docker do projeto a partir do Docker Hub](#);
    - [3.04. Execução do projeto a partir de imagem Docker utilizando Docker Compose](#);
4. [Disponilização de nova versão de produção](#4-disponilização-de-nova-versão-de-produção).
    - [4.01. Instalação do Docker no servidor de homologação Ubuntu](#)
    - [4.02. Instalação do Docker Compose no servidor de homologação Ubuntu](#)
    - [4.03. Envio de arquivo de imagem Docker do projeto em homologação para ambiente de produção](#)
    - [4.04. Instalação de arquivo de imagem Docker do projeto no ambiente de produção](#)


## 1. Arquitetura
* ### Ambiente de Desenvolvimento
    ![Arquitetura de Ambiente de Desenvolvimento](doc/images/ambiente-desenvolvimento.png)

* ### Ambiente de Homologação
    ![Arquitetura de Ambiente de Homologação](doc/images/ambiente-homologacao.png)

* ### Ambiente de Produção
    ![Arquitetura de Ambiente de Produção](doc/images/ambiente-producao.png)

## 2. Preparação e manutenção do ambiente de desenvolvimento

Nos passos de preparação do ambiente de desenvolvimento será contemplado somente a utilização do Sistema Operacional Windows 10 ou superior e também Linux Ubuntu executando sob o WSL (Windows Subsystem for Linux)

* ### 2.01. Instalação do Ubuntu no WSL2
    As informações de como instalar o Ubuntu no WSL estão presentes na página [Instalar o WSL](https://docs.microsoft.com/pt-br/windows/wsl/install)

* ### 2.02. Instalação do Visual Studio Code
    O Visual Studio Code está disponível na página [Download Visual Studio Code](https://code.visualstudio.com/download)

* ### 2.03. Instalação do Docker Desktop no Ubuntu WSL2
    O Docker Desktop está disponível na página [Docker Desktop](https://www.docker.com/products/docker-desktop/)

    **Dica:** Após a instalação inclua o usuário de trabalho no grupo docker para evitar o uso do comando sudo quando utilizar o docker cli
    ```
    $ sudo usermod -a -G docker allan
    ```

* ### 2.04. Instalação do Docker Compose no Ubuntu WSL2
    As informações de como instalar o Docker Compose estão presentes na página [Install Docker Compose CLI Plugin](https://docs.docker.com/compose/install/compose-plugin/#installing-compose-on-linux-systems)

* ### 2.05. Instalação do git e curl no Ubuntu WSL2
    No terminal do Ubuntu instalado sob WSL execute o comando:
    ```
    $ sudo apt install git curl
    ```

* ### 2.06. Obtenção do código-fonte
    No terminal do Ubuntu instalado sob WSL execute os comandos:
    ```
    $ cd ~
    $ git clone https://github.com/arosariosouza/apidadosabertos.git
    ```
    **Obs.:** Será necessário solicitar permissão de acesso ao desenvolvedor para obter o código-fonte.

* ### 2.07. Preparação do ambiente Python
    * a. Verificar a versão do Python utilizada no projeto:
        ```
        $ cd /home/allan/apidadosabertos/
        $ cat runtime.txt
        python-3.10.0
        ```

    * b. Instalar dependências do [Pyenv](https://github.com/pyenv/pyenv)
        ```
        $ sudo apt-get update; sudo apt-get install make build-essential libssl-dev zlib1g-dev \
        libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
        libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
        ```

    * c. Instalar o [Pyenv](https://github.com/pyenv/pyenv) para gerenciar novas versões de Python independentes do sistema operacional Ubuntu;
        ```
        $ curl https://pyenv.run | bash        
        ```

    * d. Adicionar as seguintes linhas no final do arquivo ~/.bashrc:    
        ```
        export PYENV_ROOT="$HOME/.pyenv"
        command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
        eval "$(pyenv init -)"
        eval "$(pyenv virtualenv-init -)"
        ```

    * e. Instalar versão python utilizada no projeto no Pyenv e ativar a utilização
        ```
        $ pyenv install 3.10.0
        $ pyenv global 3.10.0
        ```

    * f. Verificar versão instalada:
        ```
        $ python -V
        Python 3.10.0
        $ which python
        /home/allan/.pyenv/shims/python
        ```
    * g. Criar ambiente virtual Python e ativar utilização
        ```
        $ cd /home/allan/apidadosabertos/
        python -m venv .venv
        source .venv/bin/activate
        ```
    * h. Instalar bibliotecas do projeto (executar com o virtual env ativado)
        ```
        (.venv) $ pip install -r requirements.txt
        ```

* ### 2.08. Principais arquivos e diretórios do projeto
    * Diretórios:
        * **doc/** - documentação do projeto com a arquitetura;
        * **models/** - representação de modelo das tabelas/views acessadas pela API;
        * **resources/** - implementação dos endpoints da API;
        * **static/** - configuração da interface Swagger;
        * **swagger-ui/** - customização da aparência da interface Swagger, adicionando cabeçalho e rodapé à página;
        * **templates/** - template com a página principal do projeto que apenas redireciona para página do Swagger;
        * **views/** - views que devem ser criadas na base de dados onde estão presentes os dados que serão disponibilizados pela API;

    * Arquivos:
        * **apidadosabertos.conf** - arquivo de configuração do apache para ativar proxy reverso e redirecionar as requisições para serviço da API;
        * **app.py** - script python principal responsável pelo start do serviço;
        * **docker-compose.yml** - arquivo de configuração do docker compose para iniciar o container do serviço com as configurações necessárias;
        * **Dockerfile** - script docker para criação de imagem do serviço
        * **helpers.py** - script python com função para converter a saída da API para do formato json para CSV;
        * **README.md** - Documentação de instalação e manutenção do projeto;
        * **requirements.txt** - lista de bibliotecas python que devem ser instaladas para que o serviço funcione;
        * **runtime.txt** - arquito com versão do python utilizada no desenvolvimento, homologação e produção;
        * **sql_alchemy.py** - script python que instância SQL Alchemy para mapeamento objeto/relacional das tabelas do banco de dados;
        * **wsgi.py** - script python para iniciar serviço da API em ambiente de homologação e produção.

* ### 2.09. Criação de views na base de dados
    No diretório view/*.sql existem views que deve ser criadas nos ambientes de desenvolvimento, homologação e produção.

* ### 2.10. Criação de variáveis de ambiente em desenvolvimento
    No diretório raiz do projeto, crie o arquivo `.env` com o seguinte conteúdo:
    ```
    DEBUG=True
    HOST=0.0.0.0

    SQLALCHEMY_DATABASE_USER=postgres
    SQLALCHEMY_DATABASE_PASSWORD=postgres
    SQLALCHEMY_DATABASE_SERVER=localhost
    SQLALCHEMY_DATABASE_PORT=5432
    SQLALCHEMY_DATABASE_DATABASE=dbdemas

    SQLALCHEMY_TRACK_MODIFICATIONS=False
    ```
    **Obs.:** As credenciais de acesso à base de dados devem ser ajustadas de acordo banco de dados utilizado.

* ### 2.11. Execução do projeto a partir do código-fonte
    A partir do diretório raiz do projeto execute:
    ```
    $ source .venv/bin/activate
    (.venv) $ python app.py
    ```
* ### 2.12. Criando imagem Docker do projeto
    Exemplo de criação de imagem docker para determinada versão:
    ```
    $ docker build -t allansouza/apidadosabertos:1.3.2 .
    ```
* ### 2.13. Criação de variáveis de ambiente para executar container Docker em desenvolvimento usando docker compose
    No diretório raiz do projeto, crie o arquivo `variables.env` com o seguinte conteúdo:
    ```
    SQLALCHEMY_DATABASE_USER=postgres
    SQLALCHEMY_DATABASE_PASSWORD=postgres
    SQLALCHEMY_DATABASE_SERVER=192.168.0.6
    SQLALCHEMY_DATABASE_PORT=5432
    SQLALCHEMY_DATABASE_DATABASE=dbdemas
    ```
    **Obs.:** As credenciais de acesso à base de dados devem ser ajustadas de acordo banco de dados utilizado.

* ### 2.14. Execução do projeto a partir de imagem Docker utilizando Docker Compose
    No diretório raiz do projeto, execute o comando abaixo:
    ```
    $ docker-compose up -d
    ```
    Este comando irá utilizar configurações ajustadas no arquivo `docker-compose.yml` como: **imagem docker**, **variáveis de ambiente**, **porta** etc.

* ### 2.15. Envio de imagem docker do projeto ao Docker Hub
    No diretório raiz do projeto, execute os comandos abaixo:
    
    * a. Caso ainda não esteja logado no [hub.docker.com](https://hub.docker.com) e forneça as devidas credenciais:
        ```
        $ docker login
        ```
    * b. Upload de imagem para o [hub.docker.com](https://hub.docker.com)
        ```
        docker push allansouza/apidadosabertos:1.3.2
        ```

* ### 2.16. Configuração do swagger
    Para gerenciar os endpoints presentes na interface do Swagger edite o arquivo ``static/swagger.json``.

* ### 2.17. Customização de home page do swagger
    Para customizar a aparência do cabeçalho e rodapé da home page do Swagger, edite o arquivo `swagger-ui/index.template.html`. 

## 3. Disponilização de nova versão de homologação
Acesse via SSH o servidor *10.1.3.115* .

* ### 3.01. Instalação do Docker no servidor de homologação Ubuntu
    As informações de instalação do Docker no Ubuntu estão disponíveis na página [Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/)

    **Dica:** Após a instalação inclua o usuário de trabalho no grupo docker para evitar o uso do comando sudo quando utilizar o docker cli
    ```
    $ sudo usermod -a -G docker allan
    ```

* ### 3.02. Instalação do Docker Compose no servidor de homologação Ubuntu
    As informações de como instalar o Docker Compose estão presentes na página [Install Docker Compose CLI Plugin](https://docs.docker.com/compose/install/compose-plugin/#installing-compose-on-linux-systems)

* ### 3.03. Obtenção de imagem docker do projeto a partir do Docker Hub
    No terminal do servidor de homologação, execute os comandos:
    * a. Caso ainda não esteja logado no [hub.docker.com](https://hub.docker.com) e forneça as devidas credenciais:
        ```
        $ docker login
        ```
    * b. Download da image docker:
        ```
        docker pull allansouza/apidadosabertos:1.3.2
        ```

* ### 3.04. Execução do projeto a partir de imagem Docker utilizando Docker Compose
    * a. Crie o diretório apidadosabertos
        ```
        $ mkdir ~/apidadosabertos
        ```
    * b. Copie os arquivos docker-compose.yml e variables.env do ambiente de desenvolvimwento para o diretório `~/apidadosabertos` recém criado em homologação. Ajuste o esses arquivos com a versão correta da **imagem docker**, **credenciais de acesso ao banco** etc.
    * c. Acesse o diretório recém criado, e execute o comando:
        ```
        $ mkdir ~/apidadosabertos
        $ docker-compose up -d
        ```
    **IMPORTANTE:** *Toda vez que um novo container for iniciado, os passaos abaixo devem ser executados*.

    * d. Existe uma restrição de segurança no acesso ao banco de dados PostgreSQL utilizado no servidor de homologação. Por isso devemos obter o IP (valor de **IPAddress** presente na saída do comando abaixo) utilizado pelo container do serviço e dar permissão de acesso no arquivo de configuração `pg_hba.conf`

        ```
        $ docker inspect apidadosabertos
        ```
        ```json
        "Networks": {
            "apidadosabertos_default": {
                "IPAMConfig": null,
                "Links": null,
                "Aliases": [
                    "web",
                    "736c19fde1a3"
                ],
                "NetworkID": "df7b4fd2eb0e2db3214be5ba03f197",
                "EndpointID": "6e591bd31da9e248e85492c712fed",
                "Gateway": "172.24.0.1",
                "IPAddress": "172.24.0.2",
                "IPPrefixLen": 16,
                "IPv6Gateway": "",
                "GlobalIPv6Address": "",
                "GlobalIPv6PrefixLen": 0,
                "MacAddress": "02:42:ac:18:00:02",
                "DriverOpts": null
            }
        }
        ```
    * e. Inclua o IP (Valor de **IPAddress**) na configuração para PostgreSQL:
        ```
        $ sudo vim /etc/postgresql/13/main/pg_hba.conf
        ```
        ```
        host    all             all             172.24.0.2/16           md5
        ```

## 4. Disponilização de nova versão de produção
* ### 4.01. Instalação do Docker no servidor de produção RedHat Enterprise Linux
    **Esta tarefa é executada somente pela equipe suporte do DataSUS.**

* ### 4.02. Instalação do Docker Compose no servidor de produção RedHat Enterprise Linux
    **Esta tarefa é executada somente pela equipe suporte do DataSUS.**

* ### 4.03. Envio de arquivo de imagem Docker do projeto em homologação para ambiente de produção
    * a. No servidor de homologação (IP: *10.1.3.115*), faça backup da imagem já instalada.
        ```
        $ docker save -o /tmp/allansouza_apidadosabertos_1.3.2.tar allansouza/apidadosabertos:1.3.2
        ```
    
    * b. No servidor de produção (IP: *172.29.0.249*), crie o diretório apidadosabertos.

        * Acessar servidor de produção via SSH a partir do servidor de homologação
            ```
            $ ssh -C -p 37259 demas@172.29.0.249
            ```
        * Criar diretório
            ```
            $ mkdir /home/demas/apidadosabertos
            ```

    * c. No servidor de homologação (IP: *10.1.3.115*), envie o backup da imagem para o servidor de produção (IP: *172.29.0.249*).
        ```
        $ scp -P 37259 /tmp/allansouza_apidadosabertos_1.3.2.tar demas@172.29.0.249:/home/demas/apidadosabertos/
        ```

* ### 4.04. Instalação e execução de imagem Docker do projeto no ambiente de produção
    **IMPORTANTE**: *Se já tiver uma versão antiga do container em execução, este deve ser removido antes de executar esses passos*.

    * a. Copie os arquivos arquivos `docker-compose.yml` e `variables.env` para o servidor de produção no diretório `/home/demas/apidadosabertos`. Configure-os adequadamente as informações de **versão da imagem docker**, **credenciais de acesso ao banco** etc.

    * b. No servidor de produção, instale a imagem docker do serviço baixada
        ```
        $ cd /home/demas/apidadosabertos/
        $ sudo docker load -i allansouza_apidadosabertos_1.3.2.tar
        $ docker-compose up -d
        ```

**Desenvolvedor**: Allan Souza <allan.carloss@gmail.com>