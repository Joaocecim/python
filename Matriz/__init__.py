import random
disciplina=[]
for i in range(3):
    turma=[]
    for j in range(10):
        alunos=[]
        for k in range(3):
            alunos+=[random.randint(0,10)]
        turma+=[alunos]
    disciplina+=[turma]
print(disciplina)
media=0
maior=0
for i in range(len(disciplina)):
    print(f'turma {i}')
    for j in range(len(disciplina[0])):
        for k in range(len(disciplina[0][0])):
            media+=disciplina[i][j][k]/3
            if maior<media:
                maior=media

        print(f'aluno {j} : {media:.2f}')
print(maior)


