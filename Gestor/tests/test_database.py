import helpers
import unittest
import database as db
import copy

class TestDatabase(unittest.TestCase):

    def setUp(self):
        db.Clientes.lista = [
            db.Cliente("15J", "Marta", "Perez"),
            db.Cliente("48H", "Manolo", "Lopez"),
            db.Cliente("28Z", "Ana", "Garcia")
        ]
    
    def test_buscar_cliente(self):
        cliente_existente = db.Clientes.buscar("15J")
        cliente_inexistente = db.Clientes.buscar("99X")
        self.assertIsNotNone(cliente_existente)
        self.assertIsNone(cliente_inexistente)
    
    def test_crear_cliente(self):
        nuevo_cliente = db.Clientes.crear("39X", "Camilo", "Sanabria")
        self.assertEqual(len(db.Clientes.lista),4)
        self.assertEqual(nuevo_cliente.dni, "39X")
        self.assertEqual(nuevo_cliente.nombre, "Camilo")
        self.assertEqual(nuevo_cliente.apellido, "Sanabria")
    
    def test_modificar_cliente(self):
        cliente_a_modificar = copy.copy(db.Clientes.buscar("28Z"))
        cliente_modificado = db.Clientes.modificar("28Z", "Mariana", "Garcia")
        self.assertEqual(cliente_a_modificar.nombre, "Ana")
        self.assertEqual(cliente_modificado.nombre, "Mariana")

    def test_borrar_cliente(self):
        cliente_borrado = db.Clientes.borrar("48H")
        cliente_rebuscado = db.Clientes.buscar("48H")
        self.assertEqual(cliente_borrado.dni, "48H")
        self.assertIsNone(cliente_rebuscado)

    def test_dni_valido(self):
        self.assertTrue(helpers.dni_valido("00A", db.Clientes.lista))
        self.assertFalse(helpers.dni_valido("123445", db.Clientes.lista))
        self.assertFalse(helpers.dni_valido("F45", db.Clientes.lista))
        self.assertFalse(helpers.dni_valido("48H", db.Clientes.lista))






