<p align="center">
  <img src="https://i.imgur.com/pw6QG4H.png" width="200" alt="maua monitoria" />
</p>

<h1 align="center">Mauá Monitoria</h1>

<br>

# Projeto &middot; [![GitHub license](https://img.shields.io/badge/IMT-P.I-blue.svg)](https://maua.br/)

Bem-vindo ao repositório do nosso Projeto Integrador do IMT **(Instituto Mauá de Tecnologia)** dedicado à criação de uma ferramenta para a monitoria da faculdades. Este projeto nasceu da necessidade de aprimorar a interação entre monitores e alunos, visando otimizar a experiência educacional dentro da nossa instituição.

Com esta iniciativa pretendemos não só satisfazer os requisitos académicos, mas também criar soluções práticas e aplicáveis ​​que reflitam o compromisso da nossa instituição com a melhoria contínua dos seus processos educativos.

<br>

# Tech Stack

- [Python 3](https://www.python.org/downloads/)
- [Django](https://www.djangoproject.com/download/)
- [MongoDB](https://www.mongodb.com/try/download/community)
- [MongoDB Atlas](https://www.mongodb.com/atlas)
- [HTML / CSS](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [Bootstrap](https://getbootstrap.com/docs/4.0/getting-started/download/)
<br>

# Instalação

Para começar a utilizar nosso projeto, siga estas simples etapas de instalação:

1. Clone o projeto
```bash
git clone https://github.com/PauloEduardoPalauro/Maua_Monitoria1
```
<br>
2. Vá para o diretório do projeto

```bash
cd Maua_Monitoria1
```
<br>
3. Crie um ambiente virtual e ative-o

```bash 
python3 -m venv env
```
* Windows -
```bash
 env\Scripts\activate
```
* Linux - 
```bash
 . env/bin/activate
```
<br>
4. Instalar dependências

```bash
pip install -r requirements.txt
```
<br>
5. Instale o Djongo

```bash
pip install djongo
```
<br>
6. Instale o pymongo

```bash
pip install pymongo==3.12.3
```
<br>
7. Faça migrações e migre

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```
<br>
8. Criar administrador/superusuário

```bash
python manage.py createsuperuser
```
- Crie um nome pro admin;


- Email pode deixar em branco e


- Crie uma senha.
<br>
9 . Execute o projeto

```bash
python manage.py runserver
```

Agora o projeto deve estar rodando em http://127.0.0.1:8000/

<br>

# Utilização (Opcional)

1. Cadastre um Curso
   - Add department   
<br>

2. Cadastre um Monitor e aloca-lo no Curso
   - Add faculty > Departament
<br>

3. Cadastrar uma materia e aloca-la em um curso e a um monitor
  - Add course > Departament > Faculty
  - StudentKey - Codigo para alunos que não estam cadastrado nessa materia possam se cadastrar (Igual openLMS)
<br>

4. Cadastras Aluno e aloca-lo em um curso. 
  - Add student > Department
  - Course - PODE OU NÃO aloca-lo de uma vez em um curso, ou deixá-lo entrar por conta própria em um curso através da chave que foi cadastrada na matéria.
<br>

5. Faça Login como Estudante e como Monitor para ver se está tudo correto.
  - Clique em > View Site
  - Login como Estudante > Sair
  - Login como Monitor > Sair
<br>

6. Aproveite e faça seus testes.

<br>

# Imagens

<img src="https://i.imgur.com/8MInMsf.png" width="500" alt="maua monitoria" /> <img src="https://i.imgur.com/4ZXlOBq.png" width="500" alt="maua monitoria" />
<img src="https://i.imgur.com/cwhXc6Y.png" width="500" alt="maua monitoria" /> <img src="https://i.imgur.com/Jvj6SUG.png" width="500" alt="maua monitoria" />

<br>

# Considerações Finais

Nas considerações finais, enfatizamos a importância da ferramenta de monitoria no aprimoramento da interação acadêmica. O projeto proporcionou aprendizados valiosos, reforçando nossa crença na inovação educacional. Esperamos que este trabalho inspire melhorias contínuas na experiência de aprendizado. E por fim agradecimentos a quem fez esse projeto ser possivel:

- Paulo Palauro
- Ana Beatriz
- Bianca Ferreira
- Gabriel Messias


