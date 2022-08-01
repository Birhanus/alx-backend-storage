-- SQL script that ranks country origins of bands orderd by the number of
-- (no-unique) fans

SELECT origin, fans AS nb_fans FROM metal_bands
ORDER BY fans DESC 


