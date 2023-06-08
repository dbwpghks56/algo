def solution(id_list, report, k):
    answer = {}
    dt = {}
    
    for ids in id_list:
        dt[ids] = []
        answer[ids] = 0
    
    reportdt = {}
    for repor in report:
        reports = repor.split()
        reporter = reports[0]
        reported = reports[1]
        
        if reported not in reportdt:
            reportdt[reported] = []
            reportdt[reported].append(reporter)
            dt[reporter].append(reported)
            
        else:
            if reporter not in reportdt[reported]:
                reportdt[reported].append(reporter)
                dt[reporter].append(reported)
        
        
    for ids in id_list:
        for mem in dt[ids]:
            if k <= len(reportdt[mem]):
                answer[ids] = answer[ids] + 1
        
    return list(answer.values())








