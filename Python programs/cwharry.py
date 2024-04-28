# write a program for coding and decoding
st = input("Enter your message:-")
words = st.split(" ")
coding  = input("1 for coding or 0 for decoding")
coding = True if (coding == "1") else False
print(coding)
if(coding):
    nwords = [ ]
    for word in words:
        if(len(word)>=3):
            r1 = "dsf"
            r2 = "jkr"
            stnew = r1 + word[1:] + word[0] + r2
            nwords.append(stnew)
        
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))
else:
    nwords = [ ]
    for word in words:
        if(len(word)>=3):
            stnew = word[3:-3]  # here we are reversing the string
            stnew = stnew[-1] + stnew[:-1]  # here we are adding the last term of string to the first place.
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
print(" ".join(nwords))
