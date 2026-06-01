import unittest
from datetime import datetime
from app import obter_resposta, chat, main

class TestChatBot(unittest.TestCase):

    def test_obter_resposta(self):
        
        self.assertEqual(obter_resposta("Olá"), "Olá! Como posso ajudar você hoje?")
        self.assertEqual(obter_resposta("O que estás a fazer?"), "Estou a falar contigo :)")
        self.assertEqual(obter_resposta("Qual o teu género musical favorito?"), "Rock")
        self.assertEqual(obter_resposta("Vives onde?"), "Vivo na internet")
        self.assertEqual(obter_resposta("Como te chamas?"), "O meu nome é: Bot :)")
        self.assertEqual(obter_resposta('qual é o teu filme favorito?'), 'O meu filme favorito é: O Senhor dos Anéis')
        self.assertEqual(obter_resposta('qual é a tua cor favorita?'), 'A minha cor favorita é: Azul')
        self.assertEqual(obter_resposta('bye'), 'Gostei de falar contigo! Até breve...')

if __name__ == '__main__':
    unittest.main()