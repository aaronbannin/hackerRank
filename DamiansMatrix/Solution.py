# Damian's Matrix

############################################################
# M = NxN matrix where each cell contains one letter
# W = List of words
#
# We are going to create words by moving through the matrix.
# Within the matrix, you can only move one cell at a time in any direction. You can change direction at any time.
#
# -------
# |C|A|R|
# -------
# |B|A|M|
# -------
# |N|S|T|
# -------
#
# In the above example:
# CAT is formed by starting in the upper left then moving down to the right in a diagnal.
# MAT is formed by starting at the end of the second row, moving to the center, then to the bottom left.
#
# Write a function to takes an array of words (W) of length K and determines if the word can be formed using matrix M.
############################################################

# Create a trie for W
# Traverse M using two pointers, compare against Trie on each iteration

class Node(object):
    def __init__(self, value, children={}):
        # (String, Dict(Node)) -> Node
        self.value = value
        self.word = ""
        self.children = {}

    def __str__(self):
        return "Node value={} word={} children={}".format(self.value, self.word, str(self.children))

class WordMap(object):
    """
    A Trie data structure
    """
    def __init__(self, array_of_words):
        # (List(String)) -> WordMap
        self.head = {}

        current_node = None
        for word in array_of_words:
            self.add_word(word)

    def dump(self):
        # print('dump begin data={}'.format(str(self.head)))
        def print_children(letter, node, word=''):
            # print('letter={} word={}'.format(letter, word))
            print(node)
            if len(node.children) > 0:
                for letter, child in node.children.items():
                    print_children(letter, child, word + letter)

        for letter, child in self.head.items():
            print_children(letter, child, letter)

    def add_word(self, word):
        print('add_word begin word={}'.format(word))
        index = 0
        current_children = self.head
        for index in range(len(word)):
            print('letter loop begin letter={}'.format(word[index]))
            letter = word[index]
            if letter not in current_children:
                new_node = Node(letter)
                current_children[letter] = new_node
                current_children = new_node.children
                if index is len(word)-1:
                    new_node.word = word
            else:
                if index is len(word)-1:
                    current_children[letter].word = word
                current_children = current_children[letter].children


    def does_word_exist(self, word):
        # (String) -> Bool
        current_children = self.head
        for index in range(len(word)):
            try:
                current_children = current_children[word[index]].children
            except:
                # print('letter not found word={} letter={}'.format(word, word[index]))
                return False
        return True

    def verify_step(self, letter, node=None):
        # (Node, String) throws -> Node
        # if the requested letter is in children, return the next node
        if node is None:
            return self.head[letter]
        else:
            return node.children[letter]



class LetterMatrix(object):
    def __init__(self, matrix):
        # takes in a 2-dimensional array representing an NxN matrix
        self.matrix = matrix
        self.x = 0
        self.y = 0
        self.max_coordinate = len(self.matrix)
        self.found_words = set()
        self.frontier = []

    def _get_next_moves(self, x, y, indicies_visited):
        #() -> [(int, int)]
        # repeated code here, surely there is a more elegant way to write these functions
        array_of_x = self._generate_coordinate_values(x)
        array_of_y = self._generate_coordinate_values(y)
        return [(x, y) for x in array_of_x for y in array_of_y if (x, y) not in indicies_visited]

    def _generate_coordinate_values(self, input_value):
        return [x for x in range(input_value-1, input_value+2) if x >= 0 and x < self.max_coordinate]

    def walk(self, word_map, x, y, word='', indicies_visited=set(), next_node=None):
        # letter = self.current_letter()
        letter = self.matrix[y][x]
        print('walk begin word={} letter={} indicies_visited={}'.format(word, letter, indicies_visited))

        if (x, y) in indicies_visited:
            print('Already visited index={}'.format((x, y)))
            return
        else:
            # indicies_visited.append((x, y))
            updated_path = set(indicies_visited)
            updated_path.add((x, y))
        try:

            next_node = word_map.verify_step(letter, next_node)
            # print('next_node={}'.format(next_node))
            word += letter
            if len(next_node.children) is 0 or next_node.word is not "":
                print('word={} found!'.format(word))
                self.found_words.add(word)
                # return

            next_moves = self._get_next_moves(x, y, updated_path)
            print('walk found letter, word is now={} next_moves={} path={}'.format(word, next_moves, updated_path))
            for move in next_moves:
                new_x, new_y = move
                # print('x={} y={}'.format(new_x, new_y))
                self.walk(word_map, new_x, new_y, word, updated_path, next_node)
            # return
        except:
            print('cannot complete word letter={} x={} y={}'.format(letter, x, y))
            return

    # def walk_frontier(self, word_map, word, next_node=None):
    #     while self.frontier:
    #         coordinate = self.frontier.pop()
    #         letter = self.matrix[y][x]
    #         try:
    #             next_node = word_map.verify_step(letter, node=next_node
    #             word += letter




    def current_letter(self):
        return self.matrix[self.y][self.x]


def Solution(input_matrix, list_of_words):
    word_map = WordMap(list_of_words)
    letter_matrix = LetterMatrix(input_matrix)
    # print('dump word_map')
    # print(word_map.dump())

    for x in range(len(input_matrix)):
        for y in range(len(input_matrix)):
            print('begin walk x={} y={}'.format(x, y))
            letter_matrix.walk(word_map, x, y)

    print(letter_matrix.found_words)
