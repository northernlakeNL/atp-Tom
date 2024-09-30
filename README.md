# atp-Tom

Voor ATP was de opdracht om decorators te maken.
Ik heb gekozen om de decorators te koppelen aan dummy classen voor de chips die ik wil gebruiken voor mijn eind opdracht, hierdoor kan ik de decorators ook daarvoor gebruiken.

## decorators uitleg
Voor de opdracht heb ik in totaal vier decorators geschreven:
- timing decorator
- logging decorator
- caching decorator
- measurement converting decorator

### timing decorator
De timing decorator vind ik van belang voor het testen van het systeem, door een timing decorator te gebruiken kan er gekeken worden hoelang het duurt voor de functies van de sensoren een waarden terug geven. Later is deze decorator ook te gebruiken om te kijken hoe lang het systeem doet over een complete meting en het aansturen van de actuatoren zodat die tijd kan worden mee genomen voor eventuele incrementele metingen.

### logging decorator
De loging decorator vind ik van belang om te kunnen testen of de functies correct worden uitgevoerd met de verwachtte waarden, mocht dit niet zo zijn kan er sneller actie ondernomen worden om dit te herstellen.

### caching decorator
De caching decorator vind ik handig om tijd te besparen voor de complete berekening van de meting, als de waarde al bekend is kan deze gelijk worden gestuurd. Mocht er dus een grote functie komen waarbij veel tijd in beslag wordt genomen voor de berekening, kan met de cache worden gekeken of dezelfde waarde niet al een keer is gemeten.

### Measurement Converting decorator
De measurement converting decorator is handig voor als het project ook gebruikt gaat worden door mensen die niet bekend zijn met de gebruikte eenheid of als er voor andere redenen met een andere eenheid moet worden gerekend.