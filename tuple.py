def get_dta(aTuple):
  nums=()
  words=()
  for t in aTuple:
    nums=nums+(t[0],)
    if t[1] not in words:
      words=words+(t[1],)
    min_nums=min(nums)
    max_nums=max(nums)
    unique_words=len(words)
    return (min_nums,max_nums,unique_words)

(samll,large,words=get_data)