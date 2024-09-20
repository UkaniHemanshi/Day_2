"""global doc"""

def rec_fact(num):
    """rec_fact doc"""
    if num == 0 or num ==1 :
        return 1
    else:
        return (num * rec_fact(num-1))
print(rec_fact(5))

# doc string
print(__doc__)
print(rec_fact.__doc__)
