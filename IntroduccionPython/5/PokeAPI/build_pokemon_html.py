from email.mime import base
from string import Template
from get_types import get_types_info
import data as d

def build_html(base_info, base_species, doc_template = d.document_template, card_template = d.single_card):

    # Estadisticas
    stats_templ = Template('<td><FONT FACE="small fonts" size=3>$stat_name: $value </FONT></td>')
    stats = '\n'.join(stats_templ.substitute(stat_name = d.stats_es[stat_info[0]], value = stat_info[1]) for stat_info in base_info['stats'])

    # Datos desde species
    etapa_previa= f"<p style='font-style: italic; font-size: 14px; text-align: center'>Etapa previa: {base_species['previo']}</p>" 
    description = base_species['descr']

    # Tipos 
    tipos_templ = Template('<span class="label $label_class"> $value_class </span>')
    tipos = ''.join(tipos_templ.substitute(label_class = tipo_info, value_class=d.tipo_es[tipo_info])for tipo_info in base_info['tipo'])
    if base_species['tipo_esp']=='': tipo_esp=''
    else: tipo_esp = tipos_templ.substitute(label_class = base_species['tipo_esp'],value_class= base_species['tipo_esp'] )

    # Obtener Fortalezas y resistencias
    rel= get_types_info(base_info['tipo'])

    # Publicar Fortalezas y resistencias 
    sef_templ = Template('<span class="label $label_class"> $value_class </span>')
    super_ef = ''.join(sef_templ.substitute(label_class = tipo_rel, value_class=d.tipo_es[tipo_rel])for tipo_rel in rel['double_damage_to'])

    deb_templ = Template('<span class="label $label_class"> $value_class </span>')
    debil = ''.join(deb_templ.substitute(label_class = tipo_rel, value_class=d.tipo_es[tipo_rel])for tipo_rel in rel['double_damage_from'])

    res_templ = Template('<span class="label $label_class"> $value_class </span>')
    resistente = ''.join(res_templ.substitute(label_class = tipo_rel, value_class=d.tipo_es[tipo_rel])for tipo_rel in rel['half_damage_from'])

    poc_templ = Template('<span class="label $label_class"> $value_class </span>')
    poco_ef = ''.join(poc_templ.substitute(label_class = tipo_rel, value_class=d.tipo_es[tipo_rel])for tipo_rel in rel['half_damage_to'])

    inm_templ = Template('<span class="label $label_class"> $value_class </span>')
    inmune = ''.join(inm_templ.substitute(label_class = tipo_rel, value_class=d.tipo_es[tipo_rel])for tipo_rel in rel['no_damage_from'])

    ine_templ = Template('<span class="label $label_class"> $value_class </span>')
    inef = ''.join(ine_templ.substitute(label_class = tipo_rel, value_class=d.tipo_es[tipo_rel])for tipo_rel in rel['no_damage_to'])

    card = card_template.substitute(id = base_info['id'],
                                    name = base_info['name'],
                                    url = base_info['img'],
                                    tipos = tipos,
                                    description = description,
                                    stats = stats,
                                    table = stats,
                                    super_ef = super_ef,
                                    debil = debil,
                                    resistente = resistente,
                                    poco_ef = poco_ef,
                                    inmune = inmune,
                                    inef = inef,
                                    tipo_especial = tipo_esp,
                                    etapa_previa = etapa_previa)
    return doc_template.substitute(body=card)   

#Testing
if __name__ == '__main__':
   from get_base_info import get_base_pokemon

   name = 'articuno'
   print(get_base_pokemon(name))

   
   
   
  

