# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen avulla käyttäjien on mahdollista pitää kirjaa pakastimen sisällä olevista _pakasteista_. Sovellukseen on mahdollista rekisteröityä usealla käyttäjätunnuksella. Pakastin voi olla yksilöllinen tai jaettu useiden käyttäjien välillä.

## Käyttäjät

Alkuvaiheessa sovelluksella on ainoastaan perustason käyttäjätunnuksia, eli _normaaleja käyttäjiä_. Myöhemmin sovellukseen mahdollisesti lisätään kattavilla oikeuksilla varustettu _pääkäyttäjä_.

## Käyttöliittymäluonnos

Sovellus koostuu neljästä eri näkymästä

### Kirjautumisruutu

Ensimmäisenä näytetään kirjautumisruutu.

Kirjautumisruutu sisältää tekstikentät käyttäjätunnukselle ja salasanalle, kirjautumisnappulan ja uuden käyttäjän luontinappulan.

### Käyttäjänluomisruutu

Jos kirjautumisruudussa valitaan uuden käyttäjän luonti, aukeaa uusi ruutu, jossa pyydetään uutta käyttäjätunnusta ja salasanaa. Olemassaolevasta käyttäjästä varoitetaan, onnistunut käyttäjätunnuksen luonti kirjaa käyttäjän suoraan sisään.

### Päänäkymä

Onnistumisen kirjautumisen tai käyttäjän luonnin jälkeen päästään päänäkymään.

Päänäkymässä käyttäjä näkee hänen pakastimensa sisällön. Näkymässä käyttäjällä on mahdollisuus lisätä lokeroita pakastimeen ja pakasteita oman pakastimeensa lokeroihin. Päänäkymässä on myös pudotusvalikko, josta voi valita toisen käyttäjän julkaiseman pakastimen, rasti ruutuun pakastimen julkaisua varten ja nappula uloskirjautumista varten.

Vastaluodun käyttäjän pakastin on oletuksena yksilokeroinen.

Uloskirjausnappi vie takaisin kirjautumisruutuun.

### Vieraan pakastimen tarkastelu

Tämä on samankaltainen ikkuna kuin päänäkymä, mutta vain lukutilassa, eli vieraan pakastimen sisältöön ei voi kajota.

## Perusversion tarjoama toiminnallisuus

### Ennen kirjautumista

- Käyttäjä voi rekisteröidä itselleen käyttäjätunnuksen
  - Joka käyttäjällä on oltava toisista poikkeava käyttäjätunnus ja pituudeltaan tunnuksen on oltava vähintään 2 merkkiä
- Jos käyttäjätunnus on jo olemassa, sillä voi kirjautua sovellukseen
  - Sisään kirjautuminen sallitaan, mikäli käyttäjätunnus löytyy tietokannasta ja salasana täsmää käyttäjätunnusta varten tietokannasta löytyneeseen
  - Sovellus antaa virheilmoituksen, mikäli käyttäjätunnus tai salasana on väärin.

### Kirjautumisen jälkeen

- Käyttäjä näkee oman pakastimensa sisällön eli _pakasteet_
- Käyttäjä voi lisätä uuden pakasteen valitsemaansa lokeroon
  - koko pakastimen sisällön voi myös julkaista kaikkien käyttäjien nähtäväksi
- Käyttäjä voi poistaa pakasteen pakastimestaan, jolloin pakaste häviää lokerosta
- Käyttäjä voi lisätä pakasteen pakastimeensa, jolloin pakaste ilmestyy lokeroon
- Käyttäjä voi lisätä lokeroita pakastimeensa
- Käyttäjä voi kirjauta itsensä ulos järjestelmästä

## Jatkokehitysideoita

Kun perustoiminnallisuus on saatu rakennettua, sovellukseen voisi lisätä seuraavanlaisia ominaisuuksia:

- Salasanan vaihto
- Pakastekohtainen parasta-ennen päivä
- Varoitus vanhentuvista ja vanhentuneista pakasteista kirjautumisen jälkeen
- Pakastekohtainen kappalemäärä
- Pakasteen muokkaus
- Pakastimien lisäys ja poisto
- Käyttäjien kesken jaetut pakastimet
- Oman käyttäjätunnuksen lakkauttaminen
