
import random
import matplotlib.pyplot as plt

# Node class for the Binary Search Tree
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# BST class
class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_rec(self.root, key)

    def _insert_rec(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_rec(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_rec(node.right, key)

    def height(self):
        return self._height_rec(self.root)

    def _height_rec(self, node):
        if node is None:
            return 0
        return 1 + max(self._height_rec(node.left), self._height_rec(node.right))

    def imbalance(self):
        if self.root is None:
            return 0
        return abs(self._height_rec(self.root.left) - self._height_rec(self.root.right))

# AVL Tree classes
class AVLNode:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None

class AVLTree:
    def insert(self, root, key):
        if not root:
            return AVLNode(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        if balance > 1 and key < root.left.key:
            return self.rotate_right(root)
        if balance < -1 and key > root.right.key:
            return self.rotate_left(root)
        if balance > 1 and key > root.left.key:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        if balance < -1 and key < root.right.key:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def rotate_left(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def rotate_right(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

def extract_keys_in_order(root):
    if not root:
        return []
    return extract_keys_in_order(root.left) + [root.key] + extract_keys_in_order(root.right)

# Generate and analyze 1000 random BSTs
heights = []
imbalances = []
all_trees = []

for _ in range(1000):
    tree = BST()
    perm = random.sample(range(1, 21), 20)
    for num in perm:
        tree.insert(num)
    heights.append(tree.height())
    imbalances.append(tree.imbalance())
    all_trees.append((tree.imbalance(), perm, tree.height()))

# Plot height histogram
plt.figure()
plt.hist(heights, bins=range(min(heights), max(heights) + 1), edgecolor='black')
plt.title('Histogram of BST Heights')
plt.xlabel('Height')
plt.ylabel('Frequency')
plt.grid(True)
plt.savefig("height_histogram.png")

# Plot imbalance histogram
plt.figure()
plt.hist(imbalances, bins=range(min(imbalances), max(imbalances) + 1), edgecolor='black')
plt.title('Histogram of BST Imbalances')
plt.xlabel('Imbalance (|Left Height - Right Height|)')
plt.ylabel('Frequency')
plt.grid(True)
plt.savefig("imbalance_histogram.png")

# Sort by highest imbalance
most_imbalanced = sorted(all_trees, reverse=True)[:2]

# Rebalance with AVL
avl_tree = AVLTree()
for idx, (imb, perm, h) in enumerate(most_imbalanced, 1):
    root = None
    for key in perm:
        root = avl_tree.insert(root, key)
    print(f"Tree {idx}:")
    print(f"  Original Height: {h}")
    print(f"  Original Imbalance: {imb}")
    print(f"  Balanced Height: {avl_tree.get_height(root)}")
    print(f"  In-Order After AVL: {extract_keys_in_order(root)}")
    print("-" * 50)
