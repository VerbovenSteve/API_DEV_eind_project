# Basisproject API Development
## Thema

Voor mijn project heb ik gekozen voor Star Wars:

Star Wars is een franchise waar ik zelf gepassioneerd over ben.
Het universum, de personages, en de verhalen boeien me enorm.
Hierdoor is het werken aan een project binnen dit thema niet alleen een professionele uidaging, maar ook een kans om te werken met iets waar ik graag met bezig ben.
Binnen de Star Wars-wereld is er een breed scala van entiteiten zoals films, personages en starships maar ook enorm veel collector items of speelgoed.
Dit biedt me de kans om met iets gevarieerd te werken en waar ook zeer veel uitbreidingsmogelijkheden inzitten.

## Werking API

Als basis voor mijn API heb ik een Sqlite-databank gebruikt.
In de databank zitten 3 tabellen: 
1. Films
2. Persons
3. Starships

In de databank kunnen kan je per film de personages en de Starships toevoegen. Via de Api kan je zowel ze oproepen of verwijderen en je kan ook de volledige database in zijn geheel ophalen.

![image](https://github.com/VerbovenSteve/api_development/assets/113888137/11a26828-1db3-436a-aa37-368fae0a41c3)
### link naar API:

https://useritem-api-service-verbovensteve.cloud.okteto.net/docs 

In het volgende deel zal ik alle functies laten zien van de interface.
> we beginnen bij de post requests. Dit wil zeggen het opvullen van de verschillende tabellen
## post 

### post /films

Deze post zal zorgen dat we een film in de databank kunnen zetten
![image](https://github.com/VerbovenSteve/api_development/assets/113888137/5c03458c-620a-4ed0-aeda-50cc14dc322a)

### Error handeling post /films

Als een film al bestaat in de database dan zal bij het opnieuw toevoegen een error komen. deze zal als volgt eruit zien.
![image](https://github.com/VerbovenSteve/api_development/assets/113888137/12271803-e734-46ff-9a24-8964b9de02bc)


### post /persons

Deze post zorgt ervoor dat we een personage kunnen toevoegen aan een bepaald film id.
![image](https://github.com/VerbovenSteve/api_development/assets/113888137/fd733bfd-647c-4305-ba45-c99b5521e478)

### Error handeling post /persons

Als een personage al in de database bestaat zal er een error komen deze ziet er uit als volgt.
![image](https://github.com/VerbovenSteve/api_development/assets/113888137/81b8bf8b-fc55-4307-a5c3-9e1b6be9ecd6)



### post /starships

Deze post zal starships toevoegen aan een film via de film id.
![image](https://github.com/VerbovenSteve/api_development/assets/113888137/1f3f1c6b-1361-4d55-8179-c9b5afe2daef)

### Error handeling post /starships

Als er een bepaald starship al in de database staat dan zal er een error gegenereerd worden deze ziet er als volgt uit.
![image](https://github.com/VerbovenSteve/api_development/assets/113888137/d78c9eee-1cf8-40d6-adec-71e58a603d0d)


> we zullen nu verder gaan met de get requests. Dit wil zeggen dat we verschillende items uit de tabellen gaan halen.

## get

### get /films

Deze get request zal ervoor zorgen dat we alle films in de database kunnen ophalen.
![image](https://github.com/VerbovenSteve/api_development/assets/113888137/72100ca4-ad50-4d9d-94d6-c1ab20bc0fea)

### Error handeling get /films

Als we een film gaan zoeken met een id dat niet in de database te vinden is krijgen we een error.
![image](https://github.com/VerbovenSteve/api_development/assets/113888137/726c8cc3-1f04-43a1-a202-ca1eaf8bc57c)


### get /persons/

Deze request zal de persoon bij naam zoeken en uit de database ophalen.
![image](https://github.com/VerbovenSteve/api_development/assets/113888137/a44bb155-fc2c-47e2-a42d-e1cce146c07c)

### Error handeling get /persons/

Als we de naam van een personage dat niet bestaat invoeren dan krijgen we een error.
![image](https://github.com/VerbovenSteve/api_development/assets/113888137/af87e3c6-7692-433b-b2f0-4984fa650d07)


### get /starships

Deze request haalt alle starships uit de database.
![image](https://github.com/VerbovenSteve/api_development/assets/113888137/86f81e34-6cbf-4fc2-9027-982e8674314c)

### Error handeling starships

Als je verkeerde skip en limit ingeeft voor de id van de starship krijg je een error.
![image](https://github.com/VerbovenSteve/api_development/assets/113888137/f8683fc3-46b2-4cf8-a072-80e77ac87949)


### get /films/all_with_characters_starships

Deze request haalt heel de database op met alle films, personages en starships.
![image](https://github.com/VerbovenSteve/api_development/assets/113888137/c964119b-af2e-4634-a43c-5d5dd7e72e54)

> Als laatste gaan we verder met de delete requests.

## Delete 

### delete /films/

Deze delete zal alle films verwijderen.
![image](https://github.com/VerbovenSteve/api_development/assets/113888137/097fd5c4-0761-47dd-8d7c-8c5bec6406f1)

### delete /films/{film_id}

Als de film id niet bestaat en je wil deleten dan krijg je een error.
![image](https://github.com/VerbovenSteve/api_development/assets/113888137/f1393bd1-12fe-42ac-adbf-ce0611b16951)

### delete /persons

Deze delete zal alle persons verwijderen uit de database.
![image](https://github.com/VerbovenSteve/api_development/assets/113888137/4a654529-71c0-4069-bf14-78d7c325ec0b)

### delete /starships

Als je de starships wil verwijderen uit de database.
![image](https://github.com/VerbovenSteve/api_development/assets/113888137/d71ffcd8-13dc-45e7-9f9b-2f35dfb61128)

# De database is terug leeg?

Bij wijze van afsluiting laat ik graag nog zien dat de database terug volledig leeg is.
![image](https://github.com/VerbovenSteve/api_development/assets/113888137/b09a2f52-d08e-4756-bd9e-b75a5c7867f2)
![image](https://github.com/VerbovenSteve/api_development/assets/113888137/158138d9-f76c-4797-ae1c-2e8f214096e3)
![image](https://github.com/VerbovenSteve/api_development/assets/113888137/6101232b-6067-414e-b83a-b15b41ed417a)
![image](https://github.com/VerbovenSteve/api_development/assets/113888137/3ef8f02e-5f3d-401b-b387-f4b70b38a9f1)
> Zoals we kunnen zien in bovenstaande afbeeldingen is de data base volledig leeg en vinden we geen films, persons of starships meer.
> Zodat jullie zelf zouden kunnen testen zal ik ook de database terug opvullen.
