import time

m = {
            "CRINGE": "Qualcosa di eccezionalmente strano o imbarazzante",
            "LOL": "Una risposta comune a qualcosa di divertente",
            "SHEESH": "leggera disapprovazione",
            "CREEPY":"spaventoso, inquietante",
            "PARA":"preoccuparsi per qualcosa, paranoiarsi"
            }

print("Ciao, ecco il computer per i boomer! ")
time.sleep(1)

while True:
    parola = str(input("Scrivi una parola che non capisci: "))
    if parola.upper() in m:
        print(m[parola.upper()])
        print("\n")
        time.sleep(1)
