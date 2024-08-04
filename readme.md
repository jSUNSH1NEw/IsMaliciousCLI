## isMalicous project 
Created and maintened by JVQ https://github.com/hexablob

Description : Quickly secure anything by checking if is malicious.

It's based on available public malicious addresses lists sources.

https://ismalicious.com/

## isMalicious CLI
created and maintened by SUNSH1N3

This CLI is made  too make static and dynamic analysis over a ip or a domain to see if it is past/present malicious


## Usage 


### Lists 
is contained on a tar archive in this link : https://fileport.io/43ThPM8b8cJL because of the fileSize limitations of github

The archive contain : 
MaliciousC2.txt 
MaliciousDomains.txt
MaliciousIp.txt

and it need to be refered in the lists folder to make the script work fine  

./lists/MaliciousDomains.txt
./lists/MaliciousIp.txt
./lists/MaliciousC2.txt

## Described Jobs 



## TODO 

Description Static check : Rentré une ou un groupe d'ip ou de domains afin de savoir si il/elle est malicieu(xse)

Description Dynamic check  : Collectez les infos des call ouvert sur differente interface reseaux
Crée une copie avec les infos dans un tableaux md qui sont ensuite concorder par rapport au listes 

Os version 
 - faire un branche windows 
 - faire une branche linux 

Static Check
- Check d'une ou plusieurs ip
- Check d'un ou plusieurs domain 

Dynamical check
- Check & concordance des ip trouver sur le reseaux comparé au liste MaliciousIP & MaliciousC2
- Check des domain relative au Ip trouver 
- Check des ip lier au process PID
- Check des ip lier a netstas level 1
- Faire une Scan reseaux et check les ip contenu dans le scan 

Automatisation 
 - ajout de nouvelle ip ou domain suite au recherche user
 - ajout de nouvelle ip ou domain suite apres le call et sur certaine api ou site 
 - faire un tri des ip non trer sur les repos appeler par l'api 



 



