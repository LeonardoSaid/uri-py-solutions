from sys import stdin
class ftree:
    def __init__(self, n):
        self.__ft = [0] * (n + 1)
    def rsq(self, b):
        sum = 0
        while b > 0:
            sum += self.__ft[b]
            b -= (b & (-b))
        return sum
    def adj(self, k, v):
        while k < len(self.__ft):
            self.__ft[k] += v
            k += (k & (-k))
def main():
    n = int(stdin.readline())
    v = list(map(int, stdin.readline().split()))
    bb = ftree(n)
    for i in range(n):
        bb.adj(i+1, v[i])
    for line in stdin:
        q, i = line.split()
        i = int(i)
        if q == 'a':
            bb.adj(i, -v[i-1])
            v[i-1] = 0
        else:
            print(bb.rsq(i-1))
main()