from rolepermissions.roles import AbstractUserRole

class Administrador(AbstractUserRole):
    available_permissions = {
        'create_livro': True,
        'edit_livro': True,
        'delete_livro': True,
        'create_emprestimo': True,
        'edit_emprestimo': True,
        'delete_emprestimo': True,
        'view_emprestimo': True,
        'view_livro': True,
    }

class Leitor(AbstractUserRole):
    available_permissions = {
        'create_emprestimo': True,
        'view_emprestimo': True,
        'view_livro': True,
    }   