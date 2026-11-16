from datetime import datetime, timezone

def f_to_c(temp_f: float) -> float:
    return (temp_f-32)*(5/9)
def c_to_f(temp_c: float) -> float:
    return (temp_c * (9 / 5)) + 32
def feels_like_temp(temp: float, humidity: float, wind: float) -> float:
    if temp >= 68.0:
        return (-42.379 + 2.04901523*temp + 10.14333127*humidity -0.22475541*temp*humidity
        -0.00683783*(temp**2) -0.05481717*(humidity**2) + 0.00122874*(temp**2)*humidity
        +0.00085282*temp*(humidity**2)-0.00000199*(temp**2)*(humidity**2))
    elif temp <= 50.0 and wind>3.0:
        return (35.74 + 0.6215*temp -35.75*(wind**.16) + 0.4275*temp*(wind**0.16))
    else:
        return temp
def coordinate_format(latitiude: float, longitude: float) -> tuple[str, str]:
    coord_lat = ''
    coord_long = ''
    if latitiude < 0.0:
        coord_lat = f'{abs(latitiude)}/S'
    else:
        coord_lat = f'{latitiude}/N'
    if longitude < 0.0:
        coord_long = f'{abs(longitude)}/W'
    else:
        coord_long = f'{longitude}/E'
    return (coord_lat, coord_long)
def polygon_centroid(NWS_coords: list[list[float]]) -> tuple[float, float]:
    no_dup = set()
    total_x=0
    total_y=0
    for coord in NWS_coords: no_dup.add(tuple(coord))
    for coord in no_dup:
        total_x+=coord[0]
        total_y+=coord[1]
    return ((total_y/(len(no_dup)), (total_x/(len(no_dup)))))
def convert_timestamp(iso: str) -> str:
    date_time = datetime.fromisoformat(iso)
    utc_date_time = date_time.astimezone(timezone.utc)
    return utc_date_time.strftime(f'%Y-%m-%dT%H:%M:%SZ')




        
