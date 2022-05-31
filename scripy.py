import resource
import time
start = time.time()

with open('input.txt') as csv_file:
    deal_list = []
    for row in csv_file:
        deal_id = row.split(',')[0]
        deal_list.append(deal_id)
    deal_list = set(deal_list)
    deal_list = list(deal_list)
    deal_list.remove('deal_id')

with open('input.txt') as csv_file:
    for row in csv_file:
        deal_id = row.split(',')[0]
        for id in deal_list:
            if deal_id == id:
                file = id + '.txt'
                with open(file, "a") as f:
                    f.write(f"{row}\n")
end = time.time()
duration = end - start

print('Peak Memory Usage (KB) = ', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
print('Script execution time (s) = ',duration)
print('User Mode Time (s) = ', resource.getrusage(resource.RUSAGE_SELF).ru_utime)
print('System Mode Time (s) = ', resource.getrusage(resource.RUSAGE_SELF).ru_stime)
