"""
Positional-only arguments -> / 
	Tudo antes da barra deve ser APENAS posicional

Keyword-only arguments -> *
	Tudo depois do asterisco deve ser APENAS nomeados
"""

def soma(a,b,/,x,y):
	print(a+b+x+y)

def multi(a,b,*,c):
	print(a * b * c)

 
soma(1,2,x=3,y=4)
# soma(a=1, b=2, x=3, y=4) # erro

multi(1, 2, c=3)
# multi(1, 2, 3) # erro