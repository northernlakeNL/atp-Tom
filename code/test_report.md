# Test Report
## uitgevoerde tests
- Unit test: Het testen van de threshold.
- System test: Het testen van het gedrag van het systeem.
- Integration test: Het testen van de interactie tussen sensoren en acutatoren.
## verwachtingen
In de tests verwacht ik dat alles naar behoren werkt en ver binnen de tijdslimiet zal vallen, de code is niet al te ingewikkeld.
Er zou zo ver ik zie geen reden zijn om er langer dan, maximaal, een paar seconde voor nodig te hebben om de code uit te voeren.
## Test resultaten
| Datum en tijd test | Test Naam | Uitvoeringstijd (seconden) |
|--------------------|-----------|----------------------------|
| 2024-11-04 19:24:23,939 | hoge humidity test | 0.0 seconde |
| 2024-11-04 19:24:23,942 | licht test is | 0.001003265380859375 seconde |
| 2024-11-04 19:24:23,944 | lage humidity test | 0.0010082721710205078 seconde |
| 2024-11-04 19:24:23,950 | Threshold test | 0.0 seconde |
| 2024-11-04 19:24:23,957 | Humidity integration test (Fan) | 0.0 seconde |
| 2024-11-04 19:24:23,961 | Humidity integration test (humidifier) | 0.0009996891021728516 seconde |
| 2024-11-04 19:24:23,963 | Light integration test | 0.0 seconde |
| 2024-11-04 19:25:34,867 | hoge humidity test | 0.0009999275207519531 seconde |
| 2024-11-04 19:25:34,873 | licht test is | 0.0010082721710205078 seconde |
| 2024-11-04 19:25:34,879 | lage humidity test | 0.0020003318786621094 seconde |
| 2024-11-04 19:25:34,879 | Threshold test | 0.0 seconde |
| 2024-11-04 19:25:34,988 | Humidity integration test (Fan) | 0.10600590705871582 seconde |
| 2024-11-04 19:25:34,993 | Humidity integration test (humidifier) | 0.0009448528289794922 seconde |
| 2024-11-04 19:25:34,997 | Light integration test | 0.0009045600891113281 seconde |
| 2024-11-04 19:26:25,172 | hoge humidity test | 0.0009982585906982422 seconde |
| 2024-11-04 19:26:25,176 | licht test is | 0.0011119842529296875 seconde |
| 2024-11-04 19:26:25,178 | lage humidity test | 0.000997304916381836 seconde |
| 2024-11-04 19:26:25,178 | Threshold test | 0.0 seconde |
| 2024-11-04 19:26:25,183 | Humidity integration test (Fan) | 0.0 seconde |
| 2024-11-04 19:26:25,190 | Humidity integration test (humidifier) | 0.0036134719848632812 seconde |
| 2024-11-04 19:26:25,193 | Light integration test | 0.0009047985076904297 seconde |
| 2024-11-04 19:26:56,800 | hoge humidity test | 0.001058340072631836 seconde |
| 2024-11-04 19:26:56,802 | licht test is | 0.0 seconde |
| 2024-11-04 19:26:56,806 | lage humidity test | 0.0018002986907958984 seconde |
| 2024-11-04 19:26:56,807 | Threshold test | 0.0 seconde |
| 2024-11-04 19:26:56,810 | Humidity integration test (Fan) | 0.0010006427764892578 seconde |
| 2024-11-04 19:26:56,813 | Humidity integration test (humidifier) | 0.0009465217590332031 seconde |
| 2024-11-04 19:26:56,816 | Light integration test | 0.0010509490966796875 seconde |
| 2024-11-04 19:27:18,094 | hoge humidity test | 0.0010001659393310547 seconde |
| 2024-11-04 19:27:18,098 | licht test is | 0.0009989738464355469 seconde |
| 2024-11-04 19:27:18,101 | lage humidity test | 0.0010001659393310547 seconde |
| 2024-11-04 19:27:18,101 | Threshold test | 0.0 seconde |
| 2024-11-04 19:27:18,104 | Humidity integration test (Fan) | 0.0010008811950683594 seconde |
| 2024-11-04 19:27:18,108 | Humidity integration test (humidifier) | 0.0010128021240234375 seconde |
| 2024-11-04 19:27:18,110 | Light integration test | 0.0 seconde |

## Kwaliteitsimpact
1. Betrouwbaarheid: De tests zijn betrouwbaar doordat de thresholds juist zijn geverifieerd.
2. Prestaties: De tests worden uitgevoerd binnen 10 seconden.
3. Onderhoudbaarheid: Het systeem is gemakkelijk uit te breiden voor meerdere sensoren/actuatoren.

## Conclusie
De tests zijn succesvol uitgevoerd en de kwaliteit van het systeem is gewaarborgd.
