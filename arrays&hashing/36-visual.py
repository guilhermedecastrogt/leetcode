import collections

class Solution:
    def isValidSudoku(self, board):
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):

                print("=" * 60)
                print(f"Analisando posição ({r}, {c})")

                if board[r][c] == ".":
                    print("Célula vazia -> pula")
                    continue

                value = board[r][c]

                print(f"Valor encontrado: {value}")
                print()

                print(f"Linha {r}:   {rows[r]}")
                print(f"Coluna {c}:  {cols[c]}")
                print(f"Quadrado {(r//3, c//3)}: {squares[(r//3, c//3)]}")
                print()

                if (
                    value in rows[r] or
                    value in cols[c] or
                    value in squares[(r//3, c//3)]
                ):
                    print("❌ Número repetido!")
                    print("Sudoku inválido.")
                    return False

                print("Nenhuma repetição encontrada.")
                print("Adicionando aos conjuntos...")

                rows[r].add(value)
                cols[c].add(value)
                squares[(r//3, c//3)].add(value)

                print()

                print("Estado após adicionar:")
                print(f"Linha {r}:   {rows[r]}")
                print(f"Coluna {c}:  {cols[c]}")
                print(f"Quadrado {(r//3, c//3)}: {squares[(r//3, c//3)]}")

                input("\nPressione ENTER para continuar...")

        print("=" * 60)
        print("Nenhum conflito encontrado.")
        return True

board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

Solution().isValidSudoku(board)