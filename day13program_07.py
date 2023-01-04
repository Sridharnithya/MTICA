def demo_yield():
    a='Python'
    print("code segment1 executed",a)
    yield len(a)
    b='Java'
    print("code segment2 executed",b)
    yield 2
    print("code segment1 executed",c)
    yield 3
    print("code segment4 executed",d)
if __name__=="__main__":
    x=demo_yield()
    print(next(x))
    print(next(x))
    print(next(x))
