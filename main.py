import sys

def oneToOne(s1, s2):
    dict = {}
    if (len(s1) == len(s2)) and s1 and s2:
        for x in range(0, len(s1)):
            if s1[x] in dict:
                if dict.get(s1[x]) is not s2[x]:
                    return "false"
            else:
                dict[s1[x]] = s2[x]
        return "true"
    else:
        return "false"



print(oneToOne(sys.argv[1],sys.argv[2]))