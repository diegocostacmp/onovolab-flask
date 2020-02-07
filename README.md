# API Clima Tempo

Experiência com um crud usando flask e suas ferramentas

- Flask
- flask_sqlalchemy
- flask_migrate
- flask_marshmallow
- marshmallow_sqlalchemy

## Início - Descrição e Pré-Requisitos

# Pré-requisitos
* O teste deve ser escrito em linguagem Python 3;
* Utilizar o framework Flask(As demais bibliotecas e frameworks utilizados para resolução do problema são de livre escolha do candidato.);
* Executar o sistema em ambiente local;
* Banco de dados SQLite.
* Presença do requirements.txt para instalação de dependências
  
## Diferenciais
* Boas práticas de programação (seguir as convenções das linguagens e paradigmas utilizados).
* Cobertura de testes unitários
* Dockerfile que simplifique a execução do teste

## Contexto

* Implementar um webservice que utilize um serviço de previsão do tempo (http://apiadvisor.climatempo.com.br/doc/index.html#api-Forecast-Forecast15DaysByCity), e persista os dados no banco de dados relacional (SQLite). O backend deve fornecer ainda uma interface para consumo externo (API RESTful).


## Instalando o projeto e dependências
A seguir um passo a passo para a instalação do sistema e suas dependências

* clone o projeto:
```
git clone https://github.com/diegocostacmp/onovolab-flask
```
* Certifique-se de que o Python e o Ambiente Virtual (venv) estejam instalados.
Crie o ambiente virtual e instale os pacotes.
 ```
 cd e-quest
 virtualenv venv
 source venv/bin/activate (Windows: venv\Scripts\activate)
 pip install -r requirements.txt
```
## Como rodar esse projeto

```./start.sh(talvez seja necessário dar permissão de execução: chmod +x start.sh )
```

## Como fazer as migrações

```sh
flask db init
flask db migrate
flask db upgrade
```


## Como rodar os endpoints

```
# enpoint que busca a cidade e grava suas informações no banco de dados sqlite
Exemplo: http://127.0.0.1:5000/cidade/3477
# Endpoint que mostra cidade com maior temperatura maxima e media de precipitação por cidade
# O formato de data esperado é 00-0000, indicado respectivamente: dia-mes-ano
    Exemplo: http://127.0.0.1:5000/analise/06-02-2020/7-02-2020/
```
## Construido com

* [Python](https://www.python.org/) - Linguagem de programação
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - Micro-Framework Python


## Autores

* **Diego B B Costa** - *Trabalho inicial* - [Ver...****](https://github.com/diegocostacmp)
* **Ricardo Oliveira** - *Trabalho inicial* - [Ver...](https://github.com/ricardoflayer)

## Licenca

This project is licensed under the MIT License.