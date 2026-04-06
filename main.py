from sqlalchemy import create_engine, Column, Integer , String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

engine = create_engine("sqlite:///muitos_para_dados.db",encho=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)

class Professor(Base):
    __tablename__= "professor"

    id = Column(Integer,primary_key=True)
    nome = Column(String(100),nullable=False)
    materia = Column(String(100))

    aulas = relationship("Aula", back_populates="Professor", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Professor(id={self.id}, nome='{self.nome}')>"
    
