#include "sensors.hpp"
/**
 * @brief Constructor van een nieuw SCD4X::SCD4X object
 * 
 */
SCD4X::SCD4X(){}

/**
 * @brief leest de luchtvochtigheidswaarden (dummy functie)
 * 
 * Deze methode stuurt de gemeten luchtvochtigheidswaarden terug.
 * 
 * @return double 
 */
double SCD4X::readHumidity(){
    // dummy waarden voor de functie
    return 50.3;
}
/**
 * @brief Constructor van een nieuw VEML6030::VEML6030 object
 * 
 */
VEML6030::VEML6030(){}

/**
 * @brief leest de licht intensiteit (dummy functie)
 * 
 * Deze methode stuurt de gemeten lichtintensiteit in lux.
 * 
 * @return double 
 */
double VEML6030::readLightIntensity(){
    // dummy waarden voor de functie
    return 1000.4;
}
