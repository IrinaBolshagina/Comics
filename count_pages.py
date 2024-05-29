import random

def count_pages(num):

    '''calculates number of pages and number of images on each page to make 
    a layout of 2, 3, 4, 5 or 6 images on the page
    gets num - number of photos
    returns list - numbers of images on the pages'''

    lst = [5,4,3]
    lst13 = [5,4,4]

    if num <= 12:
        lst = count_less_12(num)
    else:
        count = int(num/12)
        rest = num%12
        if rest == 1:
            lst = lst * (count - 1) + lst13
        elif rest == 0:
            lst = lst * count
        else:
            lst = lst * count + count_less_12(rest)
    random.shuffle(lst)
    return lst

    
def count_less_12(num):

    '''calculates number of pages for 12 or less photos'''

    lst = [5,4,3]
    if num < 2:
        return 0
    if num == 12:
        return lst
    elif num <= 6:
        return([num])
    elif 6 < num < 12:
        return([5, num - 5])
        
if __name__ == '__main__':
    num = int(input("number of photos: "))
    while num > 0:
        pages = count_pages(num)
        print(pages, sum(pages))
        num = int(input("number of photos: "))
        