def ex5():
    def dibuixarTaulell():
        rows = 8
        columns = 8

        array_2d = [['O' if (i+j) % 2 == 0 else 'X' for j in range(columns)] for i in range(rows)]

        array_2d.append(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', '#'])
        for i in range(rows):
            array_2d[i].append(i + 1)

        for row in array_2d:
            print(' '.join(str(cell) for cell in row))



    dibuixarTaulell()

if __name__ == "__main__":
    ex5()


