from django.test import TestCase
from escola.models import Estudante, Curso, Matricula


class ModelEstudanteTestCase(TestCase):
    # def teste_falha(self):
    #     self.fail('O teste falhou')
    def setUp(self):
        self.estudante = Estudante.objects.create(
            nome = 'David Teste', 
            email = 'email@test.com',
            cpf = '343.228.300-80',
            data_nascimento = '2025-02-02',
            celular = '55 61 99999-9999'
        )

    def test_verifica_atributos_de_estudante(self):
        """Teste que verifica os atributos do modelo de estudante"""
        self.assertEqual(self.estudante.nome, 'David Teste')
        self.assertEqual(self.estudante.email, 'email@test.com') 
        self.assertEqual(self.estudante.cpf, '343.228.300-80') 
        self.assertEqual(self.estudante.data_nascimento, '2025-02-02') 
        self.assertEqual(self.estudante.celular, '55 61 99999-9999')

class ModelCursoTestCase(TestCase):
    def setUp(self):
        self.curso = Curso.objects.create(
           codigo = 'PY01',
           descricao = 'Curso de POO',
           nivel = 'B',
        ) 

    def test_verifica_o_curso(self):
        """Teste para verificar os atributos do curso"""
        self.assertEqual(self.curso.codigo, 'PY01')
        self.assertEqual(self.curso.descricao, 'Curso de POO')
        self.assertEqual(self.curso.nivel, 'B') 

class ModelMatriculaTestCase(TestCase):
    
    def setUp(self):
        self.estudante_matricula = Estudante.objects.create(
            nome = 'Teste Modelo Matricula',
            email='testemodelomatricula@gmail.com',
            cpf='91546870040',
            data_nascimento='2003-02-02',
            celular='86 99999-9999'
        )
        self.curso_matricula = Curso.objects.create(
            codigo='CTMM',descricao='Curso Teste Modelo Matricula',nivel='B'
        )
        self.matricula = Matricula.objects.create(
            estudante=self.estudante_matricula,
            curso=self.curso_matricula,
            periodo='M'
        )
    
    def test_verifica_atributos_de_matricula(self):
        """Teste que verifica os atributos do modelo de Matricula"""
        self.assertEqual(self.matricula.estudante.nome, 'Teste Modelo Matricula')
        self.assertEqual(self.matricula.curso.descricao, 'Curso Teste Modelo Matricula')
        self.assertEqual(self.matricula.periodo, 'M')                           