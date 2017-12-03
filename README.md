# params
Simple parameter space creation library for python

## Example

```python
    from params import ParamSpace
    
    ps = ParamSpace()
    ps.add_value("p1", True)
    ps.add_list("p2", ["A", "B"])
    ps.add_random("p3", 0, 1, 3)
    
    print("param space size ", ps.grid_size)
    
    for params in ps.param_grid():
        print(params)
```

```
    param space size  6
    {'p1': True, 'p2': 'A', 'p3': 0.033606735734026727}
    {'p1': True, 'p2': 'A', 'p3': 0.7415990286837093}
    {'p1': True, 'p2': 'A', 'p3': 0.92264224243582038}
    {'p1': True, 'p2': 'B', 'p3': 0.033606735734026727}
    {'p1': True, 'p2': 'B', 'p3': 0.7415990286837093}
    {'p1': True, 'p2': 'B', 'p3': 0.92264224243582038}
```