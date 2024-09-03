from datetime import datetime as dt

class Funcionarios:

  def __init__(self, nome, sobrenome, anoNascimento):
    self.nome = nome
    self.sobrenome = sobrenome
    self.anoNascimento = anoNascimento
  
  def nomeCompleto(self):
    return self.nome + ' ' + self.sobrenome
  
  def idadeFuncionario(self):
    anoAtual = dt.now().year
    self.anoNascimento = int(anoAtual - self.anoNascimento)
    return self.anoNascimento

usuario1 = Funcionarios("caique", 'fernandes', 2004)
usuario2 = Funcionarios("zé", 'aciole', 2000)
usuario3 = Funcionarios("rachel", 'ferreira', 2007)


print(Funcionarios.idadeFuncionario(usuario1))