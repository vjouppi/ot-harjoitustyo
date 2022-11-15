import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
        self.kortti = Maksukortti(1000)
        self.vajaakortti = Maksukortti(200)

    def test_uudessa_kassapaatteessa_oikea_summa(self):
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_uudessa_kassapaatteessa_nolla_myytya(self):
        self.assertEqual((self.kassa.edulliset + self.kassa.maukkaat), 0)

    def test_edullinen_kateisosto_toimii(self):
        self.kassa.syo_edullisesti_kateisella(240)
        self.assertEqual((self.kassa.edulliset), 1)

    def test_maukas_kateisosto_toimii(self):
        self.kassa.syo_maukkaasti_kateisella(400)
        self.assertEqual((self.kassa.maukkaat), 1)

    def test_edullinen_kateisosto_kasvattaa_kassaa(self):
        self.kassa.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassa.kassassa_rahaa, 100240)
        
    def test_maukas_kateisosto_kasvattaa_kassaa(self):
        self.kassa.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassa.kassassa_rahaa, 100400)

    def test_edullinen_kateistosto_palauttaa(self):
        vaihtorahat = self.kassa.syo_edullisesti_kateisella(200)
        self.assertEqual(vaihtorahat, 200)

    def test_maukas_kateistosto_palauttaa(self):
        vaihtorahat = self.kassa.syo_maukkaasti_kateisella(300)
        self.assertEqual(vaihtorahat, 300)

    def test_edullinen_kateistosto_ei_kasvata_myyntia(self):
        vaihtorahat = self.kassa.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassa.edulliset, 0)

    def test_maukas_kateistosto_ei_kasvata_myyntia(self):
        vaihtorahat = self.kassa.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_edullinen_korttiosto_toimii(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 7.60 euroa")

    def test_maukas_korttiosto_toimii(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 6.00 euroa")

    def test_edullinen_korttiosto_palauttaa(self):
        self.assertEqual(self.kassa.syo_edullisesti_kortilla(self.kortti), True)

    def test_maukas_korttiosto_palauttaa(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kortilla(self.kortti), True)

    def test_edullinen_korttiosto_kasvattaa_myyntia(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassa.edulliset, 1)

    def test_maukas_korttiosto_kasvattaa_myyntia(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassa.maukkaat, 1)

    def test_kortilla_liian_vahan_rahaa_edullinen_saldo(self):
        self.kassa.syo_edullisesti_kortilla(self.vajaakortti)
        self.assertEqual(str(self.vajaakortti), "Kortilla on rahaa 2.00 euroa")

    def test_kortilla_liian_vahan_rahaa_maukas_saldo(self):
        self.kassa.syo_maukkaasti_kortilla(self.vajaakortti)
        self.assertEqual(str(self.vajaakortti), "Kortilla on rahaa 2.00 euroa")

    def test_kortilla_liian_vahan_rahaa_edullinen_myydyt(self):
        self.kassa.syo_edullisesti_kortilla(self.vajaakortti)
        self.assertEqual(self.kassa.edulliset, 0)

    def test_kortilla_liian_vahan_rahaa_maukas_saldo(self):
        self.kassa.syo_maukkaasti_kortilla(self.vajaakortti)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_kortilla_liian_vahan_rahaa_edullinen_paluukoodi(self):
        tulos = self.kassa.syo_edullisesti_kortilla(self.vajaakortti)
        self.assertEqual(tulos, False)

    def test_kortilla_liian_vahan_rahaa_maukas_paluukoodi(self):
        tulos = self.kassa.syo_maukkaasti_kortilla(self.vajaakortti)
        self.assertEqual(tulos, False)

    def test_kortilla_edullisesti_ei_kasvata_kassaa(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        
    def test_kortilla_maukkaasti_ei_kasvata_kassaa(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_korttia_ladatessa_kortti_kasvaa(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, 1000)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 20.00 euroa")

    def test_korttia_ladatessa_kassa_kasvaa(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, 1000)
        self.assertEqual(self.kassa.kassassa_rahaa, 101000)

    def test_korttia_negatiivisella_ladatessa_kassa_ei_kasva(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, -1)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
