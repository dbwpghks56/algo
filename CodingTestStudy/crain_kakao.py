def solution(board, moves):
    answer = []
    count = 0
    for move in moves:
        row_count = 0
        col = move -1
        while True:
            if row_count < len(board):
                cur = board[row_count][col]
                if cur != 0:
                    board[row_count][col] = 0
                    if not answer:
                        answer.append(cur)
                        break
                    else:
                        if answer[-1] == cur:
                            count += 2
                            answer.pop()
                            break
                        else:
                            answer.append(cur)
                            break
                
                row_count += 1
                
            else:
                break
    
    return count








