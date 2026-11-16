from pathlib import Path
import weather_math
def get_target() -> tuple[str,str]:
        target = input().split(' ',2)
        return (target[1], target[2])
def get_weather_source() -> None | Path:
    weather = input().split(' ', 2)
    if len(weather) ==2: return None
    return Path(weather[2])
def get_query() -> tuple[list[list[str | int]], list[str]]:
    queries = []
    while True:
        query = input()
        if query == 'NO MORE QUERIES': break
        parts: list[str | int] = list(query.split(' '))
        if query[0] == 'TEMPERATURE':
            parts[3] = int(query[3])
        else:
            parts[1] = int(query[1])
        queries.append(parts)
    reverse = input().split(' ',2)
    return (queries, reverse)
def evaluate_queries(query: list[str | int]) -> :
    
                
                
                    
            
    
        
        
        
    
        
