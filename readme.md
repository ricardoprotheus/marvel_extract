# Marvel Heroes - extração

### Propósito
Utilizando o código deste repositório é possível extrair os 
dados de heróis da Marvel e criar um arquivo CSV com o DataFrame gerado.

### Arquivos contidos aqui:

- requirements.txt
- marvel_extract.py
- functions/functions.py

### Como utilizar:

- Criar uma conta no [site para desenvolvedores Marvel](https://developer.marvel.com/) 
  onde irá conseguir uma chave API, que será utilizada para autenticação.
  

- Criar um ambiente virtual e carregar o **requirements.txt**


- Definir suas chaves pública e privada como **variáveis de ambiente**


- Executar **marvel_extract.py** 

Bom, um CSV deve ser gerado ao final destes passos e 
nele você irá encontrar as seguintes colunas:

    columns=['id', 'hero_name', 'description', 'comics_count', 'series_count', 'stories_count', 'events_count']


Quaisquer pontos de melhoria, dúvidas ou elogios, é possível me contactar por aqui ou através do [LinkedIn.](https://www.linkedin.com/in/andrelsjunior/)
