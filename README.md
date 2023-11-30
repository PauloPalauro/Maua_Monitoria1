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
<br>

4. Instalar dependências

```bash
pip install -r requirements.txt
```

<br>
<br>

5. Instale o Djongo

```bash
pip install djongo
```

<br>
<br>

6. Instale o pymongo

```bash
pip install pymongo==3.12.3
```

<br>
<br>

7. Faça migrações e migre

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```
<br>
<br>

8. Criar administrador/superusuário

```bash
python manage.py createsuperuser
```
- Crie um nome pro admin;


- Email pode deixar em branco e


- Crie uma senha.

<br>
<br>

9 . Execute o projeto

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


## AWS EC2

python3 manage.py runserver 0.0.0.0:8000

<br>
<br>

Exibir todos os screens
<br>
screen -list

<br>
<br>

Criar screen com um nome
<br>
screen -S monitoria

<br>
<br>

Reconectar ao screen
<br>
screen -r monitoria

<br>
<br>

Encerrar screen
<br>
screen -X -S monitoria

<br>
<br>

Sair do screen
<br>
ctrl-A + d

<br>
<br>

Redirecionar a porta 80 para a porta 8080
<br>
sudo /sbin/iptables -t nat -I PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 8000
