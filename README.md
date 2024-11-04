# ATP opdracht Tom
Door main.py uit te voeren worden eerst de tests uitgevoerd, hierna wordt er 10 seconden gewacht om de simulatie te laten zien.

#### test resultaten locatie
De test resultaten staan in het log bestand [test_results.log](code/test_results.log).

#### test verslag locatie
Het test verslag staat in het [test_report](code/test_report.md).

## test uitleg
De tests die ik heb uitgevoerd zijn 
- [Unit test](#unit-test) 
- [Software Integratie Test](#software-integratie-test)
- [System Test](#system-test).

De tests worden gedaan om te controlleren of het systeem binnen een acceptabele tijd de juiste stappen zet om het systeem functioneel te laten werken.

### Unit test
De code voor de unit tests bevat tijdmetingen om de uitvoeringstijd van het systeem te meten. Ook zijn er verschillende controlles op het controlleren of een bepaalde waarde boven of onder de Threshold valt. Dit wordt gedaan om te controlleren of de drempelwaarden correct worden behouden en dat de code binnen een acceptabele tijd wordt uitgevoerd.

De code hiervoor is te vinden in [tests.py](code/tests.py) in de klasse ```UnitTest```.

### Software Integratie test
De code voor de Software Integratie tests bevat verifiëring voor het systeem om correct te reageren op verschillende sensorwaarden. Na het ontvangen voor de juiste waard de Fan of de Vernevelaar worden ingeschakelt. Dit allemaal moet ook binnen een bepaalde tijd gebeuren aangezien anders het klimaat negatieve impact kan hebben op de omgeving.

De code hiervoor is te vinden in [tests.py](code/tests.py) in de klasse ```IntegrationTest```.

### System test
De code voor de system tests bevat simulaties van waarden die worden gemeten om te controlleren of het systeem of het systeem correct reageert op verschillende sensor waarden.

De code hiervoor is te vinden in [tests.py](code/tests.py) in de klasse ```SystemTest```.


## Simmulatie
Er is een kleine simmulatie van lichtintensiteit en luchtvochtigheid om te zien dat de actuatoren theoretisch geactiveert worden bij het overschrijden van bepaalde waarden. De waarden worden hierdoor ook aangepast om alleen omhoog of omlaag te gaan.
Als de actuatoren niet aan staan fluctueren de waarden.

De code hiervoor is te vinden in [sim.py](code/sim.py)