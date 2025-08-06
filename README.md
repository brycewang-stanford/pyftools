# PyFtools

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![PyPI](https://img.shields.io/badge/PyPI-coming%20soon-orange.svg)](https://pypi.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

A Python implementation of **ftools** - Fast data manipulation tools inspired by Stata's ftools package.

## Overview

PyFtools is a Python port of the popular Stata package [ftools](https://github.com/sergiocorreia/ftools) by Sergio Correia. It provides fast and efficient data manipulation capabilities, particularly for working with categorical variables and performing group-based operations on large datasets.

## Key Features

- **Fast Factor Variables**: Efficient handling of categorical variables using advanced hashing algorithms
- **Group Operations**: High-performance group-by operations without requiring data sorting
- **Memory Efficient**: Optimized memory usage for large datasets
- **Pandas Integration**: Seamless integration with pandas DataFrames
- **Stata Compatibility**: Familiar syntax for users coming from Stata

## Planned Functionality

The package aims to provide Python equivalents for the following ftools commands:

- `fcollapse` - Fast collapse operations (aggregation)
- `fegen group` - Efficient group identifier generation
- `fmerge` - Fast merging operations
- `flevelsof` - Extract unique levels from variables
- `fisid` - Identify unique observations
- `fsort` - Fast sorting using counting sort
- `freshape` - Efficient reshaping operations

## Installation

**Note: This package is currently under development and will be published to PyPI soon.**

For now, you can install from source:

```bash
git clone https://github.com/brycewang-stanford/pyftools.git
cd pyftools
pip install -e .
```

Once published to PyPI, installation will be as simple as:

```bash
pip install pyftools
```

## Quick Start

```python
import pandas as pd
import pyftools as ft

# Create sample data
df = pd.DataFrame({
    'group': ['A', 'B', 'A', 'B', 'A'],
    'value': [1, 2, 3, 4, 5]
})

# Fast group operations
factor = ft.Factor(df['group'])
result = factor.collapse(df['value'], method='sum')
```

## Development Status

This project is in active development. The current repository contains the original Stata source files for reference and planning purposes. Python implementation is underway.

### Roadmap

- [ ] Core Factor class implementation
- [ ] Basic group operations
- [ ] Pandas integration
- [ ] Performance benchmarking
- [ ] Documentation and examples
- [ ] PyPI package release
- [ ] Advanced features (joins, reshaping, etc.)

## Performance Goals

PyFtools aims to provide:

- O(N) performance for most operations (vs O(N log N) for traditional approaches)
- Efficient memory usage through smart data structures
- Competitive performance with pandas and other popular data manipulation libraries
- Scalability to datasets with millions of observations

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## Acknowledgments

This project is inspired by and aims to port the excellent work of:

- [Sergio Correia](http://scorreia.com) - Original author of Stata's ftools
- [Wes McKinney](http://wesmckinney.com/) - Insights on fast data manipulation from pandas
- The broader data science community working on efficient data processing tools

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## References

- Original ftools documentation: [Stata ftools](https://github.com/sergiocorreia/ftools)
- Performance insights: [Fast Groupby Operations](http://wesmckinney.com/blog/nycpython-1102012-a-look-inside-pandas-design-and-development/)

---

**Status**: 🚧 Under Development | **Target Release**: Coming Soon to PyPI
