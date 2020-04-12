"""Following this tutorial"""

import pytest

from flaskapp import Flaskapp


@pytest.fixture
def client():
    app = Flaskapp()
#end client
