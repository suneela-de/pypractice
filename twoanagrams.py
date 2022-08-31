def checkanagram(first,second):
    if len(first)==len(second):
        if sorted(first)==sorted(second):
          print("words are anagram")

    print("not anagram")
checkanagram('cat','actf')