#!/usr/bin/env python

import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)
    def test_default_product_weight(self):
        """test default product weight is 20"""
        prod = Product('Test Product')
        self.assertEqual(prod.weight,20)

    def test_explode_stealability_nondefault(self):
        """test the explode and stealability functions with non-default values"""
        prod = Product('Test Product', flamability = 51, price =1000)
        self.assertEqual(prod.explode(),"...BABOOOM!!")
        self.assertEqual(prod.stealability(), "very stealable")

class AcmeReportTests(unittest.TestCase):
    def test_default_num_products(self):
        self.assertEqual(len(generate_products()),30)
    def test_legal_names(self):
        prod_list = generate_products()
        for prod in prod_list:
            n = prod.name
            n = n.split(" ")
            self.assertIn(n[0],ADJECTIVES)
            self.assertIn(n[1],NOUNS)


if __name__ == '__main__':
    unittest.main()
