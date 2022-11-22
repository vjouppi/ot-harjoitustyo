# Pakastekirjanpito

Tällä sovelluksella kotimikron omistaja voi valjastaa laitteensa pakastimen sisällön seurantaan.

## Dokumentaatio

[vaatimusmääritely](dokumentaatio/vaatimusmaarittely.md)

[tuntikirjanpito](dokumentaatio/tuntikirjanpito.md)

## Asennus ja käyttö

```bash
poetry install
poetry run invoke start
```

## Testaus

```bash
poetry run invoke coveragereport
xdg-open htmlcov/index.html
```
