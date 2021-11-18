# Задание 1
class Matrix:
    def __init__(self, lists):
        self.matrix = lists

    def __str__(self):
        for el in list(self.matrix):
            for i in list(el):
                print(int(i), end='\t')
            print('\n')
        return ''

    def __add__(self, other):
        result = [[0 for _ in range(len(self.matrix[0]))] for el in range(len(self.matrix))]
        answer = Matrix(result)
        for external_el in range(len(self.matrix)):
            for inner_el in range(len(self.matrix[0])):
                result[external_el][inner_el] = self.matrix[external_el][inner_el] + other[external_el][inner_el]
        return answer


if __name__ == '__main__':
    matr = [[2, 8], [6, 8], [6, 9]]
    matr_2 = [[1, 2], [4, 5], [7, 8]]
    obj = Matrix(matr)
    res = obj + matr_2
    print(res, type(res))
    print(obj, type(obj))
