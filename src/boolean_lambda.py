# Definindo os valores booleanos
TRUE = lambda x: lambda y: x
FALSE = lambda x: lambda y: y

# Definindo os operadores booleanos
NOT = lambda b: b(FALSE)(TRUE)
AND = lambda p: lambda q: p(q)(FALSE)
OR = lambda p: lambda q: p(TRUE)(q)
NAND = lambda p: lambda q: NOT(AND(p)(q))
NOR = lambda p: lambda q: NOT(OR(p)(q))
XOR = lambda p: lambda q: OR(AND(p)(NOT(q)))(AND(NOT(p))(q))

# Definindo o condicional IF, que nada mais é do que a aplicação da função de um valor booleano
IF = lambda condition: lambda x: lambda y: condition(x)(y)

# Função para facilitar a vizualição dos resultados dos operadores booleanos
def resultado(r):
    if callable(r) == True:
        if r(1)(0) == 1:
            return 'TRUE'
        else:
            return 'FALSE'
    else: 
        return r

def main():
    print('\nEscreva o seu operador booleano (NOT, AND, OR, NOR, NAND, XOR) e seu argumento')
    while True:
        try:
            str_expr = input('>').strip().upper()
            result = eval(str_expr)
            print(resultado(result))
        except KeyboardInterrupt:
            print('\nTchau!')
            break    
        except Exception as e:
            print(f"Erro na expressão: {e}")

if __name__ == '__main__':
    main()