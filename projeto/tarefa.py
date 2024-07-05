class Tarefa:
    def __init__(self,descicao):#4
        self.descricao = descicao

    def __repr__(self):
        return self.descricao
    @staticmethod
    def from_string(task_str):#5
        return Tarefa(task_str)