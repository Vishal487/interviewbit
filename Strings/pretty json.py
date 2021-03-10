def prettyJson(json):
    # write your code here...
    result = []
    multiplier = 0
    i = 0
    
    while i < len(json):
        if json[i] in ['{', '[']:
            result.append('\t' * multiplier + json[i])
            multiplier += 1
            i += 1
        elif json[i] in ['}', ']']:
            multiplier -= 1
            result.append('\t' * multiplier + json[i])
            i += 1
        elif json[i] == ',':
            result[-1]+= ','
            i += 1
        else:
            start = i
            while i < len(json) and json[i] not in ['{', '}', ',', '[', ']']:
                i += 1
            curr_s = json[start:i]
            result.append('\t' * multiplier + curr_s)
    
    return result



if __name__ == '__main__':
    # take inputs...
    json = '{A:"B",C:{D:"E",F:{G:"H",I:"J"}}}'
    
    print(prettyJson(json))
