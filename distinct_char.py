def distinct_substring(s1,k):
    upper=1
    check=''
    max_len=-10
    check=s1[0]
    m=1
    while m<=len(s1)-1:
        substring=s1[m]
        if len(set(check))<=k:
            check+=substring
        if m==len(s1)-1:
            pattern.append(check)
        if len(set(check))>k:
            check=check[:-1]
            max_len=max(max_len,len(check))
            pattern.append(check)
            check=s1[m]
    m=m+1
    if m==len(s1):
        max_len=-1
        for m in range(len(pattern)):
            max_len=max(current_len,len(pattern[m]))
        return max_len
    continue
