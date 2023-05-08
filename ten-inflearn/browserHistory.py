class Node:
    def __init__(self, value = "", prev = None, next = None) -> None:
        self.prev  = prev
        self.value = value
        self.next = next

class BrowserHistory:
    def __init__(self, homepage: str):
        new_node = Node(homepage)
        self.head = new_node
        self.point = new_node

    def visit(self, url: str) -> None:
        new_node = Node(value=url,prev=self.point)
        
        self.point.next = new_node
        
        self.point = new_node
        
        print("None")

    def back(self, steps: int) -> str:
        current = self.point
        
        while steps > 0 and current.prev != None:
            steps -= 1
            current = current.prev
            
        self.point = current
        print(current.value)

    def forward(self, steps: int) -> str:
        current = self.point
        
        while steps > 0 and current.next != None:
            steps -= 1
            current = current.next
            
        self.point = current
        print(current.value)


browserHistory = BrowserHistory("leetcode.com")
browserHistory.visit("google.com")
browserHistory.visit("facebook.com")
browserHistory.visit("youtube.com")
browserHistory.back(1)
browserHistory.back(1)
browserHistory.forward(1)
browserHistory.visit("linkedin.com")
browserHistory.forward(2)
browserHistory.back(2)
browserHistory.back(7)