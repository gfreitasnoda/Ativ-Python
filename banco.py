import pymysql
import matplotlib.pyplot as plt

# Estabelcer a comunicação com o banco de dados
#que está no container
con = pymysql.connect(host="127.0.0.1",
                      user="root",
                      password="senac@123",
                      database="bancobd",
                      port=6556,
                      
                      )

dep = []
vlr = []


cur = con.cursor()
cur.execute("select departamento,count(departamento) as `status` from chamado where statuschamada='Pendente'group by departamento;")
resultado = cur.fetchall()
for i in resultado:
    dep.append(i[0])
    vlr.append(i[1])

cur.close 

plt.figure().set_figwidth(30)
plt.figure().set_figheight(5)
plt.bar(dep,vlr)
plt.xlabel("Departamentos")
plt.ylabel("Valores")
plt.show()
plt.savefig("/usr/share/nginx/html/dep_vlr.png")
#plt.pie(preco_produtos, labels=nome_produtos)
#plt.savefig("/usr/share/nginx/html/produto_preco_pie.png")

pagina = """"
<html>
    <head>
    <title> Grafico de produtos</title>
    </head>
    <body>
        <img src="dep_vlr.png">
    </body>
</html>
"""

arquivo = open("/usr/share/nginx/html/dep_vlr.html","w")
arquivo.write(pagina)
arquivo.close()
