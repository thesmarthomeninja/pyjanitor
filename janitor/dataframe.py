from pandas import Series, DataFrame
from .functions import clean_names


class JanitorSeries(Series):
    @property
    def _constructor(self):
        return JanitorSeries

    @property
    def _constructor_expanddim(self):
        return JanitorDataFrame


class JanitorDataFrame(DataFrame):
    @property
    def _constructor(self):
        return JanitorDataFrame

    @property
    def _constructor_sliced(self):
        return JanitorSeries

    def clean_names(self):
        return clean_names(self)