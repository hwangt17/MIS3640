def move(n, source, bridge, destination):
    if n > 0:
        move(n-1, source, destination, bridge)
        print("%s --> %s" % (source,destination))
        move(n-1, bridge, source, destination)

move(3, 'A', 'B', 'C')
# Expected output:
# A --> C
# A --> B
# C --> B
# A --> C
# B --> A
# B --> C
# A --> C
