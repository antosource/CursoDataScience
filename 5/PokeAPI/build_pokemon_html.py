from string import Template
import data as d
from get_base_info import get_base_pokemon

def build_html(base_info, doc_template, card_template = d.single_card):
    tipos = 'Lorem_ipsum'
    
    # PASO2
    stats_temp = Template('<td><h5><$stat_name: $value</h5></td>')
    stats = '\n'.join([stat_temp.substitute(stat_name = d.stats_es[stat_info[0]], value = stat_info[1]) for stat_info in base_info['stats']])
    
    # PASO3
    etapa_previa = 'Lorem_ipsum'
    
    # PASO4
    tipo_esp = 'Lorem_ipsum'
    
    # PASO5
    super_ef = 'Lorem_ipsum'
    debil = 'Lorem_ipsum'
    resistente = 'Lorem_ipsum'
    poco_ef='Lorem_ipsum'
    inmune = 'Lorem_ipsum'
    inef = 'Lorem_ipsum'
    tipo_esp = 'Lorem_ipsum'
    etapa_previa = 'Lorem_ipsum'    
    
    #(tipo='other', tipo_name = d.especial_es[k]) for k,v in species_info['especial'].items() if v])
    
    
    card = card_template.substitute(id = base_info['id'],
                                    name = base_info['name'],
                                    url = base_info['img'],
                                    tipos = tipos,
                                    descripcion = '',
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
    return doc_template.substitute(body = card)   