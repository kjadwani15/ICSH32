def get_input():
    while True:
        job_input = input().split(' ',3)
        if len(job_input) !=3 or job_input[1] not in ('NOMINATIM', 'FILE'):
            continue
        
