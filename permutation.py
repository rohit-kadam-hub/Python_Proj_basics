result=list()
def generator(string,start,end):
    current=0
    if start==end-1:
        if not string in result:
            result.append(string)

    else:
        for current in range(start,end):
            x=list(string)
            temp=x[start]
            x[start]=x[current]
            x[current]=temp
            generator("".join(x),start+1,end)
            temp=x[start]
            x[start]=x[current]
            x[current]=temp
            
            
def main():
    string="123"
    length=len(string)
    generator(string,0,length)
    print(result)


if __name__== "__main__":
    main()


