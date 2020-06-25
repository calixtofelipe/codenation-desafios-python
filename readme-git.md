GIT COMANDOS

# mostra as configurações globais do git
git config --list

# depois de criar uma pasta no sistema, dentro da pasta executa esse comando para criar o reposito e arquivos git.
git init

# mostra como está o repositório (se tem algum arquivo que precisa ser incluido.
git status

# inclui o arquivo no git
git add [nome_arquivo]

# depois que arquivo é adicionado ao rodar o comando status o git irá mostrar os arquivos que podem ser incluidos
# e mostra também dos arquivos que já estão incluidos quais foram atualizados e podem ser atualizados no git.
# nesse momento pode ser executado o commit. Ou seja o git irá pegar os arquivos do repositorio
# o parametro m é para adicionar um comentario sobre quais mudanças foram feitas
# sempre tem que adicionar antes de commit para que seja atualizado.
git commit -m "Ajustado readme-git"

