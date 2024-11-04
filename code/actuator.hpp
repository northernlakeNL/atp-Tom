#ifndef ACTUATOR_HPP
#define ACTUATOR_HPP

class Fan{
    private:
        bool fanState;
        const int pin; // dummy pin       
    public:
    Fan();

    void startFan();
    
    void stopFan();

    bool getState() const;
};

class Humidifier{
    private:
        bool humidifierState;
        const int pin; // dummy pin
    public:
    Humidifier();

    void turnHumidifierOn();
    
    void turnHumidifierOff();

    bool getState() const;
};

class Light{
    private:
        bool lightState;
        const int pin; // dummy pin        
    public:
    Light();

    void turnLightOn();

    void turnLightOff();

    bool getState() const;
};

#endif // ACTUATOR_HPP