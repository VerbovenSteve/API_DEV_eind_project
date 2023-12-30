# Basisproject API Development
## Thema

Voor mijn project heb ik gekozen voor Star Wars:

Star Wars is een franchise waar ik zelf gepassioneerd over ben.
Het universum, de personages, en de verhalen boeien me enorm.
Hierdoor is het werken aan een project binnen dit thema niet alleen een professionele uidaging, maar ook een kans om te werken met iets waar ik graag met bezig ben.
Binnen de Star Wars-wereld is er een breed scala van entiteiten zoals films, personages en starships maar ook enorm veel collectors items of speelgoed.
Dit biedt me de kans om met iets gevarieerd te werken en waar ook zeer veel uitbreidingsmogelijkheden inzitten.

## Werking API

Als basis voor mijn API heb ik een Sqlite-databank gebruikt.
In de databank zitten 4 tabellen: 
1. Films
2. Persons
3. Starships
4. users

In mijn databank kan je een user aanmaken deze is word geauthenticeerd en met deze user kan je inloggen om zowel de users als alle films met de acteurs en startships te kunnen opvragen van de databank. Daarnaast aangezien Star Wars enorm veelzijdig is heb ik er voor gekozen dat iedereen bij kan dragen aan het toevoegen van films, acteurs of starships. Er komen zoveel acteurs in films voor en starships dat het bijna onmogelijk is alles te kunnen toevoegen. Dit is dan ook de grootste reden dat ik voor dit onderwerp heb gekozen. Er komen nog steeds series, animatie films van Star Wars uit deze kunnen ook toegevoegd worden aan de films bij wijze van afwisseling.

![image](https://github.com/VerbovenSteve/API_DEV_eind_project/assets/113888137/379359c5-f749-4595-a791-277fc9f572b2)

### link naar API:

https://star-wars-api-verbovensteve.cloud.okteto.net/docs 

## OpenAPI 
### screenshot van de api in OpenAPI
![image](https://github.com/VerbovenSteve/API_DEV_eind_project/assets/113888137/f2f1d57e-1e7f-4b19-a588-f73b03e92252)


In het volgende deel zal ik alle functies laten zien van de interface.
> we beginnen bij de post requests. Dit wil zeggen het opvullen van de verschillende tabellen

## postman screenshots en uitleg
## post 

### post /films

Deze post zal zorgen dat we een film in de databank kunnen zetten
![image](https://github.com/VerbovenSteve/API_DEV_eind_project/assets/113888137/9f276062-415d-4202-bbcc-54b7d2e790be)


### Error handeling post /films

Als een film al bestaat in de database dan zal bij het opnieuw toevoegen een error komen. deze zal als volgt eruit zien.
![image](https://github.com/VerbovenSteve/API_DEV_eind_project/assets/113888137/73a9c429-665b-464c-b39a-6bb947459f20)



### post /persons

Deze post zorgt ervoor dat we een personage kunnen toevoegen aan een bepaald film id.
![image](https://github.com/VerbovenSteve/API_DEV_eind_project/assets/113888137/ba52a6ff-040f-498e-b3dd-30900261b9ce)


### Error handeling post /persons

Als een personage al in de database bestaat zal er een error komen deze ziet er uit als volgt.
![image](https://github.com/VerbovenSteve/API_DEV_eind_project/assets/113888137/beacb627-4411-4843-b47f-3222980aa3e1)




### post /starships

Deze post zal starships toevoegen aan een film via de film id.
![image](https://github.com/VerbovenSteve/API_DEV_eind_project/assets/113888137/958b0abe-2f0b-4da3-baaf-4962f34f8129)


### Error handeling post /starships

Als er een bepaald starship al in de database staat dan zal er een error gegenereerd worden deze ziet er als volgt uit.
![image](https://github.com/VerbovenSteve/API_DEV_eind_project/assets/113888137/11fe9813-f580-45f6-aa05-e2e434ecd6fa)



> we zullen nu verder gaan met de get requests. Dit wil zeggen dat we verschillende items uit de tabellen gaan halen.

## get

### get /films

Deze get request zal ervoor zorgen dat we alle films in de database kunnen ophalen.
![image](https://github.com/VerbovenSteve/API_DEV_eind_project/assets/113888137/0fb6fc1b-2051-4b6f-b306-dcd5785177c1)


### Error handeling get /films

Als we een film gaan zoeken met een id dat niet in de database te vinden is krijgen we een error.
![image](https://github.com/VerbovenSteve/API_DEV_eind_project/assets/113888137/4a608a49-18c4-4363-840c-503527ea7529)



### get /persons/

Deze request zal de persoon bij naam zoeken en uit de database ophalen.
![image](https://github.com/VerbovenSteve/API_DEV_eind_project/assets/113888137/abc9550d-7117-4af3-8ad0-c391903c98d6)



### get /starships

Deze request haalt alle starships uit de database.
![image](https://github.com/VerbovenSteve/API_DEV_eind_project/assets/113888137/2e859287-cddc-4c7b-b49d-694771801f27)


### Error handeling starships

Als je verkeerde skip en limit ingeeft voor de id van de starship krijg je een error.
![image](https://github.com/VerbovenSteve/API_DEV_eind_project/assets/113888137/fc051508-61b1-467a-81c5-a5b2e9225a3e)



### get /films/all_with_characters_starships

Deze request haalt heel de database op met alle films, personages en starships.
![image](https://github.com/VerbovenSteve/API_DEV_eind_project/assets/113888137/b10fd717-d238-4cfd-96c2-257997e1d8e1)

> Nu zal ik een update doen van de naam van een film dit

## PUT

### put /films/{film_id}
![image](https://github.com/VerbovenSteve/API_DEV_eind_project/assets/113888137/ec7beb9b-63a8-4121-b6ac-e9aea3922696)


> Hierna volgt de delete request

## Delete 

### delete /films/{film_id}
Als we een film willen verwijderen uit de data bank dan kunnen we dit als volgt doen. Je geeft in de url de id mee en deze word dan verwijdert.
![image](https://github.com/VerbovenSteve/API_DEV_eind_project/assets/113888137/b1c899aa-2acb-4f22-85f6-2901e2dc82b2)


### Errorhandeling delete /films/{film_id}
Als de film id niet bestaat en je wil deleten dan krijg je een error.
![image](https://github.com/VerbovenSteve/API_DEV_eind_project/assets/113888137/dab5c279-495a-4d61-b7ba-086aea0d5fcf)



