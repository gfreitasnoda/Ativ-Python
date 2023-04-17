import matplotlib.pyplot as plt
import mpld3 

marcas = ["Nike", "Adidas", "Puma", "Versace", "Prada"]
vendas = [70,50,25,10,5]

#plt.bar(marcas, vendas)
plt.pie(vendas, labels=marcas)
mpld3.show()