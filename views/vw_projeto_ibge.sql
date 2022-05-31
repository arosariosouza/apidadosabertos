create view dbplataformabr.vw_projeto_ibge as
select
	replace(tp.nu_caae, '.', '') nu_caae,
	tp.nu_caae nu_caae_fmt,
	tp.ds_titulo_publico,
	tp.no_comite_etica,
	ti.cidade municipio_comite_etica,
	ti.uf uf_comite_etica,
	tp.dt_primeira_submissao,
	tp.co_seq_parecer,
	tp.dt_submissao,
	tp.dt_parecer,
	tp.st_parecer,
	tp.no_instituicao,
	ti2.cidade municipio_instituicao,
	ti2.uf uf_instituicao
from
	dbplataformabr.tb_projeto as tp
left join
	dbgeral.tb_ibge as ti on cast(tp.co_municipio_ibge_cep as int) = ti.ibge
left join
	dbgeral.tb_ibge as ti2 on cast(tp.co_municipio_ibge_instituicao as int) = ti.ibge;