from sqlalchemy import create_engine, Column, Integer , String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

engine = create_engine("sqlite:///escola.db")
Base = declarative_base()
Session = sessionmaker(bind=engine)

class Professor(Base):
    __tablename__= "professor"

    id = Column(Integer,primary_key=True)
    nome = Column(String(100),nullable=False)
    materia = Column(String(100))
    alunos = relationship("Alunos", back_populates="professor", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Professor(id={self.id}, nome='{self.nome}')>"
    
class Alunos(Base):
    __tablename__ = "alunos"

    id = Column(Integer,primary_key=True)
    nome = Column(String(100),nullable=False)
    RA = Column(Integer)
    idade = Column(Integer)

    professor_id = Column(Integer, ForeignKey("professor.id"), nullable=False)

    professor =relationship("Professor", back_populates="alunos")
    def __repr__(self):
        return f"<Materias(nome='{self.nome}',professor_id={self.professor_id},aulas_id={self.aulas_id})>"
    
Base.metadata.create_all(engine)

def inserir_professor():
    with Session() as session:
        try:
            nome_professor = input("Digite o nome do professor: ").capitalize()
            nome_materia = input("Digite qual a materia: ").capitalize()

            professor = Professor(nome=nome_professor, materia=nome_materia )
            session.add(professor)
            session.commit()
            print(f"professor adicionado com sucesso!")
        except Exception as erro:
            session.rollback()
            print(f"Ocorreu um erro: {erro}")
# inserir_professor()

def inserir_aluno():
    with Session() as session:
        try:
            nome_alunos = input("Digite o nome dos alunos: ").capitalize()
            nome_RA = input("Digite seu RA: ").capitalize()

            alunos = Alunos(nome=alunos, nome_RA=RA )
            session.add(alunos)
            session.commit()
            print(f"professor adicionado com sucesso!")
        except Exception as erro:
            session.rollback()
            print(f"Ocorreu um erro: {erro}")
