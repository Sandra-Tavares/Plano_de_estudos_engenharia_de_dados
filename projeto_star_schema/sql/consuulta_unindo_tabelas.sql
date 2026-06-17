select a.*,
		b.*,
		c.*,
		d.*,
		e.*
from fato_entrega AS a
left join dim_regiao AS b
ON a.id_regiao = b.id_regiao
left join dim_produto AS c
ON a.id_produto = c.id_produto
left join dim_tempo AS d
ON a.id_tempo = d.id_tempo
left join dim_motorista As e
ON a.id_motorista = e.id_motorista