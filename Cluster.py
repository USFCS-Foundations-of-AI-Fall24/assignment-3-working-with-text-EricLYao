import random

from Document import *

class Cluster :
    ## a cluster is a group of documents
    def __init__(self, centroid=None, members=None):
        if centroid :
            self.centroid = centroid
        else :
            self.centroid = Document(true_class='pos')
        if members :
            self.members = members
        else :
            self.members = []

    def __repr__(self):
        return f"{self.centroid} {len(self.members)}"

    ## You do this.
    def calculate_centroid(self):
        if not self.members:
            return None  # no members
        
        # defaultdict to store token sums
        token_sums = defaultdict(lambda: 0)
        num_docs = len(self.members)

        # Sum token counts 
        for doc in self.members:
            for token, count in doc.tokens.items():
                token_sums[token] += count

        # avg token counts
        averaged_tokens = {token: count / num_docs for token, count in token_sums.items()}

        # new centroid Document with averaged token counts
        self.centroid = Document(true_class='centroid')
        for token, avg_count in averaged_tokens.items():
            self.centroid.tokens[token] = avg_count


# Call like so: k_means(2, ['pos','neg'], positive_docs + negative_docs)

def k_means(n_clusters, true_classes, data) :
    cluster_list = [Cluster(centroid=Document(true_class=item)) for item in true_classes]

    ## initially assign data randomly.

    ## compute initial cluster centroids

    # while not done and i < limit
    #   i++

    #   reassign each Document to the closest matching cluster using
    #   cosine similarity
    #   compute the centroids of each cluster
    return cluster_list