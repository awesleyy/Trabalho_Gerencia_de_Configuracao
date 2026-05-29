from backend.src.models.produto import Produto

produto1 = Produto.cadastrar_produto()
produto1.ver_produto()
produto1.editar_nome()
produto1.ver_produto()
produto1.editar_preco()
produto1.ver_produto()