#!/usr/bin/python3

# Password guessing in Python

import random
import datetime
import time
import statistics


class geneticalg(object):

    genes = []
    fitness = int
    index = int
    childGenes = list()
    guess = ''
    newGene = ''
    alternate = ''
    bestParent = ''
    child = ''

    def __init__(self, target, geneSet):
        self.target = target
        self.geneSet = geneSet
        self.length = len(target)


    def generate_parent(self):
        while len(self.genes) < self.length:
            sampleSize = min(self.length - len(self.genes), len(self.geneSet))
            self.genes.extend(random.sample(self.geneSet, sampleSize))
        self.guess = ''.join(self.genes)
        self.fitness = self.get_fitness(self.genes)
        return Chromosome(self.guess, self.fitness)

    def get_fitness(self, guess):
        return sum(1 for expected, actual in zip(self.target, guess)
                   if expected == actual)

    def mutate(self, run):
        self.index = random.randrange(0, len(run.Genes))
        self.childGenes = list(run.Genes)
        self.newGene, self.alternate = random.sample(self.geneSet, 2)
        self.childGenes[self.index] = self.alternate \
            if self.newGene == self.childGenes[self.index] \
            else self.newGene
        self.guess = ''.join(self.childGenes)
        self.fitness = self.get_fitness(self.guess)
        return Chromosome(self.guess, self.fitness)

    def get_best(self, startTime):
        random.seed()
        self.bestParent = self.generate_parent()
        display(self.bestParent, startTime)

        if self.bestParent.Fitness >= self.length:
            return self.bestParent

        while True:
            self.child = self.mutate(self.bestParent)

            if self.bestParent.Fitness >= self.child.Fitness:
                continue
            display(self.child, startTime)
            if self.child.Fitness >= len(self.bestParent.Genes):
                return self.child
            self.bestParent = self.child

class Chromosome(object):

    def __init__(self, genes, fitness):
        self.Genes = genes
        self.Fitness = fitness


class Benchmark(object):

    @staticmethod
    def run(function):
        timings = []
        for i in range(100):
            startTime = time.time()
            function()
            seconds = time.time() - startTime
            timings.append(seconds)
            mean = statistics.mean(timings)
            print("{0} {1:3.2f} {2:3.2f}".format(
                1 + i, mean,
                statistics.stdev(timings, mean)
                if i > 1 else 0))

def display(run, startTime):
    timeDiff = datetime.datetime.now() - startTime
    print("{0}\t{1}\t{2}".format(run.Genes, run.Fitness, str(timeDiff)))

def guess_password(target):
    geneset = " abcdeghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!."
    startTime = datetime.datetime.now()
    password = geneticalg(target, geneset)

    password.get_best(startTime)
