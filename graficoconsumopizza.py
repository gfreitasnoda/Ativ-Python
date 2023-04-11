import matplotlib.pyplot as plt

sabores = ["Mussarela", "Calabresa","Calamusa", "Portuguesa", "Frango Catupiry", "Marguerita"]
consumo = [20,15,2,8,50,2]

plt.pie(consumo, labels=sabores)
plt.show()