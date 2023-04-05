def func(*args, **kwargs):
    print(f'{args=}')
    print(f'{kwargs=}')
    
func(1, 2, 3, a=5, b=6)