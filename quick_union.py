class QuickUnion:
    """Contains unions and can add items to union or check connectivity"""

    def __init__(self, number=0):
        self.__components = list(range(number))

    def union(self, p: int, q: int):
        """Creates union between p and q.
        components[i] is a parent of i"""

        self.__components[self.find_root(p)] = self.find_root(q)

    def find_root(self, p: int) -> int:
        """Finds a root of p and returns it.
        Find root is equal to find recursively parent of i,
        which doesn't have a parent"""

        while p != self.__components[p]:
            p = self.__components[p]
        return p

    def print_list(self):
        """Prints components list without formatting"""

        print(self.__components)

    def connected(self, p: int, q: int) -> bool:
        """Checks, whether p and q are in one union or not"""
        if self.find_root(p) == self.find_root(q):
            return True
        return False


def input_from_file(filename: str) -> [str]:
    """Reads given file and initialize components list"""

    file_object = open(filename, "r")
    lines = str(file_object.read())
    file_object.close()

    lines = lines.split('\n')
    return [line.split(' ') for line in lines]


def main():
    """Initializes program and run it"""

    lines = input_from_file("input.txt")

    # print(lines)

    _qu = QuickUnion(10)
    # print(_qu.find_root(2))
    # print(_qu.connected(2, 2))

    for line in lines:
        _qu.union(int(line[0]), int(line[1]))

    _qu.print_list()


if __name__ == "__main__":
    main()
