from django.db import models
'''
 private final String CREATE_TABLE = "CREATE TABLE IF NOT EXISTS Bebidas (ID INTEGER PRIMARY KEY AUTOINCREMENT, Fabricante TEXT NOT NULL, " +
			"Mililitros REAL, Estabelecimento TEXT, Preço REAL NOT NULL);";

  //  private final String CREATE_TABLE5 = "CREATE TABLE IF NOT EXISTS Bebidas5 (ID INTEGER PRIMARY KEY AUTOINCREMENT, Fabricante TEXT NOT NULL, " +
	//            "Mililitros REAL, Estabelecimento TEXT, Preço REAL NOT NULL, " + " FOREIGN KEY (Estabelecimento) REFERENCES Estabelecimento(Nome));";

	private final String CREATE_TABLE2 = "CREATE TABLE IF NOT EXISTS Estabelecimento (ID INTEGER PRIMARY KEY AUTOINCREMENT, Nome TEXT NOT NULL, " +
			"Endereço TEXT);";

	private final String CREATE_TABLE3 = "CREATE TABLE IF NOT EXISTS Cesta (ID INTEGER PRIMARY KEY AUTOINCREMENT, Nome TEXT NOT NULL);";

	'''

# Create your models here.
class Bebidas(models.Model):
	id = models.AutoField(primary_key=True)
	fabricante = models.TextField(max_length=60, null=False)
	mililitros = models.IntegerField()
	estabelecimento = models.TextField(max_length=60, null=False)
	preco = models.FloatField(null=False)

	def __str__(self):
		return "%s - %sml" % (self.fabricante, self.mililitros)

class Estabelecimento(models.Model):
	id = models.AutoField(primary_key=True)
	nome = models.TextField(max_length=60, null=False)
	endereco = models.TextField(max_length=60, null=False)

	def __str__(self):
		return self.nome

class Cesta(models.Model):
	id = models.AutoField(primary_key=True)
	nome = models.TextField(null=False)
	
	def __str__(self):
		return self.nome

class Item(models.Model):
	id = models.AutoField(primary_key=True)
	id_cesta = models.IntegerField()
	id_bebida = models.IntegerField()
		
	def __str__(self):
		return self.id
		
