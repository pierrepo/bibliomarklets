Les **bibliomarklets** visent à faciliter l'accès aux articles scientifiques payants en passant par les proxys institutionnels (CNRS, Inserm, universités...).

Ces [bookmarklets](http://fr.wikipedia.org/wiki/Bookmarklet) permettent d'accéder à des articles scientifiques à condition que : 

* vous ayez un compte (login / mot-de-passe) chez une institution/fournisseur (typiquement en étant étudiant d'une université ou personnel d'un laboratoire de recherche associé à cette institution) ;
* votre institution soit abonnée à la revue dont l'article vous intéresse.

# Comment on fait ? #

* Visualisez le fichier fichier [bibliomarklets.html](https://raw.github.com/pierrepo/bibliomarklets/master/bibliomarklets.html) en cliquant <a href="http://htmlpreview.github.com/?https://raw.github.com/pierrepo/bibliomarklets/master/bibliomarklets.html" target="_blank">ICI</a>.
* Faites glisser le bouton qui vous intéresse (l'insitution avec laquelle vous avez un compte d'accès biblio) dans la barre de favoris (Chrome), la barre personnelle (Firefox) ou directement dans vos bookmarks.
* Lorsque vous tombez sur un article payant, cliquez sur le bookmarklet que vous avez enregistré, la page devrait se recharger en vous proposant de vous authentifier (avec le compte de votre institution). Si votre compte est valide et que votre institution est abonnée à la revue dont provient l'article, vous y aurez accès.

# Comment ça marche ? #

Un [bookmarklet](http://fr.wikipedia.org/wiki/Bookmarklet) s'est grosso modo du code javascript dans un lien HTML. En cliquant sur le bouton (en fait sur le lien qu'il contient), le code javascript est exécuté. La plupart du temps celui-ci modifie l'adresse web de la page qui contient l'article  pour le faire passer par le proxy de l'institution en question.

[bibliomarklets.html](https://raw.github.com/pierrepo/bibliomarklets/master/bibliomarklets.html) est généré par le script Python [build.py](https://raw.github.com/pierrepo/bibliomarklets/master/build.py) à partir du fichier [biblioproxy.txt](https://raw.github.com/pierrepo/bibliomarklets/master/biblioproxy.txt) qui contient une liste d'institutions avec leur proxy.

L'idée des bibliomarklets vient des articles de blog suivants [Un bookmarklet pour accéder plus facilement aux publications - Bioinfo-fr.net 30/10/2013](http://bioinfo-fr.net/un-bookmarklet-pour-acceder-plus-facilement-aux-publications) et [Les articles en un clic (droit) - bibliotheque-blogs.unice.fr 26/11/2013](http://bibliotheque-blogs.unice.fr/httbu/2013/11/26/les-articles-en-un-clic-droit/)


