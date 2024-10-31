#ifndef SENSORS_HPP
#define SENSORS_HPP

#include <iostream>
#include <vector>

class i2cMock{
    private:
        uint8_t deviceAddress;
        std::vector<uint8_t> dataSimulation;
        size_t readIndex;

    public:
        i2cMock(uint8_t deviceAddress);
        void begin();
        void TransmissionStart(uint8_t deviceAddress);
        void TransmissionStop();
        void write(uint8_t data);
        uint8_t request(uint8_t deviceAddress, uint8_t quantity);
        int read();
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
};

#endif // SENSORS_HPP