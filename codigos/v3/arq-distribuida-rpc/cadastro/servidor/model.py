from datetime import datetime
import db
from sqlalchemy import Column, Float, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

class Cliente(db.Base):

    __tablename__ = 'cliente'

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    cpf = Column(String, nullable=False)
    dtNascimento = Column(DateTime, nullable=False)
    dt_hr_manutencao = Column(DateTime, default=datetime.now,
                              onupdate=datetime.now)
    endereco = relationship("Endereco", cascade="all, delete",
                            passive_deletes=True)



    def __repr__(self):
        """
            Representação do objeto com foco no programador.
        """
        return '<Cliente: %s, %s, %s, %d, %s, %s>' % (self.nome,
                self.cpf, self.dtNascimento, self.id, self.endereco,
                self.dt_hr_manutencao)


class Endereco(db.Base):

    __tablename__ = 'endereco'

    id = Column(Integer, primary_key=True)
    logradouro = Column(String, nullable=False)
    numero = Column(String)
    bairro = Column(String, nullable=False)
    cidade = Column(String, nullable=False)
    estado = Column(String, nullable=False)
    cliente_id = Column(Integer,
                        ForeignKey("cliente.id",
                                    ondelete="CASCADE"),
                        )
    dt_hr_manutencao = Column(DateTime, default=datetime.now,
                              onupdate=datetime.now)

    def __repr__(self):
        """
            Representação do objeto com foco no programador.
        """
        return '<Endereco: %s, %s, %s, %s, %s, %d, %d, %s>' % (
            self.logradouro, self.numero, self.bairro,
            self.cidade, self.estado, self.id, self.cliente_id,
            self.dt_hr_manutencao)

class Venda(db.Base):

    __tablename__ = 'venda'

    id = Column(Integer, primary_key=True)
    cliente_id = Column(Integer, ForeignKey('cliente.id'), nullable=False)
    valor = Column(Float, nullable=False)
    data = Column(DateTime, nullable=False, default=datetime.now)
    itens = relationship("ItemVenda", back_populates="venda", cascade="all, delete-orphan")

    def __repr__(self):
        """
            Representação do objeto com foco no programador.
        """
        return f'<Venda: {self.id}, Cliente ID: {self.cliente_id}, Valor: {self.valor}, Data: {self.data}>'


class ItemVenda(db.Base):

    __tablename__ = 'item_venda'

    id = Column(Integer, primary_key=True)
    venda_id = Column(Integer, ForeignKey('venda.id'), nullable=False)
    produto = Column(String, nullable=False)
    quantidade = Column(Integer, nullable=False)
    preco_unitario = Column(Float, nullable=False)

    venda = relationship("Venda", back_populates="itens")

    def __repr__(self):
        """
            Representação do objeto com foco no programador.
        """
        return f'<ItemVenda: {self.id}, Venda ID: {self.venda_id}, Produto: {self.produto}, Quantidade: {self.quantidade}, Preço Unitário: {self.preco_unitario}>'

