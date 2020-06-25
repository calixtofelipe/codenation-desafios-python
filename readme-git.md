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
git commit -m "Ajustado readme-git"

# se a edicao é em um arquivo que ja existe dentro do git
git commit -am "ajustado readme-git v4"

# ciclo de vida status git
# untracked (o git ainda não conhece o arquivo)>> unmodified (nao teve modificacao) >> modified (o arquivo foi alterado mais ainda não foi salvo) >> staged (pronto para commit)

# comando para acompanhar os log
git log

# comando para ver a mensagem e quem fez
git shortlog

# ver quantidade commit e o nome
git shortlog -sn

# ver o log com grafico (acompanhar merge rebase)
git log --graph

# para ver as modificações
git show [hash_do_commit] 

# para ver as mudanças antes mesmo de commit
git diff

# para pegar somente o nome do arquivo que foi modificado
git diff --name-only

# para voltar o arquivo para antes da edição
git checkout [nome_arquivo]

# se adicionou a mudança e ainda não deu o commit e que voltar. O arquivo volta para o estagio anterior.
git reset HEAD [nome_arquivo]

# se deu o commit e quer resetar. o soft irá voltar para o estagio antes commit. O mixed irá voltar para o estagio modificado e não adicionado. 
# O hard volta para o estagio sem modificacao
git reset --soft --mixed --hard [hash_commit_anterior_ao_que_deseja_resetar]

# para salvar no git online. cria um repositorio
# (antes de salvar eu criei minha chave ssh no meu diretorio user/.ssh e salvei a hash no meu github para autenticar quando eu estiver usando minha máquina
git remote add origin git@github.com:calixtofelipe/codenation-desafios-python.git
git push -u origin master










