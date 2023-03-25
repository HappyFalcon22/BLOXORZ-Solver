from board_test import *
import math
import random

class MCTS(Game):
    def __init__(self, level) -> None:
        super().__init__(level)
        self.childen = []
        self.parent = None
        self.visited = 0
        self.reward = 0
        self.possible_action = self.get_neighbor()

    # Base on Euclidian distance
    def cal_reward(self):  # ->>>>get reward
        if self.check_win():
            return 20
        x_goal, y_goal = self.goal
        x1, y1 = [self.pos[0], self.pos[1]]
        if len(self.pos) == 2:
            return 20 - math.sqrt((x1-x_goal)**2 + (y1-y_goal)**2)
        if len(self.pos) == 4:
            x2, y2 = [self.pos[2], self.pos[3]]
            dis1 = math.sqrt((x1-x_goal)**2 + (y1-y_goal)**2)
            dis2 = math.sqrt((x2-x_goal)**2 + (y2-y_goal)**2)
            return 20 - 0.5*(dis1+dis2)

    # Expand all legal move from a node
    def get_neighbor(self):
        result = []
        legal_move = self.list_legal_moves()
        for m in legal_move:
            if m == "D":
                nextMove = copy.deepcopy(self)
                nextMove = nextMove.right()
            if m == "S":
                nextMove = copy.deepcopy(self)
                nextMove = nextMove.down()
            if m == "A":
                nextMove = copy.deepcopy(self)
                nextMove = nextMove.left()
            if m == "W":
                nextMove = copy.deepcopy(self)
                nextMove = nextMove.up()
            nextMove.parent = self
            result.append(nextMove)
        return result

    def backup(self):
        while self is not None:
            self.reward += self.cal_reward()
            self.visited += 1
            self = self.parent

    def add_child(self,child):
        self.childen.append(child)

    def best_neighbor(self, exploration_param = 1.4):
        best_neighbor = None
        best_score = -float("inf")
        for node in self.childen():
            exploitation_score = node.reward/node.visited
            exploration_score = exploration_param * math.sqrt(math.log(self.visited)/node.visited)
            total_score =  exploitation_score + exploration_score
            if total_score > best_score:
                best_score = total_score
                best_neighbor = node
        return best_neighbor
    
    def default_policy(self):
        node = copy.deepcopy(self)
        while not node.check_win() and len(node.possible_action) > 0:
            if len(node.possible_action) > 0:
                n = random.randint(0,len(self.possible_action)-1)
                node = node.possible_action[n]
        return node.cal_reward()

    def select_untried_action(self):
        while not self.check_win():
            untried = list(set(self.possible_action) - set(self.childen))
            if len(untried) > 0:
                return untried[0]
            else:
                return None
        return None   
    def tree_policy(self):
        while not self.check_win():
            node = self.select_untried_action()
            if node is not None:
                self.childen.append(node)
                return node
            else:
                node = self.best_neighbor()
        return self            
    def MCTS(self):
        for i in range(5):
            node = self.tree_policy()
            reward = self.default_policy()
            self.backup()
        return self.best_neighbor()
    def solve(self):
        finish = self.MCTS()
        result = []
        while finish.parent is not None:
            result.append(finish.pos)
            finish = finish.parent
        return result
# function monte_carlo_tree_search(initial_state):
#     root_node = Node(state=initial_state)
#     while not stop_condition_met():
#         selected_node = selection(root_node)
#         if selected_node.is_terminal():
#             rollout_result = selected_node.get_terminal_reward()
#         else:
#             expanded_node = expansion(selected_node)
#             rollout_result = simulation(expanded_node)
#         backpropagation(expanded_node, rollout_result)
#     return best_child(root_node)

# class Node:
#     def __init__(self, state):
#         self.state = state
#         self.children = []
#         self.parent = None
#         self.visits = 0
#         self.reward = 0

#     def is_fully_expanded(self):
#         return len(self.children) == len(self.state.get_possible_actions())

#     def is_terminal(self):
#         return self.state.is_terminal()   ---> check_win()

#     def get_terminal_reward(self):
#         return self.state.get_reward()

#     def add_child(self, child_state):
#         child_node = Node(child_state)
#         child_node.parent = self
#         self.children.append(child_node)

#     def update(self, reward):
#         self.visits += 1
#         self.reward += reward

#     def get_ucb1_score(self, exploration_parameter):
#         exploitation_score = self.reward / self.visits
#         exploration_score = exploration_parameter * np.sqrt(np.log(self.parent.visits) / self.visits)
#         return exploitation_score + exploration_score

# class State:
#     def __init__(self, grid, position):
#         self.grid = grid
#         self.position = position

#     def get_possible_actions(self):
#         # Returns a list of possible actions for the current state

#     def perform_action(self, action):
#         # Returns a new state after performing the given action

#     def is_terminal(self):
#         # Returns whether the current state is a terminal state

#     def get_reward(self):
#         # Returns the reward for the current state

# def selection(node):
#     while not node.is_terminal():
#         if not node.is_fully_expanded():
#             return expansion(node)
#         else:
#             node = best_child(node)
#     return node

# def expansion(node):
#     untried_actions = [action for action in node.state.get_possible_actions() if action not in [child.state.last_action for child in node.children]]
#     action = random.choice(untried_actions)
#     new_state = node.state.perform_action(action)
#     node.add_child(new_state)
#     return node.children[-1]

# def simulation(node):
#     state = node.state
#     while not state.is_terminal():
#         action = random.choice(state.get_possible_actions())
#         state = state.perform_action(action)
#     return state.get_reward()

# def backpropagation(node, reward):
#     while node is not None:
#         node.update(reward)
#         node = node.parent

# def best_child(node):
#     exploration_parameter = np.sqrt


# function best_child(node, exploration_parameter):
#     best_child_node = None
#     best_score = -infinity
#     for child_node in node.children:
#         exploitation_score = child_node.total_reward / child_node.visits
#         exploration_score = exploration_parameter * sqrt(log(node.visits) / child_node.visits)
#         score = exploitation_score + exploration_score
#         if score > best_score:
#             best_score = score
#             best_child_node = child_node
#     return best_child_node
