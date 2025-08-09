import pandas as pd

def csv_sql(table, dirDF):
    df = pd.read_csv(dirDF)
    sql = """DROP TABLE IF EXISTS """ + table + """;

CREATE TABLE """ + table + """ (
    ID INT PRIMARY KEY,
"""

    types = ["INT", "DECIMAL", "VARCHAR", "TEXT", "DATE", "BOOLEAN"]

    for c in list(df):
        sql += "    " + c + " "
        typo = int(input(f"Seleccione el tipo de datos para { c }:\n{ "\n".join([str(n) + '-' + types[n] for n in range(0, len(types), 1)]) }\n"))
        sql += types[typo]
        if types[typo] == "DECIMAL":
            var = [(len(str(e).replace('-','').replace('.','')), len(str(e).split('.')[1])) for e in list(df[c])]
            sql += str(max(var))
        elif types[typo] == "VARCHAR":
            var = [len(str(u)) for u in list(df[c])]
            sql += "(" + str((max(var)//25)*25 + 25) + ")"
        if len([a for a in list(df[c]) if str(a) != 'nan']) == len(list(df[c])):
            sql += " NOT NULL,\n"
        else:
            sql += ",\n"

    sql += """);

INSERT INTO """ + table + """ (""" + ", ".join(list(df)) + """) VALUES
"""

    for i in range(0, len(df), 1):
        row = "    (" + str(i)
        for j in list(df.iloc[i]):
            row += ", '" + str(j) + "'"
        if i == len(df) -1:
            row += ");"
        else:
            row += "),\n"
        sql += row
    return sql

if __name__ == '__main__':
    table = 'gestoresRCD'
    sql = csv_sql(table, '../DATA/GestoresRCD.csv')
    with open('../DATA/' + table + '.sql', 'w') as file:
        file.write(sql)
    print('Se convirtió el CSV a SQL con exito!')
    print(sql)
