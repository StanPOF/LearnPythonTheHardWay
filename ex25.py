# -*- coding: utf-8 -*-
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words                 # split函数能通过指定分隔符对字符串进行切片 返回值words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)         # sorted函数可以对list进行排序,函数2返回sorted函数（sorted函数还可以接收一个比较函数实现自定义排序）

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print word                   # pop函数用于移除列表中的一个元素（默认最后一个,元素位置-1）并返回该元素的值

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)         # pop() = pop(-1)
    print word                   # 函数4有返回值,即pop对象

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)     # 先调用函数1,对sentence切片,赋值给words,再返回函数2排序

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)       # 先调用函数1,对sentence切片,赋值给words,再调用函数3,4 此函数返回值是两个

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)       # 先调用函数5,赋值给words,再调用函数3,4 此函数返回值是两个