class QuickUnion:
    """Contains unions and can add items to union or check connectivity"""

    def __init__(self, number=0):
        self.__components = list(range(number))

    def union(self, _p: int, _q: int):
        """Creates union between _p and _q.
        components[i] is a parent of i"""

        self.__components[self.find_root(_p)] = self.find_root(_q)

    def find_root(self, _p: int) -> int:
        """Finds a root of _p and returns it.
        Find root is equal to find recursively parent of i,
        which doesn't have a parent"""

        while _p != self.__components[_p]:
            _p = self.__components[_p]
        return _p

    def print_list(self):
        """Prints components list without formatting"""

        print(self.__components)

    def connected(self, _p: int, _q: int) -> bool:
        """Checks, whether _p and _q are in one union or not"""
        if self.find_root(_p) == self.find_root(_q):
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
    """Example of using QuickUnion"""

    lines = input_from_file("input.txt")

    _qu = QuickUnion(10)

    for line in lines:
        _qu.union(int(line[0]), int(line[1]))

    _qu.print_list()


if __name__ == "__main__":
    main()
