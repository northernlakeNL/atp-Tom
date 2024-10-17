#ifndef SENSORS_HPP
#define SENSORS_HPP

/**
 * @brief Een klasse voor een SCD4X
 * 
 * De klasse biedt een interface voor het meten van luchtvochitgheid waarden met gebruik van een SCD4X.
 * De methode readHumidity() is een dummy functie.
 */
class SCD4X{
    public:
    /**
     * @brief Constructor voor een nieuw SCD4X object
     * 
     * Een constructor voor de initialisatie van een SCD4X object.
     */
    SCD4X();
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
    public:
    /**
     * @brief Constructor voor een nieuw VEML6030 object.
     * 
     * Een constructor voor de initialisatie van een VEML6030 object.
     */
    VEML6030();
    /**
     * @brief een dummy functie voor een VEML6030 object.
     * 
     * @return double (een dummy reading)
     */
    double readLightIntensity();
};

#endif // SENSORS_HPP