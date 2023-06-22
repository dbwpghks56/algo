def sort_array(arr):
    # 중복 제거를 위해 set으로 변환 후 다시 리스트로 변환
    unique_words = list(set(arr))
    
    # 길이가 짧은 순서대로 정렬, 길이가 같으면 사전 순으로 정렬
    unique_words.sort(key=lambda x: (len(x), x))
    
    return unique_words
print(sort_array(['stayfolio', 'hand', 'curation', 'tuna', 'yes', 'no', 'style', 'stash']))