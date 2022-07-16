# YAML KEYGEN

A Python module for extracting keys from a YAML file.
If a YAML contains a nested hierarchy then the complete path is listed from parent to child key.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install yaml_keygen.

```bash
pip install yaml_keygen
```

The source code is currently hosted on GitHub at: https://github.com/fa1zali/yaml_keygen

## Get Started

```python
from yaml_keygen import YAML

# Initialize the YAML object
yk = YAML()

# Reads the YAML and return a dictionary object
yaml = yk.read(filename="<PATH>")

# Extracts the keys from dictionary object and stores them in a list
keys = yk.get_keys(data=yaml, sep='/')

# Saves the extracted keys to a text file
yk.to_text(data=keys, filename="<PATH>")
```

## Dependencies

[ruamel.yaml](https://sourceforge.net/p/ruamel-yaml/code/ci/default/tree/)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://github.com/fa1zali/yaml_keygen/blob/main/LICENSE)