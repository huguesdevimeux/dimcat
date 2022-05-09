# %%
from dimcat import Corpus, Pipeline, ChordSymbolUnigrams, ChordSymbolBigrams, BarPlotter, CorpusGrouper
import matplotlib.pyplot as plt

c = Corpus(directory=[
    "~/GitHub/DCMLab/all_subcorpora/debussy_suite_bergamasque/",
    "~/GitHub/DCMLab/all_subcorpora/pleyel_quartets/"
    ])

p2 = Pipeline([
    CorpusGrouper(),
    ChordSymbolBigrams(concat_groups=True), 
    ]).process_data(c)

s = p2.get(as_pandas=False)

print(s)

# s.plot(kind="bar", color="g")
# plt.savefig("global_unigrams.png")