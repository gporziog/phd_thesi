# apro il file erna template
fox_template = open("erna_v2_2_template.fox", "r")
fox_string_template=fox_template.read()
fox_template.close()

# modifico i dati del drift lenght 
# se  on dovesse servire commentare tutto da #### a ########
####
CSSM_TRIPL_to_search="<___CSSM_TRIPL>"
CSSM_TRIPL_to_replace="0.1111"
fox_string_template=fox_string_template.replace(CSSM_TRIPL_to_search, CSSM_TRIPL_to_replace)

TRIPL_SLIT1_to_search="<___trip_slit1>"
TRIPL_SLIT1_to_replace="0.2222"
fox_string_template=fox_string_template.replace(TRIPL_SLIT1_to_search, TRIPL_SLIT1_to_replace)


TRIPL_SLIT1_to_search="<___slit2_singl1>"
TRIPL_SLIT1_to_replace="0.3333"
fox_string_template=fox_string_template.replace(TRIPL_SLIT1_to_search, TRIPL_SLIT1_to_replace)

TRIPL_SLIT1_to_search="<___singl1_dipole>"
TRIPL_SLIT1_to_replace="0.4444"
fox_string_template=fox_string_template.replace(TRIPL_SLIT1_to_search, TRIPL_SLIT1_to_replace)

TRIPL_SLIT1_to_search="<___slitdip_dip_exit>"
TRIPL_SLIT1_to_replace="0.55555"
fox_string_template=fox_string_template.replace(TRIPL_SLIT1_to_search, TRIPL_SLIT1_to_replace)

TRIPL_SLIT1_to_search="<___dip_exit_doubl>"
TRIPL_SLIT1_to_replace="0.6666"
fox_string_template=fox_string_template.replace(TRIPL_SLIT1_to_search, TRIPL_SLIT1_to_replace)

TRIPL_SLIT1_to_search="<___doubl_slit3>"
TRIPL_SLIT1_to_replace="0.7777"
fox_string_template=fox_string_template.replace(TRIPL_SLIT1_to_search, TRIPL_SLIT1_to_replace)

TRIPL_SLIT1_to_search="<___slit3_SEPWF2>"
TRIPL_SLIT1_to_replace="0.8888"
fox_string_template=fox_string_template.replace(TRIPL_SLIT1_to_search, TRIPL_SLIT1_to_replace)

TRIPL_SLIT1_to_search="<___SEPWF2_slit4>"
TRIPL_SLIT1_to_replace="0.9999"
fox_string_template=fox_string_template.replace(TRIPL_SLIT1_to_search, TRIPL_SLIT1_to_replace)

TRIPL_SLIT1_to_search="<___slit4_MCP>"
TRIPL_SLIT1_to_replace="0.9011"
fox_string_template=fox_string_template.replace(TRIPL_SLIT1_to_search, TRIPL_SLIT1_to_replace)
########

# di seguito la sezione per modificare i dati degli elementi ottici
#CSSM
r_cssm_to_search="<___r_CSSM>"
r_cssm_to_replace="0.476"
fox_string_template=fox_string_template.replace(r_cssm_to_search, r_cssm_to_replace)
cssm_bending_to_search="<___CSSM_bending>"
cssm_bending_to_replace="0.30"
fox_string_template=fox_string_template.replace(cssm_bending_to_search, cssm_bending_to_replace)

# per gli elementi quali tripletti e quadrupoli che invocano questa funzione di COSY:
# "PROCEDURE MagneticQuadrupole length flux_density_at_pole_tip aperture"
#si agirà solo su "lenght" e "aperture"

# quadrupolo lenght and aperture of first element

quad_lenght_search_first="<_(-)_quad_lenght>"
quad_lenght_replace_first="0.230"
fox_string_template=fox_string_template.replace(quad_lenght_search_first, quad_lenght_replace_first)

quad_aperture_search_first="<_(-)_quad_aperture>"    
quad_aperture_replace_first="0.0521"
fox_string_template=fox_string_template.replace(quad_aperture_search_first, quad_aperture_replace_first)

#quadrupolo lenght and aperture of second element

quad_lenght_search_second="<_(+)_quad_lenght>"
quad_lenght_replace_second="0.230"
fox_string_template=fox_string_template.replace(quad_lenght_search_second, quad_lenght_replace_second)

quad_aperture_search_second="<_(+)_quad_aperture>"    
quad_aperture_replace_second="0.0521"
fox_string_template=fox_string_template.replace(quad_aperture_search_second, quad_aperture_replace_second)

#singoletto
single_lenght_search="<___single_lenght>"
single_lenght_replace="0.180"
fox_string_template=fox_string_template.replace(single_lenght_search, single_lenght_replace)

single_aperture_search="<___single_aperture>"    
single_aperture_replace="0.0385"
fox_string_template=fox_string_template.replace(single_aperture_search, single_aperture_replace)

















#tripletto lenght and aperture of first element

trip_lenght_search_first="<_(-)_trip_lenght>"
trip_lenght_replace_first="0.190"
fox_string_template=fox_string_template.replace(trip_lenght_search_first, trip_lenght_replace_first)

trip_aperture_search_first="<_(-)_trip_aperture>"    
trip_aperture_replace_first="0.053"
fox_string_template=fox_string_template.replace(trip_aperture_search_first, trip_aperture_replace_first)

#tripletto lenght and aperture of second element

trip_lenght_search_second="<_(+)_trip_lenght>"
trip_lenght_replace_second="0.290"
fox_string_template=fox_string_template.replace(trip_lenght_search_second, trip_lenght_replace_second)

trip_aperture_search_second="<_(+)_trip_aperture>"    
trip_aperture_replace_second="0.053"
fox_string_template=fox_string_template.replace(trip_aperture_search_second, trip_aperture_replace_second)

#tripletto lenght and aperture of third element

trip_lenght_search_third="<_(-)_trip_lenght>"
trip_lenght_replace_third="0.190"
fox_string_template=fox_string_template.replace(trip_lenght_search_third, trip_lenght_replace_third)

trip_aperture_search_third="<_(-)_trip_aperture>"    
trip_aperture_replace_third="0.053"
fox_string_template=fox_string_template.replace(trip_aperture_search_third, trip_aperture_replace_third)


#tripletto di focalizazione, lenght and aperture of first element

foctrip_lenght_search_first="<_(-)_foctrip_lenght>"
foctrip_lenght_replace_first="0.190"
fox_string_template=fox_string_template.replace(foctrip_lenght_search_first, foctrip_lenght_replace_first)

foctrip_aperture_search_first="<_(-)_foctrip_aperture>"    
foctrip_aperture_replace_first="0.053"
fox_string_template=fox_string_template.replace(foctrip_aperture_search_first, foctrip_aperture_replace_first)

#tripletto lenght and aperture of second element

foctrip_lenght_search_second="<_(+)_foctrip_lenght>"
foctrip_lenght_replace_second="0.290"
fox_string_template=fox_string_template.replace(foctrip_lenght_search_second, foctrip_lenght_replace_second)

foctrip_aperture_search_second="<_(+)_foctrip_aperture>"    
foctrip_aperture_replace_second="0.053"
fox_string_template=fox_string_template.replace(foctrip_aperture_search_second, foctrip_aperture_replace_second)

#tripletto lenght and aperture of third element

foctrip_lenght_search_third="<_(-)_foctrip_lenght>"
foctrip_lenght_replace_third="0.190"
fox_string_template=fox_string_template.replace(foctrip_lenght_search_third, foctrip_lenght_replace_third)

foctrip_aperture_search_third="<_(-)_foctrip_aperture>"    
foctrip_aperture_replace_third="0.053"
fox_string_template=fox_string_template.replace(foctrip_aperture_search_third, foctrip_aperture_replace_third)


# per il 60 gradi 
dipole60deg_radius_search="<___60deg_radius>"
dipole60deg_radius_replace="0.367"
fox_string_template=fox_string_template.replace(dipole60deg_radius_search, dipole60deg_radius_replace)

dipole60deg_aperture_search="<___60deg_aperture>"
dipole60deg_aperture_replace="0.375"
fox_string_template=fox_string_template.replace(dipole60deg_aperture_search, dipole60deg_aperture_replace)
  


# apro il file erna di destinazione

fox_erna = open("erna_v2_2.fox", "w")
fox_erna.write(fox_string_template)
print(fox_string_template)
fox_erna.close()

