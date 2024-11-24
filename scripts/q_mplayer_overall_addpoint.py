columns = ['ls','st', 'rs', 'lw', 'lf', 'cf', 'rf', 'rw', 'lam', 'cam', 'ram', 'lm', 'lcm', 'cm', 'rcm', 'rm', 'lwb', 'ldm', 'cdm', 'rdm', 'rwb', 'lb', 'lcb', 'cb', 'rcb', 'rb', 'gk']

qstrings = "SELECT short_name,\n\
                    overall,\n\
                    league_name,\n\
                    club_name,\n\
                    MONTH(fifa_update_date) AS Month,\n\
                    YEAR(fifa_update_date) AS Year,"
for col in columns:
    qstrings += f"""
    CAST(
        CAST(COALESCE(NULLIF(SUBSTR({col}, 1, LENGTH({col}) - 2), ''), '0') AS DECIMAL) +
        CASE 
            WHEN SUBSTR({col}, LENGTH({col}) - 1, 1) = '+' THEN CAST(COALESCE(NULLIF(SUBSTR({col}, LENGTH({col}), 1), ''), '0') AS DECIMAL)
            WHEN SUBSTR({col}, LENGTH({col}) - 1, 1) = '-' THEN -CAST(COALESCE(NULLIF(SUBSTR({col}, LENGTH({col}), 1), ''), '0') AS DECIMAL)
            ELSE 0
        END 
    AS INT) AS {col},"""



qstrings += "\nFROM male_players" 
qstrings += "\nWHERE league_name IN ('Premier League', 'La Liga', 'Ligue 1', 'Serie A')"
qstrings += "\nLIMIT 10" 

