str1 = "hello hello python"
str2 = 'My nickname is "Watermelon"'
poem = ["登鹳雀楼",
        "王之涣",
        "白日依山尽",
        "黄河入海流",
        "欲穷千里目",
        "更上一层楼"]
print(str2)
print(str1[6])

print(len(str2))
print(str1.count("llo"))
print(str2.index('o'))

for char in poem:
    print("|%s||%s||%s|" % (char.ljust(10, "　"),
                            char.center(10, "　"),
                            char.rjust(10, "　")))


# if there are spaces
poem2 = ["登鹳雀楼",
         "\t王之涣",
         "白日依山尽\r",
         "黄河入海流",
         "欲穷千里目\n",
         "更上一层楼"]

for char in poem2:
    print("|%s|" % char.strip().center(10, "　"))
