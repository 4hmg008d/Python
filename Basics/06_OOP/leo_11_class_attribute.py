class Tool(object):

    count = 0

    def __init__(self, name):
        self.name = name

        Tool.count += 1


tool1 = Tool("axies")
tool2 = Tool("hammer")
tool3 = Tool("bucket")

print(Tool.count)