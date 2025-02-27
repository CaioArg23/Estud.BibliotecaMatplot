import matplotlib.pyplot as plt

alunos = ['joão', 'maria', 'josé']
notas = [8.5, 9, 6.5]

plt.bar(alunos, notas)
plt.xlabel('Alunos')  
plt.ylabel('Notas')   
plt.title('Notas dos Alunos')  
plt.show()  
