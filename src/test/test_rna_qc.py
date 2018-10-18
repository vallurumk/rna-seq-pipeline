"""
unittests for rna_qc.py
"""

import rna_qc
import unittest
from collections import OrderedDict


class TestQCMetric(unittest.TestCase):
    def test_type_check(self):
        with self.assertRaises(TypeError):
            rna_qc.QCMetric('name', 1)

    def test_get_name(self):
        qc_obj = rna_qc.QCMetric('a', {})
        self.assertEqual(qc_obj.name, 'a')

    def test_get_content(self):
        qc_obj = rna_qc.QCMetric('_', {2: 'a', 1: 'b'})
        self.assertEqual(qc_obj.content, OrderedDict([(1, 'b'), (2, 'a')]))

    def test_less_than(self):
        smaller_obj = rna_qc.QCMetric(1, {})
        bigger_obj = rna_qc.QCMetric(2, {})
        self.assertTrue(smaller_obj < bigger_obj)

    def test_equals(self):
        first_obj = rna_qc.QCMetric('a', {})
        second_obj = rna_qc.QCMetric('a', {'x': 'y'})
        self.assertTrue(first_obj == second_obj)

    def test_repr(self):
        obj = rna_qc.QCMetric('a', {1: 'x'})
        self.assertEqual(obj.__repr__(), "QCMetric('a', OrderedDict([(1, 'x')]))")