#exercise01
def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c,0) + 1
    return d

h = histogram('Normal People')
print(h)

def print_hist(h):
    for c in h:
        print(c, h[c])
        
h = histogram('Massachusetts')
print_hist(h)