def carica_da_file(file_path):
    """Carica i libri dal file"""
    try:
        tabella=[]
        infile = open(file_path, 'r')
        for line in infile:
            row = (line.strip()).split(',')
            tabella.append(row)
        return(tabella)

    except FileNotFoundError:
        print("none")

def aggiungi_libro(biblioteca, titolo, autore, anno, pagine, sezione, file_path):
    """Aggiunge un libro nella biblioteca"""

    try:
        with open(file_path, 'a') as outfile:
            print(f"{titolo}, {autore}, {anno}, {pagine}, {sezione}", file=outfile)
            row = [titolo, autore, str(anno), str(pagine), str(sezione)]
            biblioteca.append(row)
            return(row)

    except FileNotFoundError:
        print("none")

def cerca_libro(biblioteca, titolo):
    """Cerca un libro nella biblioteca dato il titolo"""

    for row in biblioteca:
        if row[0].lower()== titolo.lower():
            return(row)
    return None

def elenco_libri_sezione_per_titolo(biblioteca, sezione):
    """Ordina i titoli di una data sezione della biblioteca in ordine alfabetico"""
    # TODO
    #tabella = [row[0] for row in biblioteca if int(row[-1]) == sezione]
    #tabella.sort(key=str.lower)
    #return tabella
    tabella=[]
    for row in biblioteca:
        if int(row[-1]) == sezione:
           tabella.append(row[0])
    if tabella==[]:
        return None
    else:
        tabella.sort(key=str.lower)
        return tabella

def main():
    biblioteca = []
    file_path = "biblioteca.csv"

    while True:
        print("\n--- MENU BIBLIOTECA ---")
        print("1. Carica biblioteca da file")
        print("2. Aggiungi un nuovo libro")
        print("3. Cerca un libro per titolo")
        print("4. Ordina titoli di una sezione")
        print("5. Esci")

        scelta = input("Scegli un'opzione >> ").strip()

        if scelta == "1":
            while True:
                file_path = input("Inserisci il path del file da caricare: ").strip()
                biblioteca = carica_da_file(file_path)
                if biblioteca is not None:
                    break

        elif scelta == "2":
            if not biblioteca:
                print("Prima carica la biblioteca da file.")
                continue

            titolo = input("Titolo del libro: ").strip()
            autore = input("Autore: ").strip()
            try:
                anno = int(input("Anno di pubblicazione: ").strip())
                pagine = int(input("Numero di pagine: ").strip())
                sezione = int(input("Sezione: ").strip())
            except ValueError:
                print("Errore: inserire valori numerici validi per anno, pagine e sezione.")
                continue

            libro = aggiungi_libro(biblioteca, titolo, autore, anno, pagine, sezione, file_path)
            if libro:
                print(f"Libro aggiunto con successo!")
            else:
                print("Non è stato possibile aggiungere il libro.")

        elif scelta == "3":
            if not biblioteca:
                print("La biblioteca è vuota.")
                continue

            titolo = input("Inserisci il titolo del libro da cercare: ").strip()
            risultato = cerca_libro(biblioteca, titolo)
            if risultato:
                print(f"Libro trovato: {risultato}")
            else:
                print("Libro non trovato.")

        elif scelta == "4":
            if not biblioteca:
                print("La biblioteca è vuota.")
                continue

            try:
                sezione = int(input("Inserisci numero della sezione da ordinare: ").strip())
            except ValueError:
                print("Errore: inserire un valore numerico valido.")
                continue

            titoli = elenco_libri_sezione_per_titolo(biblioteca, sezione)
            if titoli is not None:
                print(f'\nSezione {sezione} ordinata:')
                print("\n".join([f"- {titolo}" for titolo in titoli]))

        elif scelta == "5":
            print("Uscita dal programma...")
            break
        else:
            print("Opzione non valida. Riprova.")

if __name__ == "__main__":
    main()

