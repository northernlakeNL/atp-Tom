#ifndef SENSORS_HPP
#define SENSORS_HPP

#include <iostream>
#include <vector>
#include <cstdint>

class i2cMock{
    private:
        uint8_t deviceAddress;
        std::vector<uint8_t> dataSimulation;
        size_t readIndex;

    public:
        i2cMock(uint8_t deviceAddress);
        void write(uint8_t reg, uint8_t value);
        uint8_t read(uint8_t reg);
};

/**
 * @brief Een klasse voor een SCD4X
 * 
 * De klasse biedt een interface voor het meten van luchtvochitgheid waarden met gebruik van een SCD4X.
 * De methode readHumidity() is een dummy functie.
 */
class SCD4X{
    private:
        i2cMock i2c;
        double simulatedHumidity;
    public:
    /**
     * @brief Constructor voor een nieuw SCD4X object
     * 
     * Een constructor voor de initialisatie van een SCD4X object.
     */
    SCD4X(uint8_t deviceAddress);
    /**
     * @brief een dummy functie voor het SCD4X object.
     * 
     * @return double  (een dummy reading)
     */
    double readHumidity();
    void setSimulatedHumidity(double value);
};

/**
 * @brief een klasse voor een VEML6030
 * 
 * De klasse biedt een interface voor het meten van lichtintensiteit met gebruik van een VEML6030.
 * De methode readLightIntensity() is een dummy functie.
 */
class VEML6030{
    private:
        i2cMock i2c;
        double simulatedBrightness;
    public:
    /**
     * @brief Constructor voor een nieuw VEML6030 object.
     * 
     * Een constructor voor de initialisatie van een VEML6030 object.
     */
    VEML6030(uint8_t deviceAddress);
    /**
     * @brief een dummy functie voor een VEML6030 object.
     * 
     * @return double (een dummy reading)
     */
    double readBrightness();

    void setSimulatedBrightness(double value);
};

#endif // SENSORS_HPP