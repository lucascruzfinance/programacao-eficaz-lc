import sqlite3

# Nome do banco de dados, na raiz do repositório
DB_NAME = "banco.db"


class Note:
    """Representa uma anotação.

    Os nomes dos atributos ficam em português (titulo, detalhes) porque são
    usados na interface, enquanto as colunas do banco ficam em inglês
    (title, content), como é convenção em bancos relacionais.
    """

    def __init__(self, id, titulo, detalhes, favorito=False):
        self.id = id
        self.titulo = titulo
        self.detalhes = detalhes
        self.favorito = favorito


def get_connection():
    # Abre uma conexão com o banco de dados
    conexao = sqlite3.connect(DB_NAME)
    # Permite acessar as colunas pelo nome (ex.: linha["title"])
    conexao.row_factory = sqlite3.Row
    return conexao


def init_db():
    # Cria a tabela "note" caso ela ainda não exista
    conexao = get_connection()
    cursor = conexao.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS note (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT,
            favorite INTEGER NOT NULL DEFAULT 0
        )
        """
    )
    conexao.commit()
    conexao.close()


def load_template(nome_arquivo):
    # Constrói o caminho completo: "static/templates/" + nome do arquivo
    caminho = f"static/templates/{nome_arquivo}"

    # Abre o arquivo em modo leitura ("r" = read)
    arquivo = open(caminho, "r", encoding="utf-8")

    # Lê todo o conteúdo do arquivo
    conteudo = arquivo.read()

    # Fecha o arquivo
    arquivo.close()

    # Devolve o conteúdo como string
    return conteudo


def load_notes():
    # Lê todas as anotações do banco de dados.
    # As favoritas (favorite = 1) aparecem antes das não favoritas.
    conexao = get_connection()
    cursor = conexao.cursor()
    cursor.execute(
        "SELECT id, title, content, favorite FROM note "
        "ORDER BY favorite DESC, id ASC"
    )
    linhas = cursor.fetchall()
    conexao.close()

    # Transforma cada linha do banco em um objeto Note
    return [
        Note(linha["id"], linha["title"], linha["content"], bool(linha["favorite"]))
        for linha in linhas
    ]


def get_note(note_id):
    # Recebe o id de uma anotação e retorna essa anotação como objeto Note.
    conexao = get_connection()
    cursor = conexao.cursor()
    cursor.execute(
        "SELECT id, title, content, favorite FROM note WHERE id = ?",
        (note_id,),
    )
    linha = cursor.fetchone()
    conexao.close()

    if linha is None:
        return None

    return Note(linha["id"], linha["title"], linha["content"], bool(linha["favorite"]))


def insert_note(titulo, detalhes):
    # Insere uma nova anotação no banco. O id é gerado automaticamente.
    conexao = get_connection()
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO note (title, content) VALUES (?, ?)",
        (titulo, detalhes),
    )
    conexao.commit()
    conexao.close()


def update_note(note_id, titulo, detalhes):
    # Atualiza o título e o conteúdo de uma anotação existente.
    conexao = get_connection()
    cursor = conexao.cursor()
    cursor.execute(
        "UPDATE note SET title = ?, content = ? WHERE id = ?",
        (titulo, detalhes, note_id),
    )
    conexao.commit()
    conexao.close()


def delete_note(note_id):
    # Remove uma anotação do banco de dados.
    conexao = get_connection()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM note WHERE id = ?", (note_id,))
    conexao.commit()
    conexao.close()


def toggle_favorite(note_id):
    # Alterna o estado de favorito: 0 vira 1 e 1 vira 0.
    conexao = get_connection()
    cursor = conexao.cursor()
    cursor.execute(
        "UPDATE note SET favorite = 1 - favorite WHERE id = ?",
        (note_id,),
    )
    conexao.commit()
    conexao.close()
