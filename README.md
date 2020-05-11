# Yet Another PBO Library

Yapbol is yet another pbo library to unpack and/or modify PBO files used by the
game Arma 3.

## Installing

```
pip install yapbol
```

## Usage

### Read the contents of a file in the PBO
```python
from yapbol import PBOFile

pbo = PBOFile.read_file('filepath.pbo')

# Get metadata.hpp file, that's encoded in utf-8, from the PBO
file = pbo['metadata.hpp']
print('File contents: ', file.data.decode('utf-8'))
```

### Print the contents of a PBO file
```python
from yapbol import PBOFile

pbo = PBOFile.read_file('filepath.pbo')

for file in pbo:
    print('File name: ', file.filename)
```

### Modify and save the PBO
```python
from yapbol import PBOFile

pbo = PBOFile.read_file('filepath.pbo')

# TODO: Modify the file here

pbo.save_file('filepath.repack.pbo')
```
