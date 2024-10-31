#include "sensors.hpp"

i2cMock::i2cMock(uint8_t deviceAddress):
    deviceAddress(deviceAddress),
    readIndex(0){
        dataSimulation = {0x22, 0xB8};
    }




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
    return 50;
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
double VEML6030::readBrightness(){
    // dummy waarden voor de functie
    return 400;
}
