#include "sensors.hpp"

i2cMock::i2cMock(uint8_t deviceAddress):
    deviceAddress(deviceAddress),
    readIndex(0){
        dataSimulation = {0x22, 0xB8};
    }

void i2cMock::write(uint8_t reg, uint8_t value){
    if (reg < dataSimulation.size()){
        dataSimulation[reg] = value;
    }
}

uint8_t i2cMock::read(uint8_t reg){
    if (reg < dataSimulation.size()){
        return dataSimulation[reg];
    }
    return 0;
}

/**
 * @brief Constructor van een nieuw SCD4X::SCD4X object
 * 
 */
SCD4X::SCD4X(uint8_t deviceAddress) :
    i2c(deviceAddress)
    {}

/**
 * @brief leest de luchtvochtigheidswaarden (dummy functie)
 * 
 * Deze methode stuurt de gemeten luchtvochtigheidswaarden terug.
 * 
 * @return double 
 */
double SCD4X::readHumidity(){
    // dummy waarden voor de functie
    return simulatedHumidity;
}

void SCD4X::setSimulatedHumidity(double value){
    simulatedHumidity = value;
}
/**
 * @brief Constructor van een nieuw VEML6030::VEML6030 object
 * 
 */
VEML6030::VEML6030(uint8_t deviceAddress):
    i2c(deviceAddress)
    {}

/**
 * @brief leest de licht intensiteit (dummy functie)
 * 
 * Deze methode stuurt de gemeten lichtintensiteit in lux.
 * 
 * @return double 
 */
double VEML6030::readBrightness(){
    // dummy waarden voor de functie
    return simulatedBrightness;
}

void VEML6030::setSimulatedBrightness(double value){
    simulatedBrightness = value;
}