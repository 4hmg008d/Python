class Tool:

    count = 0

    @classmethod
    def show_tool_count(cls):
        print("Number of Tool object: %d" % cls.count)

    def __init__(self, name):
        self.name = name
        Tool.count += 1


tool1 = Tool("axles")
tool2 = Tool("hammer")
tool3 = Tool("bucket")

Tool.show_tool_count()
