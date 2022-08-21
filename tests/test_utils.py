import pandas as pd
from pandion.utils import summerize


a = pd.DataFrame({"a": range(10), "b": range(10, 100, 9)})


def test_summerize():
    assert not summerize(a)
