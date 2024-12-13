## Quick Start Guide

It’s easiest to get started using our Python client. Simply install the package:

- Install the `dyson` package using pip:
```bash
pip install dyson   
```
- SignUp/LogIn to the Dyson [`dashboard`](https://crossgl.net/#/dashboard)

- Obtain your first custom API Key for Free!

- Generate and securely store your API key in a `key.cgl` file.


```python
from dyson import router
import torch

class ComplexOperations:
    def add(self):
        a, b = 1, 3
        return a + b

    def func(self):
        x = torch.tensor([1, 2])
        y = torch.tensor([3, 4])
        z = torch.add(x, y)
        return z
```

### Routing Your Workload

Add the `key.cgl` path in your code like so,

```python
key_path = "path/to/your/key.cgl"
```

Add your function with [`paramter`](https://crossgl.github.io/crossgl-docs/dyson/#advanced-routing-parameters) values.

```python
physics_function = ComplexOperations()

result = router.route_hardware(
    key_path,                     
    physics_function,             
    mode="energy-efficient",      
    judge=3,                      
    run_type="log",               
    complexity="medium",         
    precision="normal",           
    multi_device=True             
) 
```