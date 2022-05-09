from .pipeline import Pipeline, PipelineStep
from .data import Data, Corpus
from .analyzer import ChordSymbolUnigrams
import matplotlib.pyplot as plt
import os 

class BarPlotter(PipelineStep):

    def __init__(self, directory=None, **kwargs):
        self.directory = directory
        self.kwargs = kwargs

    def process_data(self, data: Data) -> Data:
        plots = {}
        for group, df in data.iter(as_pandas=True):    
            plots[group] = df.droplevel(0).plot(kind="bar", **self.kwargs)
            if self.directory is None:
                plt.show()
            else:
                if group == ():
                    name = "global_unigrams.png"
                else:
                    name = "".join(group) + ".png"
                path = os.path.join(self.directory, name)
                plt.savefig(path)
        result = data.copy()
        result.plots = plots

        return result
