create view dbplataformabr.vw_projeto_ibge as
select
	co_seq_projeto,
	replace(tp.nu_caae, '.', '') nu_caae,
	tp.ds_titulo_publico,
	tp.no_comite_etica,
	ti.cidade municipio_comite_etica,
	ti.uf uf_comite_etica,
	tp.dt_primeira_submissao,
	tp.co_seq_parecer,
	tp.dt_submissao,
	tp.dt_parecer,
	case lower(st_parecer)
		when 'aprovado' then 1
		when 'aprovado com recomendacão' then 2
		when 'devolvido com recomendacão' then 3
		when 'não aprovado' then 4
		when 'pendente' then 5
		when 'retirado' then 6
		else null
	end co_st_parecer,
	tp.st_parecer,	
	tp.no_instituicao,
	ti2.cidade municipio_instituicao,
	sg_uf_instituicao
from
	dbplataformabr.tb_projeto as tp
left join
	dbgeral.tb_ibge as ti on cast(tp.co_municipio_ibge_cep as int) = ti.ibge
left join
	dbgeral.tb_ibge as ti2 on cast(tp.co_municipio_ibge_instituicao as int) = ti2.ibge;