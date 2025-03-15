import csv
import pandas as pd
import matplotlib.pyplot as plt
list_column = []

File = "/Users/francescomazzola/Desktop/PoliMI/_Triennale/3 Anno/2 Semestre/Progetti/Progetto_ING_INFORMATICA/Etica dei Dati/updated_performance.csv"	

with open('/Users/francescomazzola/Desktop/PoliMI/_Triennale/3 Anno/2 Semestre/Progetti/Progetto_ING_INFORMATICA/Etica dei Dati/updated_performance.csv') as csv_file:

	csv_reader = csv.reader(csv_file,delimiter = '\t')

	header_row = next(csv_reader)

	for column_name in header_row:

		list_column.append(column_name)

import csv
import matplotlib.pyplot as plt
import random

def update_performance(file_csv):
	try:
		# Leggi il file CSV con il delimitatore ';'
		with open(file_csv, 'r', newline='') as file:
			csv_reader = csv.reader(file, delimiter=';')
			intestazioni = next(csv_reader)  # Leggi le intestazioni
			
			# Rimuovi spazi bianchi dalle intestazioni
			intestazioni = [header.strip() for header in intestazioni]
			
			# Messaggio di debug per verificare le intestazioni lette
			#print("Intestazioni lette:", intestazioni)
			
			# Verifica che il campo "Performance" esista nelle intestazioni
			if "Performance" not in intestazioni:
				print("Il campo 'Performance' non esiste nel file CSV.")
				return
			
			# Converti le righe in una lista di dizionari
			dati = [dict(zip(intestazioni, [cell.strip() for cell in riga])) for riga in csv_reader]
			
		# Aggiungi valori casuali alla colonna "Performance"
		for riga in dati:
			riga["Performance"] = str(random.randint(1, 10))
			
		# Salva i dati aggiornati in un nuovo file CSV
		nuovo_file_csv = "updated_performance.csv"
		with open(nuovo_file_csv, 'w', newline='') as file_output:
			csv_writer = csv.DictWriter(file_output, fieldnames=intestazioni)
			csv_writer.writeheader()
			csv_writer.writerows(dati)
			
		print("Il file è stato aggiornato con valori casuali nella colonna 'Performance' e salvato come:", nuovo_file_csv)
		
	except FileNotFoundError:
		print("File non trovato!")
	except Exception as e:
		print("Si è verificato un errore:", e)
		
		
def start_situation_clerk(file_csv):
	try:
		# Leggi il file CSV con il delimitatore ';'
		with open(file_csv, 'r', newline='') as file:
			csv_reader = csv.reader(file, delimiter=',')
			intestazioni = next(csv_reader)  # Leggi le intestazioni
			
			# Converti le righe in una lista di dizionari
			dati = [dict(zip(intestazioni, riga)) for riga in csv_reader]
			
			# Filtra le righe che non contengono "MANAGER"
			dati_filtrati = [riga for riga in dati if riga.get("Role") != "MANAGER"]
						
		# Calcola il numero di maschi, femmine e membri delle diverse etnie
		num_maschi = sum(1 for riga in dati_filtrati if riga.get("Gender") == "Male")
		num_femmine = sum(1 for riga in dati_filtrati if riga.get("Gender") == "Female")
		
		# Calcola il numero di membri per ciascuna etnia
		num_Hispanic = sum(1 for riga in dati_filtrati if riga.get("Ethnicity") == "Hispanic")
		num_Other = sum(1 for riga in dati_filtrati if riga.get("Ethnicity") == "Other")
		num_Black = sum(1 for riga in dati_filtrati if riga.get("Ethnicity") == "Black")
		num_Asian = sum(1 for riga in dati_filtrati if riga.get("Ethnicity") == "Asian")
		num_White = sum(1 for riga in dati_filtrati if riga.get("Ethnicity") == "White")
		
		#Calcolo il numero per paga
		num_zona_A = sum(1 for riga in dati_filtrati if riga.get("Salary") == "Zone A")
		num_zona_B = sum(1 for riga in dati_filtrati if riga.get("Salary") == "Zone B")
		num_zona_C = sum(1 for riga in dati_filtrati if riga.get("Salary") == "Zone C")
		
		#Calcolo il numero per situazione familiare 
		num_single = sum(1 for riga in dati_filtrati if riga.get("FamSituation") == "Single")
		num_married = sum(1 for riga in dati_filtrati if riga.get("FamSituation") == "Married")
		num_widowed = sum(1 for riga in dati_filtrati if riga.get("FamSituation") == "Widowed")
		num_divorced = sum(1 for riga in dati_filtrati if riga.get("FamSituation") == "Divorced")
		num_performance_1 = sum(1 for riga in dati_filtrati if int(riga.get("Performance")) == 1)
		num_performance_2 = sum(1 for riga in dati_filtrati if int(riga.get("Performance")) == 2)
		num_performance_3 = sum(1 for riga in dati_filtrati if int(riga.get("Performance")) == 3)
		num_performance_4 = sum(1 for riga in dati_filtrati if int(riga.get("Performance")) == 4)
		num_performance_5 = sum(1 for riga in dati_filtrati if int(riga.get("Performance")) == 5)
		num_performance_6 = sum(1 for riga in dati_filtrati if int(riga.get("Performance")) == 6)
		num_performance_7 = sum(1 for riga in dati_filtrati if int(riga.get("Performance")) == 7)
		num_performance_8 = sum(1 for riga in dati_filtrati if int(riga.get("Performance")) == 8)
		num_performance_9 = sum(1 for riga in dati_filtrati if int(riga.get("Performance")) == 9)
		num_performance_10 = sum(1 for riga in dati_filtrati if int(riga.get("Performance")) == 10)
		
		# Estrai i valori delle performance e converti in numeri interi
		performance_values = [int(riga["Performance"]) for riga in dati_filtrati if "Performance" in riga and riga["Performance"].isdigit()]
		
		# Calcola la somma delle performance
		sum_performance = sum(performance_values)
		
		# Calcola il numero di valori di performance
		num_performance = len(performance_values)
		
		# Calcola la media della performance
		if num_performance > 0:
			media = sum_performance / num_performance
		else:
			media = 0
			
			
		# Salva i dati selezionati in un nuovo file CSV
		nuovo_file_csv = "output_situation_clerk.csv"
		with open(nuovo_file_csv, 'w', newline='') as file_output:
			csv_writer = csv.DictWriter(file_output, fieldnames=intestazioni)
			csv_writer.writeheader()
			csv_writer.writerows(dati_filtrati)
			
		print("Il file è stato ordinato, filtrato e salvato con successo come:", nuovo_file_csv)
		
		index_performance = [1,2,3,4,5,6,7,8,9,10]
		data_index_performance = [num_performance_1, num_performance_2,num_performance_3,num_performance_4,num_performance_5,
			num_performance_6,num_performance_7,num_performance_8,num_performance_9,num_performance_10]
		plt.pie(data_index_performance, labels=index_performance,autopct='%1.1f%%',textprops={'fontsize': 16})
		plt.title(f"Distribuzione per indice performance. \nLa media è {media:.2f}",fontsize=20)
		plt.show()
		# Crea il grafico a torta per il genere
		fig = plt.figure(figsize=(10, 7))
		gender = ["Male", "Female"]
		data_gender = [num_maschi, num_femmine]
		plt.pie(data_gender, labels=gender,autopct='%1.1f%%',textprops={'fontsize': 16})
		plt.title("Distribuzione per genere",fontsize=16)
		plt.show()
		
		
		# Crea il grafico a torta per l'etnia
		fig = plt.figure(figsize=(10, 7))
		Etnia = ["Hispanic", "Other", "Black", "Asian", "White"]
		data_etnia = [num_Hispanic, num_Other, num_Black, num_Asian, num_White]
		plt.pie(data_etnia, labels=Etnia, autopct='%1.1f%%')
		plt.title("Distribuzione per Etnia")
		plt.show()
		
		# Crea il grafico a torta per la paga
		fig = plt.figure(figsize=(10, 7))
		Zone = ["Zone A", "Zone B", "Zone C"]
		data_zona = [num_zona_A,num_zona_B,num_zona_C]
		plt.pie(data_zona, labels=Zone, autopct='%1.1f%%')
		plt.title("Distribuzione per Paga")
		plt.show()
		
		# Crea il grafico a torta la situazione familiare
		fig = plt.figure(figsize=(10, 7))
		FamSituation = ["Single", "Married", "Widowed", "Divorced"]
		data_fam = [num_single,num_married,num_widowed,num_divorced]
		plt.pie(data_fam, labels=FamSituation, autopct='%1.1f%%')
		plt.title("Distribuzione per Situazione Familiare")
		plt.show()
		
	except FileNotFoundError:
		print("File non trovato!")
	except Exception as e:
		print("Si è verificato un errore:", e)
		
def start_situation_manager(file_csv):
			try:
				# Leggi il file CSV con il delimitatore '\t'
				with open(file_csv, 'r', newline='') as file:
					csv_reader = csv.reader(file, delimiter=',')
					intestazioni = next(csv_reader)  # Leggi le intestazioni
					intestazioni = [header.strip() for header in intestazioni]
					
							# Messaggio di debug per verificare le intestazioni lette
					print("Intestazioni lette:", intestazioni)
					if "Role" not in intestazioni:
												print("Il campo 'Role' non esiste nel file CSV.")
												return
					# Converti le righe in una lista di dizionari
					dati = [dict(zip(intestazioni, riga)) for riga in csv_reader]
					
					# Filtra le righe che non contengono "MANAGER"
					dati_filtrati = [riga for riga in dati if riga.get("Role").strip().upper() == "MANAGER"]
					
					
				# Calcola il numero di maschi, femmine e membri delle diverse etnie
				num_maschi = sum(1 for riga in dati_filtrati if riga.get("Gender") == "Male")
				num_femmine = sum(1 for riga in dati_filtrati if riga.get("Gender") == "Female")
				# Calcola il numero di membri per ciascuna etnia
				num_Hispanic = sum(1 for riga in dati_filtrati if riga.get("Ethnicity") == "Hispanic")
				num_Other = sum(1 for riga in dati_filtrati if riga.get("Ethnicity") == "Other")
				num_Black = sum(1 for riga in dati_filtrati if riga.get("Ethnicity") == "Black")
				num_Asian = sum(1 for riga in dati_filtrati if riga.get("Ethnicity") == "Asian")
				num_White = sum(1 for riga in dati_filtrati if riga.get("Ethnicity") == "White")
				
				#Calcolo il numero per paga
				num_zona_A = sum(1 for riga in dati_filtrati if riga.get("Salary") == "Zone A")
				num_zona_B = sum(1 for riga in dati_filtrati if riga.get("Salary") == "Zone B")
				num_zona_C = sum(1 for riga in dati_filtrati if riga.get("Salary") == "Zone C")
				
				#Calcolo il numero per situazione familiare 
				num_single = sum(1 for riga in dati_filtrati if riga.get("FamSituation") == "Single")
				num_married = sum(1 for riga in dati_filtrati if riga.get("FamSituation") == "Married")
				num_widowed = sum(1 for riga in dati_filtrati if riga.get("FamSituation") == "Widowed")
				num_divorced = sum(1 for riga in dati_filtrati if riga.get("FamSituation") == "Divorced")
				num_performance_1 = sum(1 for riga in dati_filtrati if int(riga.get("Performance")) == 1)
				num_performance_2 = sum(1 for riga in dati_filtrati if int(riga.get("Performance")) == 2)
				num_performance_3 = sum(1 for riga in dati_filtrati if int(riga.get("Performance")) == 3)
				num_performance_4 = sum(1 for riga in dati_filtrati if int(riga.get("Performance")) == 4)
				num_performance_5 = sum(1 for riga in dati_filtrati if int(riga.get("Performance")) == 5)
				num_performance_6 = sum(1 for riga in dati_filtrati if int(riga.get("Performance")) == 6)
				num_performance_7 = sum(1 for riga in dati_filtrati if int(riga.get("Performance")) == 7)
				num_performance_8 = sum(1 for riga in dati_filtrati if int(riga.get("Performance")) == 8)
				num_performance_9 = sum(1 for riga in dati_filtrati if int(riga.get("Performance")) == 9)
				num_performance_10 = sum(1 for riga in dati_filtrati if int(riga.get("Performance")) == 10)
				
				# Estrai i valori delle performance e converti in numeri interi
				performance_values = [int(riga["Performance"]) for riga in dati_filtrati if "Performance" in riga and riga["Performance"].isdigit()]
				
				# Calcola la somma delle performance
				sum_performance = sum(performance_values)
				
				# Calcola il numero di valori di performance
				num_performance = len(performance_values)
				
				# Calcola la media della performance
				if num_performance > 0:
					media = sum_performance / num_performance
				else:
					media = 0
					
					
				
				# Salva i dati selezionati in un nuovo file CSV
				nuovo_file_csv = "output_situation_manager.csv"
				with open(nuovo_file_csv, 'w', newline='') as file_output:
					csv_writer = csv.DictWriter(file_output, fieldnames=intestazioni)
					csv_writer.writeheader()
					csv_writer.writerows(dati_filtrati)
					
				print("Il file è stato ordinato, filtrato e salvato con successo come:", nuovo_file_csv)
				
				# Crea il grafico a torta per il genere
				fig = plt.figure(figsize=(10, 7))
				gender = ["Male", "Female"]
				data_gender = [num_maschi, num_femmine]
				plt.pie(data_gender, labels=gender,autopct='%1.1f%%',textprops={'fontsize': 16})
				plt.title("Distribuzione per genere",fontsize = 16)
				plt.show()
				
				index_performance = [1,2,3,4,5,6,7,8,9,10]
				data_index_performance = [num_performance_1, num_performance_2,num_performance_3,num_performance_4,num_performance_5,
					num_performance_6,num_performance_7,num_performance_8,num_performance_9,num_performance_10]
				plt.pie(data_index_performance, labels=index_performance,autopct='%1.1f%%',textprops={'fontsize': 16})
				plt.title(f"Distribuzione per indice performance. \nLa media è {media:.2f}",fontsize=20)
				plt.show()
				
				# Crea il grafico a torta per l'etnia
				fig = plt.figure(figsize=(10, 7))
				Etnia = ["Hispanic", "Other", "Black", "Asian", "White"]
				data_etnia = [num_Hispanic, num_Other, num_Black, num_Asian, num_White]
				plt.pie(data_etnia, labels=Etnia, autopct='%1.1f%%',textprops={'fontsize': 16})
				plt.title("Distribuzione per Etnia",fontsize = 16)
				plt.show()
				
				# Crea il grafico a torta per la paga
				fig = plt.figure(figsize=(10, 7))
				Zone = ["Zone A", "Zone B", "Zone C"]
				data_zona = [num_zona_A,num_zona_B,num_zona_C]
				plt.pie(data_zona, labels=Zone, autopct='%1.1f%%')
				plt.title("Distribuzione per Paga")
				plt.show()
				
				# Crea il grafico a torta la situazione familiare
				fig = plt.figure(figsize=(10, 7))
				FamSituation = ["Single", "Married", "Widowed", "Divorced"]
				data_fam = [num_single,num_married,num_widowed,num_divorced]
				plt.pie(data_fam, labels=FamSituation, autopct='%1.1f%%')
				plt.title("Distribuzione per Situazione Familiare")
				plt.show()
				
			except FileNotFoundError:
				print("File non trovato!")
			except Exception as e:
				print("Si è verificato un errore:", e)
				
				
def equality(file_csv, num_manager):
					try:
						# Leggi il file CSV con il delimitatore '\t'
						with open(file_csv, 'r', newline='') as file:
							csv_reader = csv.reader(file, delimiter=',')
							intestazioni = next(csv_reader)  # Leggi le intestazioni
							
							# Converti le righe in una lista di dizionari
							dati = [dict(zip(intestazioni, riga)) for riga in csv_reader]
							
							# Filtra le righe che non contengono "MANAGER"
							dati_filtrati = [riga for riga in dati if riga.get("Role") != "MANAGER"]
							dati_manager = [riga for riga in dati if riga.get("Role") == "MANAGER"]
							
							# Dividi il dataset in gruppi basati sulla performance
							gruppi_performance = {}
							for row in dati_filtrati:
								performance = int(row["Performance"])
								if performance not in gruppi_performance:
									gruppi_performance[performance] = []
								gruppi_performance[performance].append(row)
								
							# Mescola casualmente le righe all'interno di ciascun gruppo
							for performance in gruppi_performance:
								random.shuffle(gruppi_performance[performance])
								
							# Ricombina i gruppi mantenendo l'ordine delle performance
							datiConDoppioni_ordinati = []
							for performance in sorted(gruppi_performance.keys(), reverse=True):
								datiConDoppioni_ordinati.extend(gruppi_performance[performance])
								
								
								
							current_index = 0
							datiOutput = []
							pID_set = set()
							
							while len(datiOutput) < numero_manager and current_index < len(datiConDoppioni_ordinati):
								row = datiConDoppioni_ordinati[current_index]
								if row['pID'] not in pID_set:
									datiOutput.append(row)
									pID_set.add(row['pID'])
								current_index += 1
								
							# Ordina i dati in base alla colonna "Performance"
							datiConDoppioni_ordinati.sort(key=lambda x: int(x["Performance"]), reverse=True)
							
							
							# Seleziona solo le prime num_manager righe
							dati_selezionati = datiConDoppioni_ordinati[:num_manager]
							dati_tot = dati_manager + dati_selezionati
							# Calcola il numero di maschi, femmine e membri delle diverse etnie
						num_maschi = sum(1 for riga in dati_selezionati if riga.get("Gender") == "Male")
						num_femmine = sum(1 for riga in dati_selezionati if riga.get("Gender") == "Female")

						# Calcola il numero di membri per ciascuna etnia
						num_Hispanic = sum(1 for riga in dati_tot if riga.get("Ethnicity") == "Hispanic")
						num_Other = sum(1 for riga in dati_tot if riga.get("Ethnicity") == "Other")
						num_Black = sum(1 for riga in dati_tot if riga.get("Ethnicity") == "Black")
						num_Asian = sum(1 for riga in dati_tot if riga.get("Ethnicity") == "Asian")
						num_White = sum(1 for riga in dati_tot if riga.get("Ethnicity") == "White")
						
						#Calcolo il numero per paga
						num_zona_A = sum(1 for riga in dati_tot if riga.get("Salary") == "Zone A")
						num_zona_B = sum(1 for riga in dati_tot if riga.get("Salary") == "Zone B")
						num_zona_C = sum(1 for riga in dati_tot if riga.get("Salary") == "Zone C")
						
						#Calcolo il numero per situazione familiare 
						num_single = sum(1 for riga in dati_tot if riga.get("FamSituation") == "Single")
						num_married = sum(1 for riga in dati_tot if riga.get("FamSituation") == "Married")
						num_widowed = sum(1 for riga in dati_tot if riga.get("FamSituation") == "Widowed")
						num_divorced = sum(1 for riga in dati_tot if riga.get("FamSituation") == "Divorced")
						#Calcolo indice performance
						num_performance_1 = sum(1 for riga in dati_tot if int(riga.get("Performance")) == 1)
						num_performance_2 = sum(1 for riga in dati_tot if int(riga.get("Performance")) == 2)
						num_performance_3 = sum(1 for riga in dati_tot if int(riga.get("Performance")) == 3)
						num_performance_4 = sum(1 for riga in dati_tot if int(riga.get("Performance")) == 4)
						num_performance_5 = sum(1 for riga in dati_tot if int(riga.get("Performance")) == 5)
						num_performance_6 = sum(1 for riga in dati_tot if int(riga.get("Performance")) == 6)
						num_performance_7 = sum(1 for riga in dati_tot if int(riga.get("Performance")) == 7)
						num_performance_8 = sum(1 for riga in dati_tot if int(riga.get("Performance")) == 8)
						num_performance_9 = sum(1 for riga in dati_tot if int(riga.get("Performance")) == 9)
						num_performance_10 = sum(1 for riga in dati_tot if int(riga.get("Performance")) == 10)
						
						# Estrai i valori delle performance e converti in numeri interi
						performance_values = [int(riga["Performance"]) for riga in dati_tot if "Performance" in riga and riga["Performance"].isdigit()]
						
						# Calcola la somma delle performance
						sum_performance = sum(performance_values)
						
						# Calcola il numero di valori di performance
						num_performance = len(performance_values)
						
						# Calcola la media della performance
						if num_performance > 0:
							media = sum_performance / num_performance
						else:
							media = 0
							
							
						# Salva i dati selezionati in un nuovo file CSV
						nuovo_file_csv = "output_equality.csv"
						with open(nuovo_file_csv, 'w', newline='') as file_output:
							csv_writer = csv.DictWriter(file_output, fieldnames=intestazioni)
							csv_writer.writeheader()
							csv_writer.writerows(dati_selezionati)
							csv_writer.writerows(dati_manager)
							
						print("Il file è stato ordinato, filtrato e salvato con successo come:", nuovo_file_csv)
						
						# Crea il grafico a torta per il genere
						fig = plt.figure(figsize=(10, 7))
						gender = ["Male", "Female"]
						data_gender = [num_maschi, num_femmine]
						plt.pie(data_gender, labels=gender,autopct='%1.1f%%',textprops={'fontsize': 16})
						plt.title("Distribuzione per genere",fontsize=20)
						plt.show()
						
						index_performance = [1,2,3,4,5,6,7,8,9,10]
						data_index_performance = [num_performance_1, num_performance_2,num_performance_3,num_performance_4,num_performance_5,
							num_performance_6,num_performance_7,num_performance_8,num_performance_9,num_performance_10]
						plt.pie(data_index_performance, labels=index_performance,autopct='%1.1f%%',textprops={'fontsize': 14})
						plt.title(f"Distribuzione per indice performance. \nLa media è {media:.2f}",fontsize=20)
						plt.show()
						
						# Crea il grafico a torta per l'etnia
						fig = plt.figure(figsize=(10, 7))
						Etnia = ["Hispanic", "Other", "Black", "Asian", "White"]
						data_etnia = [num_Hispanic, num_Other, num_Black, num_Asian, num_White]
						plt.pie(data_etnia, labels=Etnia, autopct='%1.1f%%')
						plt.title("Distribuzione per Etnia")
						plt.show()
						
						# Crea il grafico a torta per la paga
						fig = plt.figure(figsize=(10, 7))
						Zone = ["Zone A", "Zone B", "Zone C"]
						data_zona = [num_zona_A,num_zona_B,num_zona_C]
						plt.pie(data_zona, labels=Zone, autopct='%1.1f%%')
						plt.title("Distribuzione per Paga")
						plt.show()
						
						# Crea il grafico a torta la situazione familiare
						fig = plt.figure(figsize=(10, 7))
						FamSituation = ["Single", "Married", "Widowed", "Divorced"]
						data_fam = [num_single,num_married,num_widowed,num_divorced]
						plt.pie(data_fam, labels=FamSituation, autopct='%1.1f%%')
						plt.title("Distribuzione per Situazione Familiare")
						plt.show()
						
					except FileNotFoundError:
						print("File non trovato!")
					except Exception as e:
						print("Si è verificato un errore:", e)
						
						
def diversity_gender(file_csv, numero_manager):
	try:
		# Leggi il file CSV con il delimitatore '\t'
		with open(file_csv, 'r', newline='') as file:
			csv_reader = csv.reader(file, delimiter=",")
			intestazioni = next(csv_reader)  # Leggi le intestazioni
			
			# Converti le righe in una lista di dizionari
			dati = [dict(zip(intestazioni, riga)) for riga in csv_reader]
			
			# Filtra le righe che contengono "MANAGER"
			dati_MANAGER = [riga for riga in dati if riga.get("Role") == "MANAGER"]
			
			# Filtra le righe che non contengono "MANAGER"
			dati_CLERK = [riga for riga in dati if riga.get("Role") != "MANAGER"]
			num_maschi = sum(1 for riga in dati_MANAGER if riga.get("Gender") == "Male")
			num_femmine = sum(1 for riga in dati_MANAGER if riga.get("Gender") == "Female")
			
			
			num_totale_fin = int((num_maschi + num_femmine + numero_manager) / 2)
			num_femmine_new = num_totale_fin - num_femmine    
			num_maschi_new = num_totale_fin - num_maschi    
			
			dati_selezionati_maschi = []
			dati_selezionati_femmine = []
			
			if num_maschi_new > 0:
				dati_selezionati_maschi = [riga for riga in dati_CLERK if riga.get("Gender") == "Male"]
				dati_selezionati_maschi.sort(key=lambda x: int(x["Performance"]), reverse=True)
				dati_selezionati_maschi = dati_selezionati_maschi[:num_maschi_new]
				
			if num_femmine_new > 0:
				dati_selezionati_femmine = [riga for riga in dati_CLERK if riga.get("Gender") == "Female"]
				dati_selezionati_femmine.sort(key=lambda x: int(x["Performance"]), reverse=True)
				dati_selezionati_femmine = dati_selezionati_femmine[:num_femmine_new]
		
			nuovo_file_csv = "output_diversity_gender.csv"
			
			with open(nuovo_file_csv, 'w', newline='') as file_output:
				csv_writer = csv.DictWriter(file_output, fieldnames=intestazioni)
				csv_writer.writeheader()
				csv_writer.writerows(dati_selezionati_maschi)
				csv_writer.writerows(dati_selezionati_femmine)
				csv_writer.writerows(dati_MANAGER)
				
				# Calcola il numero di maschi, femmine e membri delle diverse etnie
				dati_tot = dati_selezionati_maschi + dati_selezionati_femmine + dati_MANAGER
				dati_candidati =  dati_selezionati_maschi + dati_selezionati_femmine
				
				num_maschi = sum(1 for riga in dati_candidati if riga.get("Gender") == "Male")
				num_femmine = sum(1 for riga in dati_candidati if riga.get("Gender") == "Female")
				
				# Calcola il numero di membri per ciascuna etnia
				num_Hispanic = sum(1 for riga in dati_tot if riga.get("Ethnicity") == "Hispanic")
				num_Other = sum(1 for riga in dati_tot if riga.get("Ethnicity") == "Other")
				num_Black = sum(1 for riga in dati_tot if riga.get("Ethnicity") == "Black")
				num_Asian = sum(1 for riga in dati_tot if riga.get("Ethnicity") == "Asian")
				num_White = sum(1 for riga in dati_tot if riga.get("Ethnicity") == "White")
				
				#Calcolo il numero per paga
				num_zona_A = sum(1 for riga in dati_tot if riga.get("Salary") == "Zone A")
				num_zona_B = sum(1 for riga in dati_tot if riga.get("Salary") == "Zone B")
				num_zona_C = sum(1 for riga in dati_tot if riga.get("Salary") == "Zone C")
				
				#Calcolo il numero per situazione familiare 
				num_single = sum(1 for riga in dati_tot if riga.get("FamSituation") == "Single")
				num_married = sum(1 for riga in dati_tot if riga.get("FamSituation") == "Married")
				num_widowed = sum(1 for riga in dati_tot if riga.get("FamSituation") == "Widowed")
				num_divorced = sum(1 for riga in dati_tot if riga.get("FamSituation") == "Divorced")
				
				#Calcolo indice performance
				num_performance_1 = sum(1 for riga in dati_tot if int(riga.get("Performance")) == 1)
				num_performance_2 = sum(1 for riga in dati_tot if int(riga.get("Performance")) == 2)
				num_performance_3 = sum(1 for riga in dati_tot if int(riga.get("Performance")) == 3)
				num_performance_4 = sum(1 for riga in dati_tot if int(riga.get("Performance")) == 4)
				num_performance_5 = sum(1 for riga in dati_tot if int(riga.get("Performance")) == 5)
				num_performance_6 = sum(1 for riga in dati_tot if int(riga.get("Performance")) == 6)
				num_performance_7 = sum(1 for riga in dati_tot if int(riga.get("Performance")) == 7)
				num_performance_8 = sum(1 for riga in dati_tot if int(riga.get("Performance")) == 8)
				num_performance_9 = sum(1 for riga in dati_tot if int(riga.get("Performance")) == 9)
				num_performance_10 = sum(1 for riga in dati_tot if int(riga.get("Performance")) == 10)
				
				# Estrai i valori delle performance e converti in numeri interi
				performance_values = [int(riga["Performance"]) for riga in dati_tot if "Performance" in riga and riga["Performance"].isdigit()]
				
				# Calcola la somma delle performance
				sum_performance = sum(performance_values)
				
				# Calcola il numero di valori di performance
				num_performance = len(performance_values)
				
				# Calcola la media della performance
				if num_performance > 0:
					media = sum_performance / num_performance
				else:
					media = 0
					
			print("Il file è stato ordinato, filtrato e salvato con successo come:", nuovo_file_csv)
			fig = plt.figure(figsize=(10, 7))
			gender = ["Male", "Female"]
			data_gender = [num_maschi, num_femmine]
			plt.pie(data_gender, labels=gender,autopct='%1.1f%%',textprops={'fontsize': 16})
			plt.title("Distribuzione per genere",fontsize=16)
			plt.show()
			
			index_performance = [1,2,3,4,5,6,7,8,9,10]
			data_index_performance = [num_performance_1, num_performance_2,num_performance_3,num_performance_4,num_performance_5,
				num_performance_6,num_performance_7,num_performance_8,num_performance_9,num_performance_10]
			plt.pie(data_index_performance, labels=index_performance,autopct='%1.1f%%',textprops={'fontsize': 14})
			plt.title(f"Distribuzione per indice performance. \nLa media è {media:.2f}",fontsize=20)
			plt.show()
			
			# Crea il grafico a torta per l'etnia
			fig = plt.figure(figsize=(10, 7))
			Etnia = ["Hispanic", "Other", "Black", "Asian", "White"]
			data_etnia = [num_Hispanic, num_Other, num_Black, num_Asian, num_White]
			plt.pie(data_etnia, labels=Etnia, autopct='%1.1f%%')
			plt.title("Distribuzione per Etnia")
			plt.show()
			
			# Crea il grafico a torta per la paga
			fig = plt.figure(figsize=(10, 7))
			Zone = ["Zone A", "Zone B", "Zone C"]
			data_zona = [num_zona_A,num_zona_B,num_zona_C]
			plt.pie(data_zona, labels=Zone, autopct='%1.1f%%')
			plt.title("Distribuzione per Paga")
			plt.show()
			
			# Crea il grafico a torta la situazione familiare
			fig = plt.figure(figsize=(10, 7))
			FamSituation = ["Single", "Married", "Widowed", "Divorced"]
			data_fam = [num_single,num_married,num_widowed,num_divorced]
			plt.pie(data_fam, labels=FamSituation, autopct='%1.1f%%')
			plt.title("Distribuzione per Situazione Familiare")
			plt.show()
			
	except FileNotFoundError:
		print("File non trovato!")
	except Exception as e:
		print("Si è verificato un errore:", e)
		
def diversity_salary(file_csv, numero_manager):
			try:
				# Leggi il file CSV con il delimitatore ';'
				with open(file_csv, 'r', newline='') as file:
					csv_reader = csv.reader(file, delimiter=',')
					intestazioni = next(csv_reader)  # Leggi le intestazioni
					
					# Converti le righe in una lista di dizionari
					dati = [dict(zip(intestazioni, riga)) for riga in csv_reader]
					
					# Filtra le righe che non contengono "MANAGER"
					dati_MANAGER = [riga for riga in dati if riga.get("Role") == "MANAGER"]
					dati_CLERK = [riga for riga in dati if riga.get("Role") != "MANAGER"]
					
					num_zona_A = sum(1 for riga in dati_MANAGER if riga.get("Salary") == "Zone A")
					num_zona_B = sum(1 for riga in dati_MANAGER if riga.get("Salary") == "Zone B")
					num_zona_C = sum(1 for riga in dati_MANAGER if riga.get("Salary") == "Zone C")
				
					num_totale_fin = int((num_zona_A + num_zona_B + num_zona_C + numero_manager) / 3)
					num_zona_A_new = num_totale_fin - num_zona_A    
					num_zona_B_new = num_totale_fin - num_zona_B    
					num_zona_C_new = num_totale_fin - num_zona_C
				
			
					dati_selezionati_zona_A = []
					dati_selezionati_zona_B = []
					dati_selezionati_zona_C = []
					
					if num_zona_A_new > 0:
						dati_selezionati_zona_A = [riga for riga in dati_CLERK if riga.get("Salary") == "Zone A"]
						dati_selezionati_zona_A.sort(key=lambda x: int(x["Performance"]), reverse=True)
						dati_selezionati_zona_A = dati_selezionati_zona_A[:num_zona_A_new]
						
					if num_zona_B_new > 0:
						dati_selezionati_zona_B = [riga for riga in dati_CLERK if riga.get("Salary") == "Zone B"]
						dati_selezionati_zona_B.sort(key=lambda x: int(x["Performance"]), reverse=True)
						dati_selezionati_zona_B = dati_selezionati_zona_B[:num_zona_B_new]
					if num_zona_C_new > 0:
						dati_selezionati_zona_C = [riga for riga in dati_CLERK if riga.get("Salary") == "Zone C"]
						dati_selezionati_zona_C.sort(key=lambda x: int(x["Performance"]), reverse=True)
						dati_selezionati_zona_C = dati_selezionati_zona_C[:num_zona_C_new]
						
					nuovo_file_csv = "output_diversity_salary.csv"
					
					with open(nuovo_file_csv, 'w', newline='') as file_output:
						csv_writer = csv.DictWriter(file_output, fieldnames=intestazioni)
						csv_writer.writeheader()
						
						csv_writer.writerows(dati_selezionati_zona_A)
						csv_writer.writerows(dati_selezionati_zona_B)
						csv_writer.writerows(dati_selezionati_zona_C)
						csv_writer.writerows(dati_MANAGER)
						
					dati_tot = dati_selezionati_zona_A + dati_selezionati_zona_B + dati_selezionati_zona_C + dati_MANAGER
					dati_candidati = dati_selezionati_zona_A + dati_selezionati_zona_B + dati_selezionati_zona_C
					num_maschi = sum(1 for riga in dati_candidati if riga.get("Gender") == "Male")
					num_femmine = sum(1 for riga in dati_candidati if riga.get("Gender") == "Female")
					
					# Calcola il numero di membri per ciascuna etnia
					num_Hispanic = sum(1 for riga in dati_tot if riga.get("Ethnicity") == "Hispanic")
					num_Other = sum(1 for riga in dati_tot if riga.get("Ethnicity") == "Other")
					num_Black = sum(1 for riga in dati_tot if riga.get("Ethnicity") == "Black")
					num_Asian = sum(1 for riga in dati_tot if riga.get("Ethnicity") == "Asian")
					num_White = sum(1 for riga in dati_tot if riga.get("Ethnicity") == "White")
					
					#Calcolo il numero per paga
					num_zona_A = sum(1 for riga in dati_candidati if riga.get("Salary") == "Zone A")
					num_zona_B = sum(1 for riga in dati_candidati if riga.get("Salary") == "Zone B")
					num_zona_C = sum(1 for riga in dati_candidati if riga.get("Salary") == "Zone C")
					
					#Calcolo il numero per situazione familiare 
					num_single = sum(1 for riga in dati_tot if riga.get("FamSituation") == "Single")
					num_married = sum(1 for riga in dati_tot if riga.get("FamSituation") == "Married")
					num_widowed = sum(1 for riga in dati_tot if riga.get("FamSituation") == "Widowed")
					num_divorced = sum(1 for riga in dati_tot if riga.get("FamSituation") == "Divorced")
					
					# Estrai i valori delle performance e converti in numeri interi
					performance_values = [int(riga["Performance"]) for riga in dati_tot if "Performance" in riga and riga["Performance"].isdigit()]
					
					# Calcola la somma delle performance
					sum_performance = sum(performance_values)
					
					# Calcola il numero di valori di performance
					num_performance = len(performance_values)
					
					# Calcola la media della performance
					if num_performance > 0:
						media = sum_performance / num_performance
					else:
						media = 0
					#Calcolo indice performance
					num_performance_1 = sum(1 for riga in dati_tot if int(riga.get("Performance")) == 1)
					num_performance_2 = sum(1 for riga in dati_tot if int(riga.get("Performance")) == 2)
					num_performance_3 = sum(1 for riga in dati_tot if int(riga.get("Performance")) == 3)
					num_performance_4 = sum(1 for riga in dati_tot if int(riga.get("Performance")) == 4)
					num_performance_5 = sum(1 for riga in dati_tot if int(riga.get("Performance")) == 5)
					num_performance_6 = sum(1 for riga in dati_tot if int(riga.get("Performance")) == 6)
					num_performance_7 = sum(1 for riga in dati_tot if int(riga.get("Performance")) == 7)
					num_performance_8 = sum(1 for riga in dati_tot if int(riga.get("Performance")) == 8)
					num_performance_9 = sum(1 for riga in dati_tot if int(riga.get("Performance")) == 9)
					num_performance_10 = sum(1 for riga in dati_tot if int(riga.get("Performance")) == 10)
					
				print("Il file è stato ordinato, filtrato e salvato con successo come:", nuovo_file_csv)
				fig = plt.figure(figsize=(10, 7))
				gender = ["Male", "Female"]
				data_gender = [num_maschi, num_femmine]
				plt.pie(data_gender, labels=gender,autopct='%1.1f%%')
				plt.title("Distribuzione per genere")
				plt.show()
				
				index_performance = [1,2,3,4,5,6,7,8,9,10]
				data_index_performance = [num_performance_1, num_performance_2,num_performance_3,num_performance_4,num_performance_5,
					num_performance_6,num_performance_7,num_performance_8,num_performance_9,num_performance_10]
				plt.pie(data_index_performance, labels=index_performance,autopct='%1.1f%%')
				plt.title(f"Distribuzione per indice performance. \nLa media è {media:.2f}",fontsize=20)
				plt.show()
				
				# Crea il grafico a torta per l'etnia
				fig = plt.figure(figsize=(10, 7))
				Etnia = ["Hispanic", "Other", "Black", "Asian", "White"]
				data_etnia = [num_Hispanic, num_Other, num_Black, num_Asian, num_White]
				plt.pie(data_etnia, labels=Etnia, autopct='%1.1f%%')
				plt.title("Distribuzione per Etnia")
				plt.show()
				
				# Crea il grafico a torta per la paga
				fig = plt.figure(figsize=(10, 7))
				Zone = ["Zone A", "Zone B", "Zone C"]
				data_zona = [num_zona_A,num_zona_B,num_zona_C]
				plt.pie(data_zona, labels=Zone, autopct='%1.1f%%',textprops={'fontsize': 16})
				plt.title("Distribuzione per Paga",fontsize=16)
				plt.show()
				
				# Crea il grafico a torta la situazione familiare
				fig = plt.figure(figsize=(10, 7))
				FamSituation = ["Single", "Married", "Widowed", "Divorced"]
				data_fam = [num_single,num_married,num_widowed,num_divorced]
				plt.pie(data_fam, labels=FamSituation, autopct='%1.1f%%')
				plt.title("Distribuzione per Situazione Familiare")
				plt.show()
				
				
					
			except FileNotFoundError:
				print("File non trovato!")
			except Exception as e:
				print("Si è verificato un errore:", e)		
				
def diversity_race(file_csv, numero_manager):
					try:
						# Leggi il file CSV con il delimitatore '\t'
						with open(file_csv, 'r', newline='') as file:
							csv_reader = csv.reader(file, delimiter=',')
							intestazioni = next(csv_reader)  # Leggi le intestazioni
							
							# Converti le righe in una lista di dizionari
							dati = [dict(zip(intestazioni, riga)) for riga in csv_reader]
							
							# Filtra le righe che non contengono "MANAGER"
							dati_MANAGER = [riga for riga in dati if riga.get("Role") == "MANAGER"]
							dati_CLERK = [riga for riga in dati if riga.get("Role") != "MANAGER"]
							num_Hispanic = sum(1 for riga in dati_MANAGER if riga.get("Ethnicity") == "Hispanic")
							num_Other = sum(1 for riga in dati_MANAGER if riga.get("Ethnicity") == "Other")
							num_Black = sum(1 for riga in dati_MANAGER if riga.get("Ethnicity") == "Black")
							num_Asian = sum(1 for riga in dati_MANAGER if riga.get("Ethnicity") == "Asian")
							num_White = sum(1 for riga in dati_MANAGER if riga.get("Ethnicity") == "White")
							
							num_totale_fin = int((num_Hispanic + num_Other + num_Black + num_Asian + num_White + numero_manager) / 5)
							num_hispanic_new = num_totale_fin - num_Hispanic    
							num_other_new = num_totale_fin - num_Other    
							num_black_new = num_totale_fin - num_Black
							num_asian_new = num_totale_fin - num_Asian
							num_white_new = num_totale_fin - num_White
							
							dati_selezionati_hispanic = []
							dati_selezionati_other = []
							dati_selezionati_black = []
							dati_selezionati_asian = []
							dati_selezionati_white = []
							
							
							if num_hispanic_new > 0:
								dati_selezionati_hispanic = [riga for riga in dati_CLERK if riga.get("Ethnicity") == "Hispanic"]
								dati_selezionati_hispanic.sort(key=lambda x: int(x["Performance"]), reverse=True)
								dati_selezionati_hispanic = dati_selezionati_hispanic[:num_hispanic_new]
							if num_other_new > 0:
								dati_selezionati_other = [riga for riga in dati_CLERK if riga.get("Ethnicity") == "Other"]
								dati_selezionati_other.sort(key=lambda x: int(x["Performance"]), reverse=True)
								dati_selezionati_other = dati_selezionati_other[:num_other_new]
							if num_black_new > 0:
								dati_selezionati_black = [riga for riga in dati_CLERK if riga.get("Ethnicity") == "Black"]
								dati_selezionati_black.sort(key=lambda x: int(x["Performance"]), reverse=True)
								dati_selezionati_black = dati_selezionati_black[:num_black_new]
							if num_asian_new > 0:
								dati_selezionati_asian = [riga for riga in dati_CLERK if riga.get("Ethnicity") == "Asian"]
								dati_selezionati_asian.sort(key=lambda x: int(x["Performance"]), reverse=True)
								dati_selezionati_asian = dati_selezionati_asian[:num_asian_new]	
							if num_white_new > 0:
									dati_selezionati_white = [riga for riga in dati_CLERK if riga.get("Ethnicity") == "White"]
									dati_selezionati_white.sort(key=lambda x: int(x["Performance"]), reverse=True)
									dati_selezionati_white = dati_selezionati_white[:num_white_new]		
							nuovo_file_csv = "output_diversity_race.csv"
							with open(nuovo_file_csv, 'w', newline='') as file_output:
								csv_writer = csv.DictWriter(file_output, fieldnames=intestazioni)
								csv_writer.writeheader()
								
								csv_writer.writerows(dati_selezionati_hispanic)
								csv_writer.writerows(dati_selezionati_other)
								csv_writer.writerows(dati_selezionati_black)
								csv_writer.writerows(dati_selezionati_asian)
								csv_writer.writerows(dati_selezionati_white)
								csv_writer.writerows(dati_MANAGER)
								
						dati_tot = dati_selezionati_hispanic + dati_selezionati_other + dati_selezionati_black + dati_selezionati_asian + dati_selezionati_white + dati_MANAGER
						dati_candidati = dati_selezionati_hispanic + dati_selezionati_other + dati_selezionati_black + dati_selezionati_asian + dati_selezionati_white 
						num_maschi = sum(1 for riga in dati_candidati if riga.get("Gender") == "Male")
						num_femmine = sum(1 for riga in dati_candidati if riga.get("Gender") == "Female")
						
						# Calcola il numero di membri per ciascuna etnia
						num_Hispanic = sum(1 for riga in dati_candidati if riga.get("Ethnicity") == "Hispanic")
						num_Other = sum(1 for riga in dati_candidati if riga.get("Ethnicity") == "Other")
						num_Black = sum(1 for riga in dati_candidati if riga.get("Ethnicity") == "Black")
						num_Asian = sum(1 for riga in dati_candidati if riga.get("Ethnicity") == "Asian")
						num_White = sum(1 for riga in dati_candidati if riga.get("Ethnicity") == "White")
						
						#Calcolo indice performance
						num_performance_1 = sum(1 for riga in dati_tot if int(riga.get("Performance")) == 1)
						num_performance_2 = sum(1 for riga in dati_tot if int(riga.get("Performance")) == 2)
						num_performance_3 = sum(1 for riga in dati_tot if int(riga.get("Performance")) == 3)
						num_performance_4 = sum(1 for riga in dati_tot if int(riga.get("Performance")) == 4)
						num_performance_5 = sum(1 for riga in dati_tot if int(riga.get("Performance")) == 5)
						num_performance_6 = sum(1 for riga in dati_tot if int(riga.get("Performance")) == 6)
						num_performance_7 = sum(1 for riga in dati_tot if int(riga.get("Performance")) == 7)
						num_performance_8 = sum(1 for riga in dati_tot if int(riga.get("Performance")) == 8)
						num_performance_9 = sum(1 for riga in dati_tot if int(riga.get("Performance")) == 9)
						num_performance_10 = sum(1 for riga in dati_tot if int(riga.get("Performance")) == 10)
	
						
						#Calcolo il numero per paga
						num_zona_A = sum(1 for riga in dati_tot if riga.get("Salary") == "Zone A")
						num_zona_B = sum(1 for riga in dati_tot if riga.get("Salary") == "Zone B")
						num_zona_C = sum(1 for riga in dati_tot if riga.get("Salary") == "Zone C")
						
						#Calcolo il numero per situazione familiare 
						num_single = sum(1 for riga in dati_tot if riga.get("FamSituation") == "Single")
						num_married = sum(1 for riga in dati_tot if riga.get("FamSituation") == "Married")
						num_widowed = sum(1 for riga in dati_tot if riga.get("FamSituation") == "Widowed")
						num_divorced = sum(1 for riga in dati_tot if riga.get("FamSituation") == "Divorced")	
						
						
						# Estrai i valori delle performance e converti in numeri interi
						performance_values = [int(riga["Performance"]) for riga in dati_tot if "Performance" in riga and riga["Performance"].isdigit()]
						
						# Calcola la somma delle performance
						sum_performance = sum(performance_values)
						
						# Calcola il numero di valori di performance
						num_performance = len(performance_values)
						
						# Calcola la media della performance
						if num_performance > 0:
							media = sum_performance / num_performance
						else:
							media = 0
							
						
						print("Il file è stato ordinato, filtrato e salvato con successo come:", nuovo_file_csv)
						
						fig = plt.figure(figsize=(10, 7))
						gender = ["Male", "Female"]
						data_gender = [num_maschi, num_femmine]
						plt.pie(data_gender, labels=gender,autopct='%1.1f%%')
						plt.title("Distribuzione per genere")
						plt.show()
						
						index_performance = [1,2,3,4,5,6,7,8,9,10]
						data_index_performance = [num_performance_1, num_performance_2,num_performance_3,num_performance_4,num_performance_5,
							num_performance_6,num_performance_7,num_performance_8,num_performance_9,num_performance_10]
						plt.pie(data_index_performance, labels=index_performance,autopct='%1.1f%%')
						plt.title(f"Distribuzione per indice performance. \nLa media è {media:.2f}",fontsize=20)
						plt.show()
		
						# Crea il grafico a torta per l'etnia
						fig = plt.figure(figsize=(10, 7))
						Etnia = ["Hispanic", "Other", "Black", "Asian", "White"]
						data_etnia = [num_Hispanic, num_Other, num_Black, num_Asian, num_White]
						plt.pie(data_etnia, labels=Etnia, autopct='%1.1f%%',textprops={'fontsize': 16})
						plt.title("Distribuzione per Etnia",fontsize=16)
						plt.show()
		
						# Crea il grafico a torta per la paga
						fig = plt.figure(figsize=(10, 7))
						Zone = ["Zone A", "Zone B", "Zone C"]
						data_zona = [num_zona_A,num_zona_B,num_zona_C]
						plt.pie(data_zona, labels=Zone, autopct='%1.1f%%')
						plt.title("Distribuzione per Paga")
						plt.show()
		
						# Crea il grafico a torta la situazione familiare
						fig = plt.figure(figsize=(10, 7))
						FamSituation = ["Single", "Married", "Widowed", "Divorced"]
						data_fam = [num_single,num_married,num_widowed,num_divorced]
						plt.pie(data_fam, labels=FamSituation, autopct='%1.1f%%')
						plt.title("Distribuzione per Situazione Familiare")
						plt.show()
							
					except FileNotFoundError:
						print("File non trovato!")
					except Exception as e:
						print("Si è verificato un errore:", e)			
def diversity_family_situation(file_csv, numero_manager):
					try:
						# Leggi il file CSV con il delimitatore '\t'
						with open(file_csv, 'r', newline='') as file:
							csv_reader = csv.reader(file, delimiter=',')
							intestazioni = next(csv_reader)  # Leggi le intestazioni
							
							# Converti le righe in una lista di dizionari
							dati = [dict(zip(intestazioni, riga)) for riga in csv_reader]
							
							# Filtra le righe che non contengono "MANAGER"
							dati_MANAGER = [riga for riga in dati if riga.get("Role") == "MANAGER"]
							dati_CLERK = [riga for riga in dati if riga.get("Role") != "MANAGER"]
							
							num_single = sum(1 for riga in dati_MANAGER if riga.get("FamSituation") == "Single")
							num_married = sum(1 for riga in dati_MANAGER if riga.get("FamSituation") == "Married")
							num_widowed = sum(1 for riga in dati_MANAGER if riga.get("FamSituation") == "Widowed")
							num_divorced = sum(1 for riga in dati_MANAGER if riga.get("FamSituation") == "Divorced")
							
							
							num_totale_fin = int((num_single + num_married + num_widowed + num_divorced + numero_manager) / 4)
							num_single_new = num_totale_fin - num_single    
							num_married_new = num_totale_fin - num_married    
							num_widowed_new = num_totale_fin - num_widowed
							num_divorced_new = num_totale_fin - num_divorced
							
							dati_selezionati_single = []
							dati_selezionati_married = []
							dati_selezionati_widowed = []
							dati_selezionati_divorced = []
							
							if num_single_new > 0:
								dati_selezionati_single = [riga for riga in dati_CLERK if riga.get("FamSituation") == "Single"]
								dati_selezionati_single.sort(key=lambda x: int(x["Performance"]), reverse=True)
								dati_selezionati_single = dati_selezionati_single[:num_single_new]
							if num_married_new > 0:
								dati_selezionati_married = [riga for riga in dati_CLERK if riga.get("FamSituation") == "Married"]
								dati_selezionati_married.sort(key=lambda x: int(x["Performance"]), reverse=True)
								dati_selezionati_married = dati_selezionati_married[:num_married_new]
							if num_widowed_new > 0:
								dati_selezionati_widowed = [riga for riga in dati_CLERK if riga.get("FamSituation") == "Widowed"]
								dati_selezionati_widowed.sort(key=lambda x: int(x["Performance"]), reverse=True)
								dati_selezionati_widowed = dati_selezionati_widowed[:num_widowed_new]
							if num_divorced_new > 0:
								dati_selezionati_divorced = [riga for riga in dati_CLERK if riga.get("FamSituation") == "Divorced"]
								dati_selezionati_divorced.sort(key=lambda x: int(x["Performance"]), reverse=True)
								dati_selezionati_divorced = dati_selezionati_divorced[:num_divorced_new]	
								
							nuovo_file_csv = "output_diversity_family_situation.csv"
							
							with open(nuovo_file_csv, 'w', newline='') as file_output:
								csv_writer = csv.DictWriter(file_output, fieldnames=intestazioni)
								csv_writer.writeheader()
								
								csv_writer.writerows(dati_selezionati_single)
								csv_writer.writerows(dati_selezionati_married)
								csv_writer.writerows(dati_selezionati_widowed)
								csv_writer.writerows(dati_selezionati_divorced)
								csv_writer.writerows(dati_MANAGER)
						dati_tot = dati_selezionati_single + dati_selezionati_married + dati_selezionati_widowed + dati_selezionati_divorced  + dati_MANAGER
						dati_candidati = dati_selezionati_single + dati_selezionati_married + dati_selezionati_widowed + dati_selezionati_divorced
						num_maschi = sum(1 for riga in dati_candidati if riga.get("Gender") == "Male")
						num_femmine = sum(1 for riga in dati_candidati if riga.get("Gender") == "Female")
						
						# Calcola il numero di membri per ciascuna etnia
						num_Hispanic = sum(1 for riga in dati_tot if riga.get("Ethnicity") == "Hispanic")
						num_Other = sum(1 for riga in dati_tot if riga.get("Ethnicity") == "Other")
						num_Black = sum(1 for riga in dati_tot if riga.get("Ethnicity") == "Black")
						num_Asian = sum(1 for riga in dati_tot if riga.get("Ethnicity") == "Asian")
						num_White = sum(1 for riga in dati_tot if riga.get("Ethnicity") == "White")
						
						#Calcolo il numero per paga
						num_zona_A = sum(1 for riga in dati_tot if riga.get("Salary") == "Zone A")
						num_zona_B = sum(1 for riga in dati_tot if riga.get("Salary") == "Zone B")
						num_zona_C = sum(1 for riga in dati_tot if riga.get("Salary") == "Zone C")
						
						#Calcolo il numero per situazione familiare 
						num_single = sum(1 for riga in dati_candidati if riga.get("FamSituation") == "Single")
						num_married = sum(1 for riga in dati_candidati if riga.get("FamSituation") == "Married")
						num_widowed = sum(1 for riga in dati_candidati if riga.get("FamSituation") == "Widowed")
						num_divorced = sum(1 for riga in dati_candidati if riga.get("FamSituation") == "Divorced")	
						
						#Calcolo indice performance
						num_performance_1 = sum(1 for riga in dati_tot if int(riga.get("Performance")) == 1)
						num_performance_2 = sum(1 for riga in dati_tot if int(riga.get("Performance")) == 2)
						num_performance_3 = sum(1 for riga in dati_tot if int(riga.get("Performance")) == 3)
						num_performance_4 = sum(1 for riga in dati_tot if int(riga.get("Performance")) == 4)
						num_performance_5 = sum(1 for riga in dati_tot if int(riga.get("Performance")) == 5)
						num_performance_6 = sum(1 for riga in dati_tot if int(riga.get("Performance")) == 6)
						num_performance_7 = sum(1 for riga in dati_tot if int(riga.get("Performance")) == 7)
						num_performance_8 = sum(1 for riga in dati_tot if int(riga.get("Performance")) == 8)
						num_performance_9 = sum(1 for riga in dati_tot if int(riga.get("Performance")) == 9)
						num_performance_10 = sum(1 for riga in dati_tot if int(riga.get("Performance")) == 10)
						
						# Estrai i valori delle performance e converti in numeri interi
						performance_values = [int(riga["Performance"]) for riga in dati_tot if "Performance" in riga and riga["Performance"].isdigit()]
						
						# Calcola la somma delle performance
						sum_performance = sum(performance_values)
						
						# Calcola il numero di valori di performance
						num_performance = len(performance_values)
						
						# Calcola la media della performance
						if num_performance > 0:
							media = sum_performance / num_performance
						else:
							media = 0
							
						print("Il file è stato ordinato, filtrato e salvato con successo come:", nuovo_file_csv)
						fig = plt.figure(figsize=(10, 7))
						gender = ["Male", "Female"]
						data_gender = [num_maschi, num_femmine]
						plt.pie(data_gender, labels=gender,autopct='%1.1f%%')
						plt.title("Distribuzione per genere")
						plt.show()
						
						index_performance = [1,2,3,4,5,6,7,8,9,10]
						data_index_performance = [num_performance_1, num_performance_2,num_performance_3,num_performance_4,num_performance_5,
							num_performance_6,num_performance_7,num_performance_8,num_performance_9,num_performance_10]
						plt.pie(data_index_performance, labels=index_performance,autopct='%1.1f%%',textprops={'fontsize': 16})
						plt.title(f"Distribuzione per indice performance. \nLa media è {media:.2f}",fontsize=20)
						plt.show()
						
						
						# Crea il grafico a torta per l'etnia
						fig = plt.figure(figsize=(10, 7))
						Etnia = ["Hispanic", "Other", "Black", "Asian", "White"]
						data_etnia = [num_Hispanic, num_Other, num_Black, num_Asian, num_White]
						plt.pie(data_etnia, labels=Etnia, autopct='%1.1f%%')
						plt.title("Distribuzione per Etnia")
						plt.show()
						
						# Crea il grafico a torta per la paga
						fig = plt.figure(figsize=(10, 7))
						Zone = ["Zone A", "Zone B", "Zone C"]
						data_zona = [num_zona_A,num_zona_B,num_zona_C]
						plt.pie(data_zona, labels=Zone, autopct='%1.1f%%')
						plt.title("Distribuzione per Paga")
						plt.show()
						
						# Crea il grafico a torta la situazione familiare
						fig = plt.figure(figsize=(10, 7))
						FamSituation = ["Single", "Married", "Widowed", "Divorced"]
						data_fam = [num_single,num_married,num_widowed,num_divorced]
						plt.pie(data_fam, labels=FamSituation, autopct='%1.1f%%',textprops={'fontsize': 16})
						plt.title("Distribuzione per Situazione Familiare",fontsize=16)
						plt.show()
						
						
					except FileNotFoundError:
						print("File non trovato!")
					except Exception as e:
						print("Si è verificato un errore:", e)			
def equity_gender(file_csv, numero_manager):
							import csv
	
							try:
								# Leggi il file CSV con il delimitatore ','
								with open(file_csv, 'r', newline='') as file:
									csv_reader = csv.reader(file, delimiter=',')
									intestazioni = next(csv_reader)  # Leggi le intestazioni
									
									# Converti le righe in una lista di dizionari
									dati = [dict(zip(intestazioni, riga)) for riga in csv_reader]
									dati_MANAGER = [riga for riga in dati if riga.get("Role") == "MANAGER"]
									dati_CLERK = [riga for riga in dati if riga.get("Role") != "MANAGER"]
									
									num_male = sum(1 for riga in dati_CLERK if riga.get("Gender") == "Male")
									num_female = sum(1 for riga in dati_CLERK if riga.get("Gender") == "Female")
									
									dati_filtrati = [riga for riga in dati if riga.get("Role") != "MANAGER" and riga.get("Gender") == "Female"]
									dati_filtrati.sort(key=lambda x: int(x["Performance"]), reverse=True)
									
									if num_male > num_female:
										totale = num_male + num_female
										x = totale / (2 * num_female)
										N = int((x * num_female) - num_female)
									else:
										totale = num_male + num_female
										x = totale / (2 * num_male)
										N = int((x * num_male) - num_male)
									# Identifica le righe da duplicare
									rows_to_duplicate = []
									count = 0
									
									for idx, row in enumerate(dati_CLERK):
										if num_male > num_female:
											if row['Gender'] == "Female" and row['Role'] == "CLERK":
												rows_to_duplicate.append(row)
												count += 1
										else:
											if row['Gender'] == "Male" and row['Role'] == "CLERK":
												rows_to_duplicate.append(row)
												count += 1
										if count == N:
											break
									datiConDoppioni = dati_CLERK + rows_to_duplicate
									datiConDoppioni.sort(key=lambda x: int(x["Performance"]), reverse=True)
					
	
									# Dividi il dataset in gruppi basati sulla performance
									gruppi_performance = {}
									for row in datiConDoppioni:
										performance = int(row["Performance"])
										if performance not in gruppi_performance:
											gruppi_performance[performance] = []
										gruppi_performance[performance].append(row)
										
									# Mescola casualmente le righe all'interno di ciascun gruppo
									for performance in gruppi_performance:
										random.shuffle(gruppi_performance[performance])
										
									# Ricombina i gruppi mantenendo l'ordine delle performance
									datiConDoppioni_ordinati = []
									for performance in sorted(gruppi_performance.keys(), reverse=True):
										datiConDoppioni_ordinati.extend(gruppi_performance[performance])
										
						
										
									current_index = 0
									datiOutput = []
									pID_set = set()
									
									while len(datiOutput) < numero_manager and current_index < len(datiConDoppioni_ordinati):
										row = datiConDoppioni_ordinati[current_index]
										if row['pID'] not in pID_set:
											datiOutput.append(row)
											pID_set.add(row['pID'])
										current_index += 1
										
								nuovo_file_csv = "output_equity_gender.csv"
								with open(nuovo_file_csv, 'w', newline='') as file_output:
									csv_writer = csv.DictWriter(file_output, fieldnames=intestazioni)
									csv_writer.writeheader()
									csv_writer.writerows(datiOutput)
									
								print("Il file è stato ordinato, filtrato e salvato con successo come:", nuovo_file_csv)
								dati_tot = dati_MANAGER + datiOutput
								
								#Calcolo indice performance
								num_performance_1 = sum(1 for riga in dati_tot if int(riga.get("Performance")) == 1)
								num_performance_2 = sum(1 for riga in dati_tot if int(riga.get("Performance")) == 2)
								num_performance_3 = sum(1 for riga in dati_tot if int(riga.get("Performance")) == 3)
								num_performance_4 = sum(1 for riga in dati_tot if int(riga.get("Performance")) == 4)
								num_performance_5 = sum(1 for riga in dati_tot if int(riga.get("Performance")) == 5)
								num_performance_6 = sum(1 for riga in dati_tot if int(riga.get("Performance")) == 6)
								num_performance_7 = sum(1 for riga in dati_tot if int(riga.get("Performance")) == 7)
								num_performance_8 = sum(1 for riga in dati_tot if int(riga.get("Performance")) == 8)
								num_performance_9 = sum(1 for riga in dati_tot if int(riga.get("Performance")) == 9)
								num_performance_10 = sum(1 for riga in dati_tot if int(riga.get("Performance")) == 10)
								index_performance = [1,2,3,4,5,6,7,8,9,10]
								data_index_performance = [num_performance_1, num_performance_2,num_performance_3,num_performance_4,num_performance_5,
									num_performance_6,num_performance_7,num_performance_8,num_performance_9,num_performance_10]
								# Estrai i valori delle performance e converti in numeri interi
								performance_values = [int(riga["Performance"]) for riga in dati_tot if "Performance" in riga and riga["Performance"].isdigit()]
								
								# Calcola la somma delle performance
								sum_performance = sum(performance_values)
								
								# Calcola il numero di valori di performance
								num_performance = len(performance_values)
								
								# Calcola la media della performance
								if num_performance > 0:
									media = sum_performance / num_performance
								else:
									media = 0
									
								plt.pie(data_index_performance, labels=index_performance,autopct='%1.1f%%',textprops={'fontsize': 16})
								plt.title(f"Distribuzione per indice performance. \nLa media è {media:.2f}",fontsize=20)
								plt.show()
								num_maschi = sum(1 for riga in datiOutput if riga.get("Gender") == "Male")
								num_femmine = sum(1 for riga in datiOutput if riga.get("Gender") == "Female")
								fig = plt.figure(figsize=(10, 7))
								gender = ["Male", "Female"]
								data_gender = [num_maschi, num_femmine]
								plt.pie(data_gender, labels=gender,autopct='%1.1f%%',textprops={'fontsize': 16})
								plt.title("Distribuzione per genere",fontsize=16)
								plt.show()
								
							except FileNotFoundError:
								print("File non trovato!")
							except Exception as e:
								print("Si è verificato un errore:", e)
								
def scelta_manager(scelta_dimension, scelta_attribute, numero_manager):
	if scelta_dimension == 1:  # Equality
		equality(File, numero_manager)
	elif scelta_dimension == 2:  # Equity
		if scelta_attribute == 1:  # Salary
			equity_gender(File, numero_manager)
		elif scelta_attribute == 2:  # Gender
			equity_gender(File, numero_manager)
		elif scelta_attribute == 3:  # Family Situation
			equity_gender(File, numero_manager)
		elif scelta_attribute == 4:  # Ethnicity
			equity_gender(File, numero_manager)
	elif scelta_dimension == 3:  # Diversity
		if scelta_attribute == 1:  # Salary
			diversity_salary(File, numero_manager)
		elif scelta_attribute == 2:  # Gender
			diversity_gender(File, numero_manager)
		elif scelta_attribute == 3:  # Family Situation
			diversity_family_situation(File, numero_manager)
		elif scelta_attribute == 4:  # Ethnicity
			diversity_race(File, numero_manager)
	
	
print("Ethical dimension disponibili:")
print("1. Equality")
print("2. Equity")
print("3. Diversity")

scelta_dimension = int(input("Che Ethical Dimension vuoi? Inserisci il numero corrispondente: "))

print("Affected Attribute disponibili:")
print("1. Salary")
print("2. Gender")
print("3. Family situation")
print("4. Ethnicity")

scelta_attribute = int(input("Che Affected Attribute vuoi? Inserisci il numero corrispondente: "))


numero_manager = int(input("Quanti CLERK vuoi promuovere a manager? "))
scelta_manager(scelta_dimension,scelta_attribute,numero_manager)
#start_situation_manager(File)
#update_performance(File)
#start_situation_clerk(File)