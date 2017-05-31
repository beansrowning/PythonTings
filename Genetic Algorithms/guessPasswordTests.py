#!/usr/bin/python3

import unittest
import datetime
import geneticalg as genetic

class GuessPasswordTests(unittest.TestCase):
    geneset = " abcdeghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!."

    def test_Hello_World(self):
        target = "Hello World!"
        self.guess_password(target)

    def test_benchmark(self):
        genetic.Benchmark.run(lambda: self.test_Hello_World())

    def guess_password(self, target):

        optimalFitness = len(target)
        startTime = datetime.datetime.now()
        password = genetic.geneticalg(target, self.geneset)
        best = password.get_best(startTime)

        self.assertEqual(best.Genes, target)

if __name__ == '__main__':
    unittest.main()
