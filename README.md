Les **bibliomarklets** visent à faciliter l'accès aux articles scientifiques payants en passant par les portails de différentes institutions (CNRS, Inserm, universités...).

Ces [bookmarklets](http://fr.wikipedia.org/wiki/Bookmarklet) permettent d'accéder à des articles scientifiques payants à condition que : 

* vous ayez un compte (login / mot-de-passe) chez une institution/fournisseur (typiquement en étant étudiant d'une université ou personnel d'un laboratoire de recherche associé à cette institution) ;
* votre institution soit abonnée à la revue dont l'article vous intéresse.

# Comment on fait ? #
* Enregistrez le fichier `bibliomarklets.html` sur votre ordinateur puis ouvrez-le avec votre navigateur habituel.
* Faites glisser le bouton qui vous intéresse (l'insitution chez qui vous avez un accès un compte d'accès biblio) dans la barre de favoris (Chrome), la barre personnelle (Firefox) ou directement dans vos bookmarks.
* Lorsque vous tombez sur un article payant, cliquez sur le bookmarklet que vous avez enregistré, la page devrait se recharger en vous proposant de vous authentifier (avec le compte de votre institution). Si votre compte est valide et que votre institution est abonné à la revue dont provient l'article, vous y aurez accès.

# Comment ça marche ? #
Un [bookmarklet](http://fr.wikipedia.org/wiki/Bookmarklet) s'est grosso modo du code javascript dans un lien HTML. En cliquant sur le bouton (en fait sur le lien qu'il contient), le code javascript est exécuté. La plupart du temps celui-ci modifie l'adresse web de la page qui contient l'article  pour le faire passer par le proxy de l'institution en question.


<p>L'idée des bibliomarklets vient des articles de blog suivants <a href="http://bioinfo-fr.net/un-bookmarklet-pour-acceder-plus-facilement-aux-publications">Un bookmarklet pour accéder plus facilement aux publications [Bioinfo-fr.net 30/10/2013]</a> et <a href="">Les articles en un clic (droit) [bibliotheque-blogs.unice.fr 26/11/2013]</a>.
