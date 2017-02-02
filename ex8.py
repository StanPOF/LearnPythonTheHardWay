# -*- coding: utf-8 -*-
formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")  # 这里输出结果是'one' 'two' 'three' 'four'
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter %(
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)

# %r有时打印出来是单引号，而实际用的是双引号是因为python会用最有效的方式输出字符串,这对于%r是可接受的因为是用于调试。