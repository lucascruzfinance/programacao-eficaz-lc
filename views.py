from utils import load_data, load_template, save_data

def index():
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title=dados['titulo'], details=dados['detalhes'])
        for dados in load_data('notes.json')
    ]
    notes = '\n'.join(notes_li)
    
    return load_template('index.html').format(notes=notes)

def submit(titulo, detalhes):
    # Carrega as anotações existentes
    notas = load_data('notes.json')
    
    # Cria um novo dicionário com a nova anotação
    nova_nota = {
        'titulo': titulo,
        'detalhes': detalhes
    }
    
    # Adiciona a nova nota à lista
    notas.append(nova_nota)
    
    # Salva a lista atualizada no arquivo
    save_data('notes.json', notas)