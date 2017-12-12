# Bibliomarklets

Les **bibliomarklets** visent à faciliter l'accès aux articles scientifiques payants en passant par les proxys institutionnels (CNRS, Inserm, universités...).

Ces [bookmarklets](http://fr.wikipedia.org/wiki/Bookmarklet) permettent d'accéder à des articles scientifiques à condition que : 

- Vous ayez un compte (login et mot de passe) chez une institution / fournisseur. Typiquement en étant étudiant d'une université ou personnel d'un laboratoire de recherche associé à cette institution.

- Votre institution soit abonnée à la revue dont l'article vous intéresse.


# Comment faire ?

* Visualisez le fichier fichier [bibliomarklets.html](https://raw.github.com/pierrepo/bibliomarklets/master/bibliomarklets.html) en cliquant <a href="http://htmlpreview.github.com/?https://raw.github.com/pierrepo/bibliomarklets/master/bibliomarklets.html" target="_blank">ICI</a>.
* Faites glisser le bouton qui vous intéresse (l'institution avec laquelle vous avez un compte d'accès biblio) dans la barre de favoris (pour Chrome), la barre personnelle (pour Firefox) ou directement dans les bookmarks de votre navigateur.
* Lorsque vous tombez sur un article payant, cliquez sur le bookmarklet que vous avez précédemment enregistré, la page devrait se recharger en vous proposant de vous authentifier (avec le compte de votre institution). Si votre compte est valide et que votre institution est abonnée à la revue dont provient l'article, vous y aurez accès.


# Comment ça marche ?

Un [bookmarklet](http://fr.wikipedia.org/wiki/Bookmarklet) s'est grosso modo du code javascript dans un lien HTML. En cliquant sur le bouton (en fait sur le lien qu'il contient), le code javascript est exécuté. Celui-ci modifie l'adresse web de la page qui contient l'article pour le faire passer par le proxy de l'institution en question.

Concrètement, une bibliomarklet va simplement ajouter `.proxy.votre.institution` à l'adresse de la page de votre article, tranformant ainsi

```
http://site.editeur/adresse/article/interessant
```

en

```
http://site.editeur.proxy.votre.institution/adresse/article/interessant
```

Le fichier [bibliomarklets.html](https://raw.github.com/pierrepo/bibliomarklets/master/bibliomarklets.html) est généré par le script Python [build.py](https://raw.github.com/pierrepo/bibliomarklets/master/build.py) à partir du fichier [biblioproxy.txt](https://raw.github.com/pierrepo/bibliomarklets/master/biblioproxy.txt) qui contient une liste d'institutions avec leurs proxys.

# Pourquoi il n'y a pas de bibliomarklet pour ma fac / institution ?

1. Parce que je n'ai pas eu le temps de le faire ;-) Si vous accèdez à votre bliblio via un proxy *simple* du type `http://site.editeur.scientifique.proxy.votre.institution/adresse/article/interessant` alors vous pouvez :

    * L'ajouter vous même au fichier [biblioproxy.txt](https://raw.github.com/pierrepo/bibliomarklets/master/biblioproxy.txt) en clonant ce [dépôt GitHub](https://github.com/pierrepo/bibliomarklets) puis en demandant un [*Pull Request*](https://github.com/pierrepo/bibliomarklets/pulls). 

    * M'envoyer un [mail](http://cupnet.net/about/) ;-)

    * Ou aussi utiliser le [générateur dynamique de bibliomarklets](http://jbarnoud.github.io/proxy-bookmarklet/) proposé par mon ancien collègue [Jonathan Barnoud](https://twitter.com/jbarnoud). Entrez le proxy de votre institution, cliquez sur *Create* et vous obtenez votre bookmarklet !

2. Parce que votre institution utilise un proxy *compliqué* du type 

    ```
    http://sfxeu06.hosted.exlibrisgroup.com/33UPMC?url_ver=Z39.88-2004&url_ctx_fmt=infofi/
    ```
    ou
    ```
    http://atoz.ebsco.com/Link/PackageLocation/7245?PackageLocationId=4619346&UrlSource=ATOZ&Usage=ATOZ
    ```
    et là je ne peux rien pour vous...


# Concepts

L'idée des bibliomarklets vient des articles de blog suivants [Un bookmarklet pour accéder plus facilement aux publications - Bioinfo-fr.net 30/10/2013](http://bioinfo-fr.net/un-bookmarklet-pour-acceder-plus-facilement-aux-publications) et [Les articles en un clic (droit) - bibliotheque-blogs.unice.fr 26/11/2013](http://bibliotheque-blogs.unice.fr/httbu/2013/11/26/les-articles-en-un-clic-droit/)

# Projets connexes

Stephen Turner a également créé un autre [bibliomarklet](https://stephenturner.github.io/scihub_bookmark/) pour Sci-Hub.
