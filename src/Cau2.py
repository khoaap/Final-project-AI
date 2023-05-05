class Node:
    def __init__(self):
        self.identifier: str = ""
        self.value: int = 0

    def __init__(self, indentifier: str):
        self.identifier: str = indentifier
        self.value: int = 0

    def __init__(self, identifier: str, value: int):
        self.identifier: str = identifier
        self.value: int = value 

    def __str__(self) -> str:
        return "(" + self.identifier + ", " + str(self.value) + ")"
    
    
class MinimaxDecision:

    # KHởi tạo các thuộc tính rỗng
    def __init__(self, root: Node = None, terminalStates: dict = {}, successors: dict = {}):
        self.root: Node = root
        self.terminalStates: dict = terminalStates # Dict chứa Node và value 
        self.successors: dict = successors # Dict chứa Node và các successor
    
    def read(self, filename: str):
        treeList: list = [] # Danh sách chứa thông tin file input
        branchList: list = [] # Danh sách chứa các nhánh của cây
        utilList: list = [] # Danh sách chứa giá trị của mỗi Node

        with open(filename, 'r') as file:
            for line in file:
                treeList.append(line)

        successorAmount = int(treeList[0].split()[0]) # Số lượng nhánh của cây
        # utilAmount = int(treeList[0].split()[1])


        """ Xử lý dict terminalStates """
        for index1 in range(1, successorAmount + 1):
            branchList.append(treeList[index1].split())
        for index2 in range(successorAmount + 1, len(treeList)):
            utilList.append(treeList[index2].split())
 
        # Thêm elements vào dict terminalStates
        for element in utilList:
            node = Node(element[0], int(element[1]))
            self.terminalStates[node.identifier] = node.value
        

        """ Xử lý dict successors """
        predecessors = []
        for branch in branchList:
            if branch[0] not in predecessors: 
                predecessors.append(branch[0])

        for node in predecessors:
            successorsList = []
            for branch in branchList:
                if node == branch[0] and node != branch[1]:
                    successorsList.append(branch[1])
                    # branchList.remove(branch)
            self.successors[node] = successorsList
        

    def run(self):
        pass

    # print -> (identifier, value)
    def print(self):
        for key, value in self.terminalStates.items():
            print("(" + key + ", " + str(value) + ")")


if __name__ == "__main__":
    # decision = MinimaxDecision()

    # node1 = Node("n1", 10)
    # node2 = Node("n2", 20)
    # successors = {
    #     node1: [node2],
    #     node2: []
    # }
    # terminalStates = { "n1": 20, "n2": 20 }

    decision = MinimaxDecision()

    decision.read("./src/minimax.txt")

    decision.print()

    