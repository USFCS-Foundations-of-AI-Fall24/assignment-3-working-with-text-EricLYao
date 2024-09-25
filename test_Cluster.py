from unittest import TestCase
from Cluster import *
from Document import *

class TestCluster(TestCase):
    def test_calculate_centroid(self):
        d = Document(true_class='pos')
        d.add_tokens(['cat','dog','fish','monkey'])
        d2 = Document(true_class='neg')
        d2.add_tokens(['cat','fish','fish','map'])
        d3 = Document(true_class='pos')
        d3.add_tokens(['dog','dog','cat','orangutan'])

        cluster = Cluster(members=[d, d2, d3])
        cluster.calculate_centroid()

        expected = {
            'cat': 1,
            'dog': 1,
            'fish': 1,
            'monkey' : 1/3,
            'map' : 1/3,
            'orangutan' : 1/3
        }
        for item in cluster.centroid.tokens :
            assert cluster.centroid.tokens[item] == expected[item]

        print('OK')


    def test_kmeans(self):
        d = Document(true_class='pos')
        d.add_tokens(['cat', 'dog', 'fish'])
        d2 = Document(true_class='pos')
        d2.add_tokens(['cat', 'dog', 'fish'])
        d3 = Document(true_class='neg')
        d3.add_tokens(['bunny', 'lizard', 'octopus'])
        print(k_means(2, ['pos', 'neg'], [d,d2,d3]))


