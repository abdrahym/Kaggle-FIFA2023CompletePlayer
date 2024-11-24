columns = ['ls','st', 'rs', 'lw', 'lf', 'cf', 'rf', 'rw', 'lam', 'cam', 'ram', 'lm', 'lcm', 'cm', 'rcm', 'rm', 'lwb', 'ldm', 'cdm', 'rdm', 'rwb', 'lb', 'lcb', 'cb', 'rcb', 'rb', 'gk']

qstrings = "SELECT short_name,\n\
                    overall,\n\
                    league_name,\n\
                    club_name,\n\
                    MONTH(fifa_update_date) AS Month,\n\
                    YEAR(fifa_update_date) AS Year"
for col in columns:
    qstrings += f""",
    CASE 
        WHEN INSTR({col}, '+') > 0 THEN SUBSTR({col}, 1, INSTR({col}, '+') - 1)
        WHEN INSTR({col}, '-') > 0 THEN SUBSTR({col}, 1, INSTR({col}, '-') - 1)
        ELSE {col}
    END AS {col}"""

qstrings += "\nFROM male_players" 
qstrings += "\nWHERE league_name IN ('Premier League', 'La Liga', 'Ligue 1', 'Serie A')"

