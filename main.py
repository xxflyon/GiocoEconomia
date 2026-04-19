import random 
print ("Benvenuto in questo gioco di vita economica.")
euro = 0
fame = 10
costo_spesa = 40
FAME_MASSIMA = 10
FAME_MINIMA = 0
grano = 0
prezzo_grano = 15

print ("--------------------------------------------------")
while True:
    

    print("---- Stato Attuale ----")
    print(f"Euro: {euro}")
    print(f"Fame: {fame}")
    print(f"Grano: {grano}")
    print(f"Prezzo del grano: {prezzo_grano}")
    print("--------------------------------------------------")
    print ("Quale azione scegli?")
    print("1. Vai a lavorare, guadagni 110 euro.")
    print("2. investi in borsa costa 50 euro, guadagno casuale. ")
    print(f"3. Vai a fare spesa,costo di {costo_spesa} euro.")
    print("4. Compra grano, costa 15 euro per unità.")
    print("5. Vendi grano, guadagni 15 euro per ogni unità.")
    print("6. Esci dal gioco.")

    

    scelta = input ("Inserisci uno dei seguenti numeri (1, 2, 3, 4, 5, 6.): ")
    print ("------------------------------------------")

    fame -= 1

    if scelta == "1":
        euro += 110
        print("Hai guadagnato 110 euro.")

    elif scelta == "2":
        costo_investimento = 50
        if euro >= costo_investimento:
            euro -= costo_investimento
            print ("Hai investito 50 euro in azioni...")
            probabilità = random.randint(1, 100)
            if probabilità <= 20:
                print ("L'investimento è andato male! Hai perso 20 euro")
                euro -= 20
            elif probabilità <=80:
                guadagno = random.randint(50, 80)
                euro += guadagno
                print(f"L'investimento è andato bene, hai guadagnato {guadagno} euro.")
            else:
                guadagno = random.randint(90, 150)
                euro += guadagno
                print (f"L'investimento ha avuto un gran successo, hai guadagnato {guadagno} euro. ")
        else:
            print ("Non hai abbastanza soldi per investire, ti servono 50 euro.")
    elif scelta == "3":
        if euro >= costo_spesa:
            euro -= costo_spesa
            fame += 3
            print ("Sei andato a fare la spesa, hai speso 40 euro e ti sei ristorato di 2 punti fame .")
        if fame > 10:
            fame = FAME_MASSIMA
            print ("Sei andato a fare la spesa, hai speso 40 euro e ti sei ristorato di 2 punti fame .")
        if euro < costo_spesa:
           print(f"Non hai abbastanza soldi per fare la spesa. Hai bisogno di {costo_spesa} euro") 
    elif scelta == "4":
        try:
            quantità_valuta = int(input(f"Quante unità di grano vuoi comprare (costo {prezzo_grano} per unità)?"))
            if quantità_valuta <= 0 :
               print ("Devi comprare almeno 1 unità di grano.")
            else:
               costo_totale = quantità_valuta * prezzo_grano
            if euro >= costo_totale:
               euro -= costo_totale
               grano += quantità_valuta
               print(f"Hai comprato{quantità_valuta} unità di grano per {costo_totale} euro.")
            else:
               print (f"Non hai abbastanza soldi. Ti servono {costo_totale} soldi per comprare {quantità_valuta} euro.")
        except ValueError:
            print ("Quantità non valida. inserisci un numero per la quantità.")

    elif scelta == "5":
        if grano >= 1:
            euro += prezzo_grano
            grano -= 1
            print(f"Hai venduto un' unità di grano per {prezzo_grano} euro.")
        else:
            print("Non hai grano da vendere.")
    elif scelta == "6":
        print ("Uscita dal gioco. Arrivederci!")
        break
    else: 
        print (" Scelta non valida. Per favore inserisci una delle seguenti opzioni")
    if fame <= 0:
        print ("Il gioco è finito, perchè sei morto di fame.")
        break
    
print("Il gioco è terminato.")