# Avaliação Módulo 2 - Let's Code - Ciência de Dados

## Sobre o Projeto

Foram utilizados dados do `World Happiness Report`.

Fontes:

https://www.kaggle.com/mathurinache/world-happiness-report?select=2020.csv

https://www.kaggle.com/ajaypalsinghlo/world-happiness-report-2021?select=world-happiness-report-2021.csv


Juntou-se as bases de dados dos anos 2019, 2020 e 2021 para ter uma conjunto de dados mais completo.


## Etapas para rodar o projeto (Linux)

1 - Clonar repositório

```
git clone https://github.com/Akaori/avaliacao_modulo_2.git
```

2 - Mudar para diretório do projeto

```
cd avaliacao_modulo_2
```

3 - Criar ambiente virtual

```
virtualenv env
```

4 - Ativar ambiente virtual

```
source env/bin/activate
```

5 - Instalar bibliotecas

```
pip install -r requirements.txt
```

6 - Rodar API

```
python api_happiness.py
```

7 - Testar API

Abrir uma  janela no browser e digitar o seguinte endereço:

```
http://localhost:5000/happiness
```
