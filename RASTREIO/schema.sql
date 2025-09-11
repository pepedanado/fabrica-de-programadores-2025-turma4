CREATE TABLE IF NOT EXISTS encomendas(
    id INTEGER PRIMARY KEY ASC AUTOINCREMENT,
    produto VARCHAR(400),
    endereco VARCHAR(400),
    meio VARCHAR(250),
    data_hora TEXT
);