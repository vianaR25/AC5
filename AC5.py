#1
def imprime_padrao(n):
  for i in range(1, n + 1):
      for j in range(1, i + 1):
          print(j, end=" ")
      print()

def main():
  n = int(input("Digite o valor de n: "))
  imprime_padrao(n)

if __name__ == "__main__":
  main()


#2
def contar(n):
  n_str = str(n)
  digitos = len(n_str)
  return digitos


n = int(input("Digite um número : "))
q = contar(n)
print(f"O número {n} tem {q} dígitos.")




#3
try:
  
  n1 = int(input(" primeiro número inteiro: "))
  n2 = int(input("segundo número inteiro: "))

  
  resul = n1 / n2

except ValueError:
  print("Erro: nao sao números válidos.")

except ZeroDivisionError:
  print("Erro: Divisão por zero .")

else:
  print(f"Resultado : {resul}")

finally:
  print("Finalzado.")
