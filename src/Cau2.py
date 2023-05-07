class Node:
    def __init__(self):
        self.identifier: str = ""
        self.value: int = 0

    def __init__(self, indentifier: str):
        self.identifier: str = indentifier
        self.value: int = 0

    def __init__(self, identifier: str, value: int = None):
        self.identifier: str = identifier
        self.value: int = value

    def __str__(self) -> str:
        return "(" + self.identifier + ", " + str(self.value) + ")"


class TreeNode:
    def __init__(self, node):
        self.node = node
        self.children = []

    def add_child(self, child: 'TreeNode'):
        self.children.append(child)

    def build_tree(self, terminalStates, successors):
        if self.node.identifier in successors:
            for successor in successors[self.node.identifier]:
                child_node = Node(successor)
                if successor in terminalStates:
                    child_node.value = terminalStates[successor]
                child = TreeNode(child_node)
                child.build_tree(terminalStates, successors)
                self.add_child(child)

    def print_tree(self):
        print(str(self.node))
        for child in self.children:
            child.print_tree()


class MinimaxDecision:

    # KHởi tạo các thuộc tính rỗng
    def __init__(self, root: Node = None, terminalStates: dict = {}, successors: dict = {}):
        self.root: Node = root
        self.terminalStates: dict = terminalStates  # Dict chứa Node và value
        self.successors: dict = successors  # Dict chứa Node và các successor
        self.tree: TreeNode = None

    def read(self, filename: str):
        treeList: list = []  # Danh sách chứa thông tin file input
        branchList: list = []  # Danh sách chứa các nhánh của cây
        utilList: list = []  # Danh sách chứa giá trị của mỗi Node

        with open(filename, 'r') as file:
            for line in file:
                treeList.append(line)

        successorAmount = int(treeList[0].split()[0])  # Số lượng nhánh của cây

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
            self.successors[node] = successorsList

        # Xác định node root
        root_identifier = "n00"
        self.root = Node(root_identifier, None)
        # print(self.root)
        # Gán giá trị cho root nếu nó là terminal state
        if root_identifier in self.terminalStates:
            self.root.value = self.terminalStates[root_identifier]
        # Xây dựng cây và cập nhật successors
        self.tree = TreeNode(self.root)
        self.tree.build_tree(self.terminalStates, self.successors)

    def run(self):
        self.minimax(self.tree, True)

    def minimax(self, node, maximizingPlayer):
        if not node.children:  # node is a leaf
            return node.node.value
        if maximizingPlayer:
            best_value = -float("inf")
            for child in node.children:
                v = self.minimax(child, False)
                best_value = max(best_value, v)
                node.node.value = best_value
            return best_value
        else:  # minimizing player
            best_value = float("inf")
            for child in node.children:
                v = self.minimax(child, True)
                best_value = min(best_value, v)
                node.node.value = best_value
            return best_value

    # print -> (identifier, value)
    def print(self):
        self.tree.print_tree()


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

    decision.read("minimax.txt")

    decision.run()
    decision.print()
   # decision.print_successors(decision.root)
   # decision.printterminalStates()
