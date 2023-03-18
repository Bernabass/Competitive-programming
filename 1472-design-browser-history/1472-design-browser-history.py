class BrowserHistory:
    #
    def __init__(self, homepage: str):
        self.array = [homepage]
        self.cur_page_pointer = 0  
        self.cur_boundary = 0

    
    def visit(self, url: str) -> None:
        self.cur_page_pointer += 1
        if self.cur_page_pointer == len(self.array):
            self.array.append(url)
        else:
            self.array[self.cur_page_pointer] = url
        self.cur_boundary = self.cur_page_pointer
        

    def back(self, steps: int) -> str:
        self.cur_page_pointer = max(0, self.cur_page_pointer - steps)
        return self.array[self.cur_page_pointer]
        

    def forward(self, steps: int) -> str:
        self.cur_page_pointer = min(self.cur_boundary, self.cur_page_pointer + steps)
        return self.array[self.cur_page_pointer]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)