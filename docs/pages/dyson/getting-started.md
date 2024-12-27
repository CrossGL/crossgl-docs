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
import dyson
import torch
import time
from dyson import router

# Define a function
def mat(a, b):
    return torch.matmul(a,b)


```

### Routing Your Workload

Add the `key.cgl` path in your code like so,

```python
key_path = "path/to/your/key.cgl"
```

Add your function with [`parameter`](https://crossgl.github.io/crossgl-docs/pages/dyson/overview/#advanced-routing-parameters) values.

```python
hardware = router.route_hardware(
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

We now have the hardware name required for routing. This can be passed as a parameter to the dyson.run() function, enabling it to route to the specified hardware.

```python
# Compile the function for CUDA (or CPU)
func = dyson.run(mat, target_device=hardware)

# Execute the function with arguments
a = torch.randn(1000, 1000)
b = torch.randn(1000, 1000)
result = func(a, b)

print(result)
```

