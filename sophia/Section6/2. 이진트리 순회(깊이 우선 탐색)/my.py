import sys, os
sys.stdin = open(f'{os.path.dirname(os.path.realpath(__file__))}/input.txt', "rt")

def preorder(x):
    if x > 7:
        return 
    else:
        print(x, end = ' ')
        preorder(x * 2)
        preorder(x*2+1)

def inorder(x):
    if x > 7:
        return 
    else:
        inorder(x * 2)
        print(x, end = ' ')
        inorder(x*2+1)

def postorder(x):
    if x > 7:
        return 
    else:
        postorder(x * 2)
        postorder(x*2+1)
        print(x, end = ' ')   

if __name__ == "__main__":
    preorder(1)
    print()
    inorder(1)
    print()
    postorder(1)