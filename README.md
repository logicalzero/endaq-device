# `endaq.device`
`endaq.device` (formerly `endaqlib`) provides a means of representing, accessing, configuring
and controlling [enDAQ™ data
recorders](https://endaq.com/collections/endaq-shock-recorders-vibration-data-logger-sensors).
It also supports legacy SlamStick™ devices (X, C, and S).

## Installation

<!--
The `endaq-device` package is [available on
PyPI](https://pypi.org/project/endaq-device/), and can be installed via
`pip`:

    pip install endaq-device
-->
For the most recent features that are still under development, you can
also use <span class="title-ref">pip</span> to install endaq directly
from [the GitHub
repository](https://github.com/MideTechnology/endaq-device/):

    pip install git+https://github.com/MideTechnology/endaq-device.git@develop

Note: While `endaq-device` installs into the same `endaq` 'namespace' as
[endaq-python](https://docs.endaq.com/en/latest/index.html), it is
otherwise separate; the two packages are not interdependent, and one can
be installed without the other. The packages do distinctly different
things, and have very different use-cases.

## Documentation
*Note: the documentation is currently a work in progress.*
<!--
The docs for this package can be found [here](https://docs.endaq.com/en/latest/).
-->

The documentation is built using [Sphinx](https://www.sphinx-doc.org). To build the documentation,
clone the repo and use the following steps:
1. `cd <repo root dir>`
2. `pip install -e .[docs]`
3. `pip install -r ./docs/requirements.txt`   
4. `sphinx-build -W -b html docs docs/_build`

Note: The documentation build conflicts with endaq-python; if you already have
endaq-python installed, it is easiest to work in a virtual environment (e.g., first using
`python -m venv <env dir>` followed by `<venv dir>\Scripts\activate` under Windows,
`source <venv dir>/bin/activate` under Linux/macOS). 

## License

The endaq-python repository is licensed under the MIT license. The full text can be found in the [LICENSE file](https://github.com/MideTechnology/endaq-python/blob/main/LICENSE).
