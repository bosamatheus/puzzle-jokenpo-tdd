import unittest


class Jokenpo():
    
    def joga(self, jogador1, jogador2):
        if jogador1 == "Pedra":
            if jogador2 == "Tesoura":
                return "Pedra"
            elif jogador2 == "Papel":
                return "Papel"
            else:
                return "Pedra"
        elif jogador1 == "Papel":
            if jogador2 == "Pedra":
                return "Papel"
            elif jogador2 == "Tesoura":
                return "Tesoura"
            else:
                return "Papel"
        else:
            if jogador2 == "Pedra":
                return "Pedra"
            elif jogador2 == "Papel":
                return "Tesoura"
            else:
                return "Tesoura"


class JokenpoTest(unittest.TestCase):

    def test_pedra_tesoura(self):
        jokenpo = Jokenpo()
        self.assertEqual("Pedra", jokenpo.joga("Pedra", "Tesoura"))

    def test_pedra_papel(self):
        jokenpo = Jokenpo()
        self.assertEqual("Papel", jokenpo.joga("Pedra", "Papel"))
    
    def test_pedra_pedra(self):
        jokenpo = Jokenpo()
        self.assertEqual("Pedra", jokenpo.joga("Pedra", "Pedra"))

    def test_papel_tesoura(self):
        jokenpo = Jokenpo()
        self.assertEqual("Tesoura", jokenpo.joga("Papel", "Tesoura"))
    
    def test_papel_pedra(self):
        jokenpo = Jokenpo()
        self.assertEqual("Papel", jokenpo.joga("Papel", "Pedra"))
    
    def test_papel_papel(self):
        jokenpo = Jokenpo()
        self.assertEqual("Papel", jokenpo.joga("Papel", "Papel"))
    
    def test_tesoura_pedra(self):
        jokenpo = Jokenpo()
        self.assertEqual("Pedra", jokenpo.joga("Tesoura", "Pedra"))
    
    def test_tesoura_papel(self):
        jokenpo = Jokenpo()
        self.assertEqual("Tesoura", jokenpo.joga("Tesoura", "Papel"))
    
    def test_tesoura_tesoura(self):
        jokenpo = Jokenpo()
        self.assertEqual("Tesoura", jokenpo.joga("Tesoura", "Tesoura"))


if __name__ == "__main__":
    unittest.main()
