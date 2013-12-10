class Node:
    def __init__(self, name):
        self.name = name
        self.label = None
        self.decisionAttr = None
        self.branches = []


# Returns the root node of the constructed decision tree
def constructDecisionTree(examples, targetAttribute, attributes):
    root = Node('Decision Tree Root')

    # Examples are all positive
    if all(example.label == '+' for example in examples):
        root.label = '+'
        return root

    # Examples are all negative
    elif all(example.label == '-' for example in examples):
        root.label = '-'
        return root

    # Attributes is empty
    elif not attributes:
        root.label = getMostCommonLabel(examples)
        return root
    else:
        attr = getHighestInfoGainAttr(attributes, examples)
        root.decisionAttr = attr
        possibleValues = uniqueValues(attr, examples)

        for value in possibleValues:
            newBranch = Node(attr + ' = ' + value)
            root.branches.append(newBranch)
            branchExamplesGen = (row for row in examples if row[attr] == value)
            branchExamples = sorted(branchExamplesGen)

            if not branchExamples:
                leaf = Node(getMostCommonValue(targetAttribute, examples, possibleValues))
                newBranch.branches.append(leaf)


# Returns the most common label (+ or -) in the given list of nodes
def getMostCommonLabel(nodes):
    pCount = 0
    nCount = 0

    for node in nodes:
        if node.label == '+':
            pCount += 1
        elif node.label == '-':
            nCount += 1

    if pCount >= nCount:
        return '+'
    else:
        return '-'


# Returns the attribute from attributes with the highest information gain that best classifies examples.
# TODO: implement
def getHighestInfoGainAttr(attributes, examples):
    return attributes[0];


# Returns a list of the unique values of the given attribute in the given examples
# TODO: implement
def uniqueValues(attr, examples):
    return []


# Returns the most common value of the attribute in the examples
# Values param is the possible value for that attribute
def getMostCommonValue(attr, examples, values):
    valueCounts = []

    for value in values:
        valueCount = 0
        for example in examples:
            if example[attr] == value:
                valueCount += 1
        valueCounts.append(valueCount)

    maxIndex = valueCounts.index(max(valueCounts))
    return values[maxIndex]