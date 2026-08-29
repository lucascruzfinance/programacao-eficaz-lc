import html

from utils import (
    load_template,
    load_notes,
    get_note,
    insert_note,
    update_note,
    delete_note,
    toggle_favorite,
)


def index():
    note_template = load_template('components/note.html')

    notes_li = []
    for nota in load_notes():
        notes_li.append(
            note_template.format(
                id=nota.id,
                title=nota.titulo,
                details=nota.detalhes,
                # Estrela cheia se favorita, vazia caso contrário
                fav_icon='★' if nota.favorito else '☆',
                # Classe extra usada pelo CSS para destacar a nota favorita
                fav_class='favorited' if nota.favorito else '',
            )
        )

    notes = '\n'.join(notes_li)

    return load_template('index.html').format(notes=notes)


def submit(titulo, detalhes):
    # Cria uma nova anotação no banco de dados
    insert_note(titulo, detalhes)


def edit_page(note_id):
    # Monta a página de edição com o título e o conteúdo já preenchidos
    nota = get_note(note_id)

    return load_template('edit.html').format(
        id=nota.id,
        # Escapa aspas/sinais para não quebrar o atributo value="..."
        title=html.escape(nota.titulo, quote=True),
        details=html.escape(nota.detalhes, quote=True),
    )


def update(note_id, titulo, detalhes):
    # Salva as alterações da anotação no banco de dados
    update_note(note_id, titulo, detalhes)


def delete(note_id):
    # Apaga a anotação do banco de dados
    delete_note(note_id)


def favorite(note_id):
    # Favorita ou desfavorita a anotação
    toggle_favorite(note_id)
