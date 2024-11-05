# Inteli - Instituto de Tecnologia e Liderança 

<p align="center">
<a href= "https://www.inteli.edu.br/"><img src="assets/inteli.png" alt="Inteli - Instituto de Tecnologia e Liderança" border="0"></a>
</p>

# Previgol

## Elementar

## :student: Integrantes: 
- <a href="https://www.linkedin.com/in/bruno-jancso-fabiani-0272532b3/">Bruno Jancsó Fabiani </a>
- <a href="https://www.linkedin.com/in/danielaraujogon%C3%A7alves/">Daniel Augusto de Araújo Gonçalves </a>
- <a href="https://www.linkedin.com/in/davi-basa/">Davi Basã Henrique Alves </a>
- <a href="https://www.linkedin.com/in/fernando-soares-oliveira/">Fernando Soares de Oliveira </a>
- <a href="https://www.linkedin.com/in/giovanna-britto/">Giovanna Fátima de Britto Vieira </a>
- <a href="https://www.linkedin.com/in/gucolombini/">Gustavo Colombini </a>
- <a href="https://www.linkedin.com/in/rafael-furtado-b30715265/">Rafael Furtado Victor dos Santos </a>

## :teacher: Professores:
### Orientador(a) 
- <a href="https://www.linkedin.com/in/fabiana-martins-de-oliveira-8993b0b2/">Fabiana Martins de Oliveira</a>
### Instrutores
- <a href="https://www.linkedin.com/in/bruna-mayer/">Bruna Mayer</a>
- <a href="https://www.linkedin.com/in/cristiano-benites-ph-d-687647a8/">Cristiano da Silva Benites</a> 
- <a href="https://www.linkedin.com/in/egondaxbacher/">Egon Daxbacher</a> 
- <a href="https://www.linkedin.com/in/henrique-mohallem-paiva-6854b460/">Henrique Mohallem Paiva</a>
- <a href="https://www.linkedin.com/in/michele-bazana-de-souza-69b77763/">Michele Bazana de Souza</a> 


## 📝 Descrição

O presente projeto tem como tema central o desenvolvimento de um modelo preditivo para a International Business Machine Corp (IBM), com o objetivo de desenvolver um modelo para prever o resultado de partidas de futebol e gerar dados e estatísticas para auxiliar em análises estratégicas, decisões comerciais e para apoiar o desempenho dos jogadores.

Dessa forma, considerando a necessidade dos técnicos e patrocinadores de possuir informações mais qualificadas para auxiliar nas suas resoluções, surge a demanda de uma ferramenta para prever os resultados de partidas e fornecer informações para criar estratégias de jogos e para apoiar decisões comerciais. Portanto, esse projeto se estabelece com o objetivo de atender essa necessidade por meio do desenvolvimento de um modelo preditivo treinado com dados históricos de partidas de futebol.

Sendo assim, a solução desenvolvida consiste em uma aplicação web para a visualização dos resultados dos três modelos treinados. Sendo que, o primeiro modelo visa prever o resultado do **ganhador de uma partida**, utilizando o Random Forest, enquanto o segundo modelo visa prever o **placar de uma partida** também utilizando o Random Forest. Por fim, o terceiro modelo visa prever **qual jogador fará o primeiro gol** utilizando o XGBoost. 

Logo, para visualizar os notebooks desenvolvidos é preciso acessar o primeiro link disponibilizado abaixo. Enquanto para acessar a aplicação é necessário acessar o segundo link.   

<b>Link para Vídeo Demonstrativo:</b> <a href="https://inteli.edu.br">Vídeo</a>

<b>Link para a Aplicação Web</b> <a href="https://inteli.edu.br">Aplicação</a>

## 📁 Estrutura de pastas

Dentre os arquivos presentes na raiz do projeto, definem-se:

- <b>readme.md</b>: arquivo que serve como guia e explicação geral sobre o projeto (o mesmo que você está lendo agora).

- <b>assets</b>: todas as imagens e mídias utilizadas nos notebooks e documentação são posicionadas aqui.

- <b>documents</b>: aqui estarão todos os documentos do projeto. Há também uma pasta denominada <b>extras</b> onde estão presentes documentos complementares.

- **front**: esta pasta contém todo o código referente à interface de usuário e exibição do projeto.
    - **.streamlit**: contém as configurações e arquivos de suporte necessários para o funcionamento do Streamlit, a ferramenta utilizada para desenvolver a interface web.
    - **static**: responsável por armazenar arquivos estáticos como folhas de estilo (CSS), imagens e outros elementos utilizados no frontend.
    - **templates**: onde estão armazenados os templates HTML utilizados na renderização das páginas do frontend, servindo de base para a estrutura visual do aplicativo.

- **notebooks**: pasta que centraliza todos os Jupyter Notebooks desenvolvidos durante o projeto, organizados por categorias.
    - **EDA**: contém os notebooks utilizados para a análise exploratória dos dados e para o pré-processamento, onde foram feitas investigações iniciais e o tratamento dos dados.
    - **compare models**: contém os notebooks dedicados à comparação de diferentes modelos preditivos, incluindo experimentos e ajustes de parâmetros para avaliar a performance de cada modelo.
    - **final models**: armazena os notebooks finais com os modelos preditivos que apresentaram os melhores resultados e que foram selecionados para uso na fase de produção.

## 💻 Execução dos projetos

Há duas formas principais de executar os notebooks deste projeto: utilizando o [Jupyter Notebook](https://jupyter.org/) ou o [Google Colab](https://colab.research.google.com/).

#### 1.1.1. Execução via Jupyter Notebook

**1. Verifique a versão do Python:**  
Certifique-se de que a versão 3.10 do Python está instalada.

**1.1. Comando para verificar a versão:**
```
python --version
```

**1.2. Instalação das Bibliotecas Necessárias:**  
Cada notebook pode exigir bibliotecas específicas, então é importante verificar o cabeçalho de cada um para instalar os pacotes corretos. Aqui estão algumas bibliotecas comuns utilizadas nos notebooks deste projeto:
```
pip install pandas matplotlib seaborn openpyxl import-ipynb
```

**2. Execução dos Notebooks:**
1. Abra o Jupyter Notebook:
    ```
    jupyter notebook
    ```
2. Navegue até o notebook desejado (por exemplo, `pre_processing.ipynb`, `data_exploration.ipynb`, ou `main.ipynb`) e execute célula por célula.

#### 1.1.2. Execução via Google Colab

**1. Upload dos Arquivos:**
- Faça o upload dos notebooks e datasets necessários no Google Colab.

**2. Instalação das Bibliotecas:**  
Na primeira célula do Colab, instale as bibliotecas necessárias:
```
!pip install pandas matplotlib seaborn openpyxl import-ipynb
```

**3. Execução dos Notebooks:**  
Navegue até o notebook que deseja executar e rode célula por célula.

**4. Importante:**
Se o utilizador não salvar uma cópia do notebook no seu Google Drive, as alterações realizadas não serão salvas. Para garantir que você mantenha o progresso:

1. Vá até o menu Arquivo (File).
2. lique em Salvar uma cópia no Drive. Isso criará uma cópia do notebook no seu Google Drive pessoal, permitindo que você salve todas as modificações feitas durante a execução.

#### 1.1.3. Download dos Datasets

Para executar os notebooks corretamente, baixe os datasets no seguinte [link](https://drive.google.com/drive/folders/1F_FVjAKfDFCbjb2CBesHeuoV4ZP0tvLG?usp=sharing). Certifique-se de mover os arquivos baixados para a pasta adequada antes de executar os notebooks.

### 1.1.4. Erros Comuns
- **Erro de Importação**: Verifique se todas as bibliotecas necessárias estão instaladas.
- **Erro de Caminho de Arquivo**: Certifique-se de que os arquivos CSV estão no diretório correto.

Caso os erros persistam, você pode procurar ajuda em plataformas como o [Google](https://www.google.com.br/?hl=pt-BR) ou [ChatGPT](https://chatgpt.com/).

Além disso, há a possibilidade de visualizar os resultados de cada modelo por meio da aplicação desenvolvida, sendo assim para executá-la basta seguir os passos abaixo.

### 1.2. Como Rodar o Front

**1. Acesse a pasta `front`:**
```
cd front
```

**2. Execute o Streamlit:**
```
streamlit run dash.py
```

**3. Abra um novo terminal e acesse novamente a pasta `front`:**
```
cd front
```

**4. Execute a aplicação backend:**
```
python app.py
```

**5. Acesse o link gerado:**  
Após a execução dos comandos acima, será gerado um link no terminal que permitirá acessar a interface do projeto.


## 🗃 Histórico de lançamentos

* 1.0.0 - 11/10/2024
    * [sprint 5] Lançamento da primeira versão do modelo preditivo com documentação.
* 0.6.0 - 27/09/2024
    * [sprint 4] Comparação de modelos preditivos
* 0.3.1 - 13/09/2024
    * [sprint 3] Preparação de dados e modelo preditivo preliminar
* 0.2.7 - 30/08/2024
    * [sprint 2] Análise exploratória e levantamento de hipóteses
* 0.1.3 - 16/08/2024
    * [sprint 1] Documentação de entendimento do negócio

## 📋 Licença/License

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.dev/Intelihub/Template_M3">Esti-Match</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://www.inteli.edu.br/">Inteli</a>, <a href="https://github.com/BrunoFabiani">Bruno Jancsó Fabiani<a>, <a href="https://github.com/odanielaugusto">Daniel Augusto de Araújo Gonçalves</a>, <a href="https://github.com/davibasa">Davi Basã Henrique Alves</a>, <a href="https://github.com/Fernandoliveira05">Fernando Soares de Oliveira</a>, <a href="https://github.com/giovanna-britto">Giovanna Fátima de Britto Vieira</a>, <a href="https://github.com/gucolombini">Gustavo Colombini</a>, <a href="https://github.com/Rafaelfurtadovs">Rafael Furtado Victor dos Santos</a> is licensed under <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>