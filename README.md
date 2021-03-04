# Git global setup

<p> git config --global user.name "David Silva"
<p> git config --global user.email "david.dacostaesilva@gmail.com"

# Create a new repository 

<p> git clone https://gitlab.com/david710/python.git
<p>cd python
<p>touch README.md
<p>git add README.md
<p>git commit -m "add README"
<p>git push -u origin master
<p>git pull (para puxar arquivos do repositorio)
<p>git rm <arquivo> (para deletar arquivos)
<p>git rm -r <directory> (para deletar diretorio)

# Push an existing folder 

<p>cd existing_folder
<p>git init
<p>git remote add origin https://gitlab.com/david710/python.git
<p>git add .
<p>git commit -m "Initial commit"
<p>git push -u origin master

# Push an existing Git repository 

<p>cd existing_repo
<p>git remote rename origin old-origin
<p>git remote add origin https://gitlab.com/david710/python.git
<p>git push -u origin --all
<p>git push -u origin --tags
