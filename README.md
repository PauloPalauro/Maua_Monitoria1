## RODAR LOCALMENTE

1. Clone o projeto

```bash
git clone https://github.com/PauloEduardoPalauro/Maua_Monitoria1
```
<br>
<br>

2. Vá para o diretório do projeto

```bash
cd Maua_Monitoria1
```
<br>
<br>

3. Crie um ambiente virtual e ative-o

```bash 
python -m venv env
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
<br>

4. Instalar dependências

```bash
pip install -r requirements.txt
```

<br>
<br>

5. Faça migrações e migre

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```
<br>
<br>

6. Criar administrador/superusuário

```bash
python manage.py createsuperuser
```
- Crie um nome pro admin;


- Email pode deixar em branco e


- Crie uma senha.

<br>
<br>

7. Instale o Djongo

```bash
pip install djongo
```

<br>
<br>

8. Vá no MongoDB e crie um novo Database

   MongoDB Compass > New DataBase > Escolha os nommes do DataBase e da Coleção (Serão usados a frente)

<br>
<br>

9. Va no Settings.py e mude o Nome do Database para o nome que você escolheu

    eMLS > settings.py > DATABASES > 'NAME' : 'NOME_DO_SEU_DATABASE'

<br>
<br>

10. Instale o pymongo

```bash
pip install pymongo==3.12.3
```

<br>
<br>

11 . Repita o Passo 5 novamente

<br>
<br>

12 . Execute o projeto

```bash
python manage.py runserver
```

Agora o projeto deve estar rodando em http://127.0.0.1:8000/

<br>
<br>

## Utilização Inicial

1. Clique em > Logar como Admin > Faça Login com o administrador/superusuário que criou acima.

2. E comece de utilizar da forma que preferir.

<br>
<br>

## Recomendação de como utilizar:

1. Cadastre um Curso
   - Add department
     
<br>
<br>

2. Cadastre um Monitor e aloca-lo no Curso
   - Add faculty > Departament

<br>
<br>

3. Cadastrar uma materia e aloca-la em um curso e a um monitor
  - Add course > Departament > Faculty
  - StudentKey - Codigo para alunos que não estam cadastrado nessa materia possam se cadastrar (Igual openLMS)
    
<br>
<br>

4. Cadastras Aluno e aloca-lo em um curso. 
  - Add student > Department
  - Course - PODE OU NÃO aloca-lo de uma vez em um curso, ou deixá-lo entrar por conta própria em um curso através da chave que foi cadastrada na matéria.

<br>
<br>

5. Faça Login como Estudante e como Monitor para ver se está tudo correto.
  - Clique em > View Site
  - Login como Estudante > Sair
  - Login como Monitor > Sair

<br>
<br>

6. Aproveite e faça seus testes.

