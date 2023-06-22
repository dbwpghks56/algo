def unique(arr):
    # 짝수 카운트
    odd_count = 0
    # 홀수 카운트
    even_count = 0
    # 홀수 인덱스
    odd_index = 0
    # 짝수 인덱스
    even_index = 0
    
    # 인덱스와 벨류를 동시에 가져오기 위해 enumerate 를 사용
    for idx, value in enumerate(arr):
        # 어차피 짝수나 홀수가 하나만 존재하기 때문에 덮어씌워도 무리가 없다.
        # 짝수가 나오는 경우 카운트 추가 및 인덱스를 덮어씌우기
        if value % 2 == 0:
            even_count += 1
            even_index = idx
        # 홀수가 나오는 경우 카운트 추가 및 인덱스를 덮어씌우기
        else:
            odd_count += 1
            odd_index = idx
        
        # 비교해서 홀수가 1이면 홀수 인덱스 반환
        if (even_count > 1 and odd_count == 1):
            return odd_index
        # 반대의 경우
        elif( even_count == 1 and odd_count > 1):
            return even_index
        
print(unique([2, 4, 7, 8, 10]))