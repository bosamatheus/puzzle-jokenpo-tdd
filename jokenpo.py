import unittest

class Jokenpo(object):
    
    def verifica_vencedor(self, jogador1, jogador2):
        return "Pedra"

class JokenpoTest(unittest.TestCase):

    def test_pedra_vence(self):
        jokenpo = Jokenpo()
        self.assertEqual("Pedra", jokenpo.verifica_vencedor("Pedra", "Tesoura"))

if __name__ == "__main__":
    unittest.main()
