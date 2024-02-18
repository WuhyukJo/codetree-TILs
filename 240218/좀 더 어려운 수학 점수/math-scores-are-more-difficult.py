Am, Ae = map(int, input().split())
Bm, Be = map(int, input().split())

if Am > Bm or (Am == Bm and Ae > Be) :
    print("A")
else :
    print("B")