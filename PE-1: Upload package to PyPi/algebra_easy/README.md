# algebra_easy

_A simple linear algebra package written in Python 3_

---

## Installation

**algebra_easy** is available from the Python Package Index [PyPi](https://pypi.org).
If you have Python 3 installed on your system you can use the `pip install` command:

```
pip install algebra_easy
```

---

## Classes

The algebra_easy package currently offers the `Vector()` class, which can directly be imported into your project with:

```python
from algebra_easy import Vector
```

---

## Vector Class

### _Attributes_

The `Vector()` class has two attributes:

- `Vector.coordinates` (Decimal object)
- `Vector.dimension` (int)

### _Methods_

The following `Vector()` class methods are available:

### Constructor

Arguments: int, float

```
v1 = Vector([1.5, -4.8, 3])
```

### + Method

```
v3 = v1 + v2
```

### - Method

```
v3 = v1 - v2
```

### Scalar Mutliplication

Arguments: int, float

```
v1.times_scalar(42)
```


### Vector Normalization

```
unit_vector = v1.normalized()
```
