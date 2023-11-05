class DetectSquares:

    def __init__(self):
        self.x_coordinate = defaultdict(lambda:defaultdict(int))
        self.y_coordinate = defaultdict(lambda:defaultdict(int))
        
    def add(self, point: List[int]) -> None:
        x, y = point
        self.x_coordinate[x][y] += 1
        self.y_coordinate[y][x] += 1

    def count(self, point: List[int]) -> int:
        px, py = point
        total = 0
        seen = set()

        for y in self.x_coordinate[px]:
            if y != py:
                side = abs(py - y)
                if side not in seen:
                    total += self.squares(side, point)
                    seen.add(side)

        return total

    def squares(self, side, point):
        x, y = point
        count = 0
        count += self.y_coordinate[y].get(x - side, 0) * self.x_coordinate[x].get(y - side, 0) * self.x_coordinate[x - side].get(y - side, 0)
        count += self.y_coordinate[y].get(x + side, 0) * self.x_coordinate[x].get(y + side, 0) * self.x_coordinate[x + side].get(y + side, 0)
        count += self.y_coordinate[y].get(x - side, 0) * self.x_coordinate[x].get(y + side, 0) * self.x_coordinate[x - side].get(y + side, 0)
        count += self.y_coordinate[y].get(x + side, 0) * self.x_coordinate[x].get(y - side, 0) * self.x_coordinate[x + side].get(y - side, 0)

        return count




        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)