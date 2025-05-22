# Template per il progetto di programmazione web
Scarica il progetto con il seguente comando:
```bash
git clone git@github.com:danielepintore/unica_progetto_programmazione_web.git progetto_web
cd progetto_web
```
Una volta scaricato entra nella cartella del progetto dove troverai delle
sottocartelle contenenti dei template utili per iniziare lo sviluppo del
progetto. Ecco una lista delle principali cartelle e a cosa servono.

## application
In questa cartella è contenuto il codice sorgente del front-end che per ora è
un'applicazione react. Puoi vederla entrando nellla cartella: `cd application` e
digitando: `npm install --force && npm run dev`

## models
In questa cartella sono contenuti tutti i modelli di dati che vengono utilizzati
dalla nostra applicazione

## router
In questa cartella vengono definiti tutte le routes (endpoint) dell'applicazione

## data
In questa cartella è definita l'istanza del database con le varie funzioni
helper es: popolamento del database con dati fittizi)

# Come eseguirlo
Per far partire il server è presente un Makefile che semplifica il tutto. Al
primo avvio è neccessario digitare il seguente comando:
```bash
make venv install
```
Questo comando genera il virtual environment e installa le varie dipendenze, poi
per i successivi avvii basta digitare:
```bash
make run
```
