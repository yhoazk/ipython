#!/usr/bin/python

def count_words(s,n):
    d = [] # create empty list
    wls = s.split(" ")
    uniq = set(wls) # eliminate duplicateds
    for i in uniq:
        d.append((i, wls.count(i)))
    print d

    #sort the set
    d = sorted(sorted(d, key=lambda nm: nm[0]), key= lambda cnt: cnt[1], reverse=True)
    return d[:n]

def main():
    s = raw_input().strip()
    n = int(raw_input().strip())
    li = count_words(s, n)
    print li



if __name__ == "__main__":
    main()
