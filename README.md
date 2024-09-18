# Library (lib_name)
***

## Introdução

A library **lib_name** pode ser utilizada com o intuito de melhorar o trabalho do time de automação, minimizando o tempo de manutenção em funções auxiliares, evitando duplicidades e organizando-as em um único repositório.

Além de organizar as funções, a library também pode ser responsável por controlar as dependências do projeto de automação, 
evitando dependências em diferentes versões.\

Sendo assim, havendo a necessidade de criar novas funções para serem utilizadas nos projetos de automação, o responsável deverá entender se faz sentido a utilização em outros projetos, 
incluindo na lib caso faça, assim, todos podem fazer a utilização das mesmas de forma unificada.
***

## Instalação
>A instalação da lib no projeto de automação com Robot Framework poderá ser feita através do pip install.
> 
> [Incluir aqui os links de ajuda, caso tenha](https://github.com/rftrombeta/lib-python-robot-framework)
***

## Links Uteis 
Segue abaixo alguns links importantes para a correta utilização e conhecimento da lib: 

1. [Release Notes](release-notes.md)
2. [Documentação Funcional](documentação-funcional.md)
***

## Comandos uteis para desenvolver na lib

> **Rodar os testes**\
> Após finalizar o desenvolvimento, a execução local para testes poderá ser feita utilizando o exemplo de comando abaixo:
> * python -m src.function_package.my_function.py
>   * Também é possível acrescentar argumentos acrescentando **env:**

> **Buildar projeto para teste**\
> Após finalizar os testes, podemos gerar um pacote da lib para instalação nos demais projetos utilizando o comando 
> ```python -m build```. 
> * Esse comando criará uma pasta chamada **dist** com um arquivo ```tar.gz``` que poderá ser utilizado para instalação no projeto.
> * ```pip install lib_name-1.1.1.tar.gz``` 
***
## Files from Lib
### setup.py
Esse arquivo é o responsável por realizar o controle da lib, como descrição, diretórios, versões e suas dependências.\
Todas as dependências incluídas no setup.py serão instaladas como dependência do projeto de automação no momento em que a lib for instalada.\
Dessa forma, o projeto de automação não precisará de um arquivo ```requirements.txt``` específico.

### packages python
Dentro dos respectivos pacotes, teremos os arquivos python contendo com as respectivas funções. Essas funções poderão ser 
apenas para utilização interna da lib, servindo de apoio para outras funções, ou, serão utilizadas nos projetos de automação,
nesse caso, devendo ser incluídas nos respectivos arquivos de inicialização ```__init__.py```, como demonstrado abaixo:
> from my_function import (function_one)