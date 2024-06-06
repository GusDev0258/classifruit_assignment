# INSTRUÇÕES PARA O USO DO TRABALHO ENTREGA 2

## Dependências do projeto

- Possuir Python3 e PIP instalado
- Possuir NodeJS e NPM instalado

---

## Instruções claras de como instalar cada um das dependências

### UNIX SYSTEMS

#### Python3

Para instalar o python3 em um UNIX system DEBIAN based, caso não tenha vindo instalado ( acho improvável), abra seu terminal e digite
`sudo apt update`
`sudo apt install python3`
`sudo apt install python3-pip`

#### NodeJS

O NodeJS é importante para rodar o front-end, e o NPM é o seu gerenciador de pacotes para instalar abra seu terminal e digite
`sudo apt update`
`sudo apt install nodejs`
`sudo apt install npm`

---

### WINDOWS

#### Python3

Para instalar o python3 em um Windows, acesse https://www.python.org/downloads/ e baixe a versão mais recente

#### NodeJS

Para instalar o NodeJS e o NPM em um Windows, acesse https://nodejs.org/en e baixe a versão do NodeJS LTS

---

## Instruções claras de como rodar o projeto

### UNIX SYSTEMS

Dentro do diretório entrega_2 no seu terminal para rodar os scripts de modelo e api backend realize os seguintes passos:

- `python -m venv`
- `source .venv/Scrips/activate`
- `pip install -r requirements.txt`
  Assim, é para ter ativado o ambiente virtual do python que foi criado para o projeto e instalar as dependências.
  Do contrário, caso não queira usar o venv, só de um `pip install -r requirements.txt`
  Dessa forma você instalou as dependências do projeto e pode roda-lo.

### WINDOWS

Dentro do diretório entrega_2 abra seu terminal e digite:

- `python -m venv`
- ` .venv/Scrips/activate` <- Note a importância do espaço no início, do contrário não irá funcionar.
  Do contrário as instruções para instalar as dependências do projeto são as mesmas do UNIX SYSTEMS, já que é só ter o python3 e o pip instalado.
- `pip install -r requirements.txt`

---

A partir daqui os comandos para rodar os projetos, etc. São os mesmos tanto para WINDOWS quanto para UNIX

OBS: Utilize o powershell do windows para utilizar os mesmos comandos do UNIX no windows.

---

## RODANDO A API BACKEND

`cd api`

`python app.py`

## TREINAR MODELOS

`cd modelo`

> - Modelo ResNet `python train_resnet_model.py`

> - Modelo EfficientNet `python train_effnet_model.py`

## TESTAR MODELOS

`cd modelo`

> - `python test_models.py`

## RODANDO FRONT-END

`cd frontend`

`npm install`

`npm run dev`

---

## O FRONTEND ESTÁ LOCALIZADO NA URL: http://localhost:3000

## O BACKEND ESTÁ LOCALIZADO NA URL: http://localhost:5000 COM O ENDPOINT /predict
