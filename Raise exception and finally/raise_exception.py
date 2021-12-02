try:
    raise MemoryError('Memory error')
except MemoryError as e:
    print(e)