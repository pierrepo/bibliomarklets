# -*- coding: utf8 -*-

"""
This script build a HTML file containing bookmarklets from a list of proxies
"""

import configparser

__author__ = "Pierre Poulain"
__copyright__ = "Copyright 2017"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Pierre Poulain"
__email__ = "pierre.poulain@cupnet.net"
__status__ = "Development"



PROXY_NAME = "biblioproxy.txt"
BIBLIOMARKLETS_NAME = "bibliomarklets.html"

HTML_HEADER = """<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="fr" lang="fr" dir="ltr">
<head>

<title>Bibliomarklets : bookmarklets pour faciliter l'accès aux articles scientifiques payants</title>

<style type="text/css">
.btn {
    display: inline-block;
    width: 150px;
    background: #e3e3e3;
    border: 1px solid #bbb;
    -webkit-border-radius: 3px;
    -moz-border-radius: 3px;
    border-radius: 3px;
    color: #333;
    font: bold 12px helvetica, arial, sans-serif;
    padding: 5px 5px 5px 5px;
    margin: 1px 2px 1px 2px;
    text-align: center;
    text-decoration: none;
}

.link {
    margin: 5px 1px;
}
</style>
</head>
<body>
<h1>Bibliomarklets</h1>
"""

# need in order: alias, section, proxy, alias, and section
HTML_BOOKMARKLET = """
<p class="link">
<a class="btn" title="{alias} / {section}" href="javascript:(function(){{location.hostname=location.hostname+'{proxy}';}})();">{alias}</a>
accès via {section}
</p>
"""

HTML_FOOTER = """
<h2>Comment utiliser ces bibliomarklets ?</h2>
<p>
<ul>
    <li>Faites glisser le bouton qui vous intéresse (l'institution avec
    laquelle vous avez un compte d'accès biblio) dans la barre de favoris 
    (pour Chrome), la barre personnelle (pour Firefox) ou directement dans 
    les bookmarks de votre navigateur.</li>
    <li>Lorsque vous tombez sur un article payant, cliquez sur le bookmarklet 
    que vous avez précédemment enregistré. La page devrait se recharger 
    en vous proposant de vous authentifier (avec le compte de votre 
    institution). Si votre compte est valide et que votre institution est 
    abonnée à la revue dont provient l'article, vous y aurez accès.</li>
</ul>
</p>

<h2>Comment contribuer ?</h2>
<p>
Le code utilisé pour générer cette page est disponible <a href="https://github.com/pierrepo/bibliomarklets">ici</a>. N'hésitez pas à l'améliorer.
</p>
<p>
Si vous souhaitez ajouter votre instition, envoyez-moi un mail à pierre.poulain@cupnet.net (mais lisez <a href="https://github.com/pierrepo/bibliomarklets#pourquoi-il-ny-a-pas-de-bibliomarklet-pour-ma-fac--institution-">ceci</a> d'abord).
</p>
<p>
-- <br />
Pierre Poulain (<a href="http://cupnet.net">cupnet.net</a>, 2017)
</p>
</body>
</html>
"""


if __name__ == "__main__":
    proxies = configparser.SafeConfigParser()
    proxies.read(PROXY_NAME)

    f_out = open(BIBLIOMARKLETS_NAME, "w")
    f_out.write(HTML_HEADER)

    # Read the whole configuration file
    for section in proxies.sections():
        proxy_dic = {}
        for (key, value) in proxies.items(section):
            proxy_dic[key] = value
        f_out.write(HTML_BOOKMARKLET.format(alias=proxy_dic["alias"],
                                            section=section,
                                            proxy=proxy_dic["proxy"]))

    f_out.write(HTML_FOOTER)
    f_out.close()
    print("wrote {}".format(BIBLIOMARKLETS_NAME))
