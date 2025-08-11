import pandas as pd

def noSymbol(txt):
    symbols = ["(", ")", "/"]
    ans = txt
    for s in symbols:
        ans = ans.replace(s, "")
    return ans

def csv_sql(table: str, dirDF: str):
    df = pd.read_csv(dirDF)
    sql = "DROP TABLE IF EXISTS " + table + ";\n\n"
    sql += """CREATE TABLE """ + table + """ (
    ID SERIAL PRIMARY KEY"""

    types = ["INT", "DECIMAL", "VARCHAR", "TEXT", "DATE", "BOOLEAN"]

    for c in list(df):
        sql += ",\n    " + noSymbol(c).replace(" ", "_") + " "
        options = "\n".join([str(n) + '-' + types[n] for n in range(0, len(types), 1)])
        typo = int(input(f"Seleccione el tipo de datos para '{ c }':\n{ options }\n"))

        if types[typo] == "DECIMAL":
            var = list()
            for e in list(df[c]):
                try:
                    var.append((len(str(e).replace('-','').replace('.','')), len(str(e).split('.')[1])))
                except IndexError:
                    pass
            sql += types[typo] + str(max(var))
        elif types[typo] == "VARCHAR" or types[typo] == "TEXT":
            var = [len(str(u)) for u in list(df[c])]
            if (max(var)//25)*25 + 25 >= 300:
                sql += "TEXT"
            else:
                sql += "VARCHAR(" + str((max(var)//25)*25 + 25) + ")"
        else:
            sql += types[typo]

        if len([a for a in list(df[c]) if str(a) != 'nan']) == len(list(df[c])):
            sql += " NOT NULL"

    sql += """\n);

INSERT INTO """ + table + """ (""" + ", ".join([noSymbol(t).replace(" ", "_") for t in list(df)]) + """) VALUES
"""

    for i in range(0, len(df), 1):
        row = "    ('" + list(df.iloc[i])[0] + "'"
        for j in list(df.iloc[i])[1::]:
            row += ", '" + str(j) + "'"
        if i == len(df) -1:
            row += ");"
        else:
            row += "),\n"
        sql += row.replace("nan", "")
    return sql

if __name__ == '__main__':
    table = 'itemsEjec'
    sql = csv_sql(table, '../DATA/itemsEjec.csv')
    with open('../DATA/' + table + '.sql', 'w') as file:
        file.write(sql)
    print(sql)
    print('Se convirtió el CSV a SQL con exito!')
