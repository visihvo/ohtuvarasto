import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    #Lisätty testaamaan alustuksessa (tilavuus < 0) -> 0
    def test_virheellinentilavuus_nollataan(self):
        self.varasto = Varasto(-10)
        self.assertAlmostEqual(self.varasto.tilavuus, 0.0)

    #Lisätty testaamaan alustuksessa, että saldo < 0 alustaa saldon nollaksi
    def test_negatiivinensaldo_nollataan(self):
        self.varasto = Varasto(1, -1)
        self.assertAlmostEqual(self.varasto.saldo, 0.0)

    def test_paljonko_mahtuuu_toimiioikein(self):
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 10)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    #Lisätty testaamaan, että negatiivinen lisäys ei lisää
    def test_negatiivistalisatessa_eilisata(self):
        self.varasto.lisaa_varastoon(-1)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    #Lisätty testaamaan, jos lisättävä määrä+saldo > tilavuus,
    #johtaa siihen että lisätään vain niin paljon, kuin mahtuu eli tilavuus.
    def test_ylitilavuuden_eilisata(self):
        self.varasto.lisaa_varastoon(20)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    #Lisätty testaamaan, ettei saldosta voi ottaa negatiivista
    #määrää pois. 
    def test_negatiivinenottaminen_eiota(self):
        self.varasto.ota_varastosta(-1)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    #Lisätty testaamaan, ettei saldoa enempää voi ottaa
    #ja tämä jättää saldoksi tällöin 0.
    def test_eivoi_ottaa_enempaa_kuin_on(self):
        self.varasto.lisaa_varastoon(5)
        self.varasto.ota_varastosta(10)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
    
    #Lisätty testaamaan, että __str__ tulostaa oikein
    def test_str(self):
        self.assertAlmostEqual(self.varasto.__str__(), "saldo = 0, vielä tilaa 10")
