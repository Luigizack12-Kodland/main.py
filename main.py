meme_dict = {
            "CRINGE": "Qualcosa di eccezionalmente strano o imbarazzante",
            "LOL": "Una risposta comune a qualcosa di divertente",
            "CLAPPARE": "Quando in un gioco sparatutto si uccide un nemico",
            "GG": "Esultanza per quando si vince in un gioco o per congratulare qualcuno",
            "CREEPY":"spaventoso, inquietante"
            }

parola = input("Scrivi una parola che non capisci (usa solo lettere maiuscole!): ")

if parola in meme_dict.keys():
    print(meme_dict[parola])
else:
    print("Non posso aiutarti, mi dispiace")
