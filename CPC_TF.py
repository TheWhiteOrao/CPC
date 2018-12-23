engine_min = 1.100
engine_max = 1.940
engine_cp = 0.25
engine_range = engine_max - engine_min
engine_cs = engine_range * (1 - engine_cp) + engine_min
engine_cp_range = engine_range * engine_cp
print(engine_cs, engine_cp_range)
