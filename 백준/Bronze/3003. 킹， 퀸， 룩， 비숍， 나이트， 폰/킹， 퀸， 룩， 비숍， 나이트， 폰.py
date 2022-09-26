king = 1
queen = 1
rook = 2
bishop = 2
knight = 2
pawn = 8

k,q,r,b,kn,p = input().split()
white_king = int(k)
white_queen = int(q)
white_rook = int(r)
white_bishop = int(b)
white_knight = int(kn)
white_pawn = int(p)
print(king-white_king, queen-white_queen, rook-white_rook, bishop-white_bishop,knight-white_knight, pawn-white_pawn)