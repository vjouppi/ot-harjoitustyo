## Monopoli

Monopoli-pelin luokkakaavio

```mermaid
 classDiagram
      Monopoli "" --> "1" Pelilauta
      Pelaaja "" --> "2" Noppa
      Pelilauta "" --> "40" Ruutu
      Ruutu "" --> "1" Ruutu
      Monopoli "" --> "2..8" Pelaaja
      Pelaaja "" --> "1" Pelinappula
      Pelinappula "" --> "1" Ruutu
```
